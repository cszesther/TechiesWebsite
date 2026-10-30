import type { PortableTextBlock } from "emdash";

type TextBlock = {
  _type?: string;
  _key?: string;
  style?: string;
  children?: { text?: string }[];
  markDefs?: { href?: string }[];
  asset?: { _ref?: string };
};

export function articleTitle(title: string) {
  // Only the recognised imported event title loses its redundant date/location.
  return title.replace(/^(Roast My TechStack #\d+)\s*·\s*[A-Za-z]+ \d{1,2}, \d{4}\s*·\s*Singapore$/, "$1");
}

export function headingId(node: { _key?: string }, index = 0) {
  return `article-${node._key || index}`;
}

export function articleOutline(value: PortableTextBlock[] | null | undefined) {
  return (value ?? []).flatMap((value, index) => {
    const node = value as TextBlock;
    if (node._type !== "block" || !/^h[12]$/.test(node.style ?? "")) return [];
    const label = node.children?.map(child => child.text ?? "").join("").trim();
    if (!label) return [];
    const profile = node.markDefs?.find(mark => /^\/(members|people)#/.test(mark.href ?? ""))?.href;
    return [{ id: headingId(node, index), label, profile }];
  });
}

export function withoutRepeatedLead(value: PortableTextBlock[], leadId?: string) {
  // Keep the stored body intact; suppress only its early duplicate of the lead.
  const duplicate = value.findIndex((value, index) => {
    const node = value as TextBlock;
    return index < 4 && node._type === "image" && Boolean(leadId) && node.asset?._ref === leadId;
  });
  return duplicate < 0 ? value : value.filter((_, index) => index !== duplicate);
}
