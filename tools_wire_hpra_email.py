from pathlib import Path
import re, json

root = Path(".")
html_files = sorted(root.glob("*.html"))

# ===== Config (HPRA) =====
DOMAIN = "humanprivacyrightsalliance.org"
NAME = "Human Privacy Rights Alliance"

# Footer block to insert (HPRA only)
footer_block = f"""
<div id="contacts-hpra" style="margin-top:1.25rem;font-size:.95rem;line-height:1.5">
  <strong>Contact {NAME}:</strong>
  <a href="mailto:info@{DOMAIN}?subject=General%20Inquiry%20-%20HPRA">info@{DOMAIN}</a> &middot;
  <a href="mailto:help@{DOMAIN}?subject=Support%20Request%20-%20HPRA">help@{DOMAIN}</a> &middot;
  <a href="mailto:security@{DOMAIN}?subject=Vulnerability%20Disclosure%20-%20HPRA">security@{DOMAIN}</a> &middot;
  <a href="mailto:media@{DOMAIN}?subject=Media%20Inquiry%20-%20HPRA">media@{DOMAIN}</a> &middot;
  <a href="mailto:donate@{DOMAIN}?subject=Donation%20Inquiry%20-%20HPRA">donate@{DOMAIN}</a>
</div>
""".strip()

# Minimal Organization JSON-LD for HPRA
json_ld = {
  "@context":"https://schema.org",
  "@type":"Organization",
  "name": NAME,
  "url": f"https://{DOMAIN}/",
  "contactPoint": [
    {"@type":"ContactPoint","contactType":"customer support","email":f"help@{DOMAIN}"},
    {"@type":"ContactPoint","contactType":"security","email":f"security@{DOMAIN}"}
  ]
}
json_ld_tag = '<script type="application/ld+json">'+json.dumps(json_ld, ensure_ascii=False)+'</script>'

def insert_footer(html: str) -> str:
    # Remove any previous HPRA block to avoid duplicates
    html = re.sub(r'<div id="contacts-hpra".*?</div>\s*', '', html, flags=re.I|re.S)
    # Prefer placing inside <footer>, else before </body>, else append
    if re.search(r"</footer>", html, flags=re.I):
        return re.sub(r"</footer>", footer_block + "\n</footer>", html, count=1, flags=re.I)
    if re.search(r"</body>", html, flags=re.I):
        return re.sub(r"</body>", footer_block + "\n</body>", html, count=1, flags=re.I)
    return html + "\n" + footer_block + "\n"

def insert_json_ld(html: str) -> str:
    # Only add if a HPRA JSON-LD isn’t already present (check NAME)
    if re.search(r'application/ld\+json', html, flags=re.I) and (NAME in html):
        return html
    if re.search(r"</head>", html, flags=re.I):
        return re.sub(r"</head>", json_ld_tag + "\n</head>", html, count=1, flags=re.I)
    return html

updated = []
for p in html_files:
    t = p.read_text(encoding="utf-8", errors="ignore")
    t2 = insert_footer(t)
    t3 = insert_json_ld(t2)
    if t3 != t:
        p.write_text(t3, encoding="utf-8")
        updated.append(p.name)

print("Updated files:")
for n in updated:
    print(" -", n)
