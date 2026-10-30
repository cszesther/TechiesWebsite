"""Export public SSR pages for visual review, never the CMS or its database."""
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import parse_qs, unquote, urljoin, urlsplit
from urllib.request import urlopen

ORIGIN = 'http://localhost:4333'
OUT = Path('.preview/site')
MEDIA_PREFIX = '/_emdash/api/media/file/'


def public_url(value):
    url = urlsplit(urljoin(ORIGIN, value))
    if url.path == '/_image':
        source = parse_qs(url.query).get('href', [''])[0]
        return public_url(source) if source else value
    if url.hostname in ('localhost', '127.0.0.1'):
        if url.path.startswith(MEDIA_PREFIX):
            return '/preview-media/' + url.path[len(MEDIA_PREFIX):]
        return url.path + ('?' + url.query if url.query else '') + ('#' + url.fragment if url.fragment else '')
    return value


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.output, self.links, self.images = [], set(), set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'a' and values.get('href'):
            url = urlsplit(urljoin(ORIGIN, values['href']))
            if url.netloc == urlsplit(ORIGIN).netloc and not url.path.startswith(('/_emdash', '/_astro', '/api/')):
                if url.query:
                    raise ValueError('Snapshot does not support query pagination: ' + values['href'])
                self.links.add(url.path or '/')
        rewritten = []
        for key, value in attrs:
            if value is not None:
                if key in ('src', 'href', 'poster', 'action'):
                    value = public_url(value)
                elif key == 'srcset':
                    value = re.sub(r'/_image\?[^\s,]+', lambda m: public_url(m[0]), value)
                if key in ('src', 'srcset'):
                    self.images.update(re.findall(r'/preview-media/[^\s,]+', value))
            rewritten.append(key if value is None else f'{key}="{html.escape(value, quote=True)}"')
        if tag == 'form' and values.get('method') != 'dialog':
            raise ValueError('Interactive forms need an explicit snapshot fallback; refusing export')
        self.output.append('<' + tag + (' ' + ' '.join(rewritten) if rewritten else '') + '>')
        if tag == 'head':
            self.output.append('<meta name="robots" content="noindex, nofollow">')
        if tag == 'body':
            self.output.append('<aside style="padding:10px 20px;background:#fbf8ef;color:#080b12;font:14px/1.5 Inter,sans-serif;text-align:center">Design preview · bundled reference content · CMS editing stays local</aside>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
    def handle_endtag(self, tag):
        self.output.append(f'</{tag}>')
    def handle_data(self, data):
        self.output.append(data)
    def handle_entityref(self, name):
        self.output.append('&' + name + ';')
    def handle_charref(self, name):
        self.output.append('&#' + name + ';')
    def handle_comment(self, data):
        self.output.append('<!--' + data + '-->')
    def handle_decl(self, data):
        self.output.append('<!' + data + '>')


def check():
    assert public_url('/_image?href=http%3A%2F%2Flocalhost%3A4331%2F_emdash%2Fapi%2Fmedia%2Ffile%2Fphoto.jpg&w=600') == '/preview-media/photo.jpg'
    p = Page()
    p.feed('<a href="/posts/roast-7#speaker">Read</a><img src="/_emdash/api/media/file/photo.jpg" alt="A &amp; B">')
    assert p.links == {'/posts/roast-7'} and p.images == {'/preview-media/photo.jpg'}
    assert 'A &amp; B' in ''.join(p.output)
    p.feed('<form method="dialog"><button>Close</button></form>')
    print('Snapshot URL/parser checks passed')


def main():
    check()
    # Only this generated directory is replaced; local CMS state is never touched.
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree('dist/client', OUT)
    pending, visited, images = {'/', '/events', '/people', '/posts'}, set(), set()
    while pending:
        route = pending.pop()
        if route in visited:
            continue
        decoded = unquote(route)
        if '..' in decoded.split('/') or not decoded.startswith('/'):
            raise ValueError('Unsafe snapshot path: ' + route)
        with urlopen(ORIGIN + route, timeout=30) as response:
            if response.status != 200 or 'text/html' not in response.headers.get('Content-Type', ''):
                raise ValueError('Expected public HTML: ' + route)
            page = Page()
            page.feed(response.read().decode())
        if '<h1' not in ''.join(page.output):
            raise ValueError('Missing page heading: ' + route)
        path = OUT / decoded.lstrip('/') / 'index.html'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(''.join(page.output))
        visited.add(route)
        images.update(page.images)
        pending.update(page.links - visited)
        if len(visited) > 100:
            raise ValueError('Unexpectedly large snapshot; inspect before publishing')
    # Copy only photos referenced by rendered public content, not the whole library.
    for image in images:
        name = unquote(image.removeprefix('/preview-media/'))
        if '/' in name or name in ('.', '..'):
            raise ValueError('Unsafe media path')
        source = Path('.preview/uploads') / name
        destination = OUT / 'preview-media' / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    (OUT / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
    (OUT / '_headers').write_text('/*\n  X-Robots-Tag: noindex, nofollow\n  X-Content-Type-Options: nosniff\n')
    manifest = {'kind': 'read-only design snapshot', 'routes': sorted(visited), 'photos': len(images)}
    (OUT / 'preview-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Exported {len(visited)} pages and {len(images)} referenced photos to {OUT}')


if __name__ == '__main__':
    check() if '--check' in sys.argv else main()
