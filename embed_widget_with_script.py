import os

html_path = "index.html"

# Widget block with no duplicate script tag
widget_block = '''
<div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: flex-start; margin-top: 2rem;">
  <div style="flex: 1; min-width: 250px;">
    <h2>501(c)(3) ready</h2>
    <p>We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>
  </div>
  <div style="flex: 1; min-width: 300px; max-width: 400px;">
    <div class="gfm-embed" data-url="https://www.gofundme.com/f/help-hpra-build-a-safer-digital-world/widget/large?sharesheet=undefined&attribution_id=sl:9edbdbcf-4184-44b5-9ffa-679f9829d938"></div>
  </div>
</div>
'''

# Script tag to load GoFundMe widget
script_tag = '<script defer src="https://www.gofundme.com/static/js/embed.js"></script>'

# Read the HTML file
with open(html_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace the original section with the widget-enhanced block
content = content.replace(
    '<h2>501(c)(3) ready</h2>\n<p>We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>',
    widget_block
)

# Ensure the script tag is present before </body>
if script_tag not in content:
    content = content.replace("</body>", f"{script_tag}\n</body>")

# Save the updated file
with open(html_path, "w", encoding="utf-8") as file:
    file.write(content)

print("✅ Widget embedded and script tag ensured.")
