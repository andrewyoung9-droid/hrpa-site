import os

html_path = "index.html"

# Original KPI block to be replaced
original_kpi = '''
<div class="kpi">
      <h3>501(c)(3) ready</h3>
      <p class="small">We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>
    </div>
'''

# Updated KPI block with GoFundMe widget
updated_kpi = '''
<div class="kpi" style="display: flex; flex-direction: column; gap: 1rem;">
  <div>
    <h3>501(c)(3) ready</h3>
    <p class="small">We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>
  </div>
  <div>
    <div class="gfm-embed" data-url="https://www.gofundme.com/f/help-hpra-build-a-safer-digital-world/widget/large?sharesheet=undefined&attribution_id=sl:9edbdbcf-4184-44b5-9ffa-679f9829d938"></div>
  </div>
</div>
'''

# Script tag to ensure widget loads
script_tag = '<script defer src="https://www.gofundme.com/static/js/embed.js"></script>'

# Read the HTML file
with open(html_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace the original KPI block
if original_kpi in content:
    content = content.replace(original_kpi, updated_kpi)
    print("✅ Replaced KPI block with widget.")
else:
    print("⚠️ Original KPI block not found. No changes made.")

# Ensure the script tag is present before </body>
if script_tag not in content:
    content = content.replace("</body>", f"{script_tag}\n</body>")
    print("✅ Added GoFundMe script tag.")
else:
    print("ℹ️ Script tag already present.")

# Save the updated file
with open(html_path, "w", encoding="utf-8") as file:
    file.write(content)

print("🎉 Widget embedded successfully.")
