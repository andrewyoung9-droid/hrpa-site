import os

# Path to your HTML file
html_path = "index.html"

# Widget HTML block
widget_html = '''
<div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: flex-start; margin-top: 2rem;">
  <div style="flex: 1; min-width: 250px;">
    <h2>501(c)(3) ready</h2>
    <p>We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>
  </div>
  <div style="flex: 1; min-width: 300px; max-width: 400px;">
    <div class="gfm-embed" data-url="https://www.gofundme.com/f/help-hpra-build-a-safer-digital-world/widget/large?sharesheet=undefined&attribution_id=sl:9edbdbcf-4184-44b5-9ffa-679f9829d938"></div>
    <script defer src="https://www.gofundme.com/static/js/embed.js"></script>
  </div>
</div>
'''

# Read and update the file
with open(html_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace the original section with the widget-enhanced version
updated_content = content.replace(
    '<h2>501(c)(3) ready</h2>\n<p>We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>',
    widget_html
)

# Save the updated file
with open(html_path, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("✅ GoFundMe widget successfully embedded.")
