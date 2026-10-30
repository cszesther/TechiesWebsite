"""Read-only smoke check against the hosted design snapshot."""
from html.parser import HTMLParser
import json
import re
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ORIGIN = 'https://techies-design-preview.esther-speakeasy.workers.dev'

def fetch(path):
    return urlopen(Request(ORIGIN + path, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30)

class Assets(HTMLParser):
    paths = set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for key in ('src', 'href'):
            value = values.get(key, '')
            if tag in ('img', 'script', 'link') and value.startswith(('/_astro/', '/preview-media/', '/brand/')):
                self.paths.add(value)

with fetch('/preview-manifest.json') as response:
    manifest = json.load(response)
for route in manifest['routes']:
    with fetch(route) as response:
        page = response.read().decode()
        assert response.status == 200
        assert 'noindex' in response.headers.get('X-Robots-Tag', '')
        assert len(re.findall(r'<h1(?:\s|>)', page)) == 1, route
        assert not re.search(r'(?:src|href)="https?://(?:localhost|127\.0\.0\.1)', page), route
        Assets().feed(page)
for path in Assets.paths:
    with fetch(path) as response:
        assert response.status == 200, path
for path in ('/_emdash/admin', '/_emdash/api/content/posts', '/this-route-does-not-exist'):
    try:
        fetch(path)
        raise AssertionError('Unexpected hosted backend: ' + path)
    except HTTPError as error:
        assert error.code == 404, path
print(f"PASS: {len(manifest['routes'])} routes, {len(Assets.paths)} assets, noindex, one H1, no local assets, no hosted CMS/API")
