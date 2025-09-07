import os

html_path = "index.html"

# Exact block to remove (the second widget section)
duplicate_section = '''
<section style="margin-top: 2rem;">
  <div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: flex-start;">
    <!-- Text Block -->
    <div style="flex: 1; min-width: 250px;">
      <h2>501(c)(3) ready</h2>
      <p>We’re building the documentation, programs, and transparent practices that donors and grantmakers expect.</p>
    </div>

    <!-- GoFundMe Widget -->
    <div style="flex: 1; min-width: 300px; max-width: 400px;">
      <div class="gfm-embed" data-url="https://www.gofundme.com/f/help-hpra-build-a-safer-digital-world/widget/large?sharesheet=undefined&attribution_id=sl:9edbdbcf-4184-44b5-9ffa-679f9829d938"></div>
    </div>
  </div>

  <!-- Required Script -->
  <script defer src="https://www.gofundme.com/static/js/embed.js"></script>
</section>
'''

# Read the HTML file
with open(html_path, "r", encoding="utf-8") as file:
    content = file.read()

# Remove the duplicate section
if duplicate_section in content:
    content = content.replace(duplicate_section, "")
    print("✅ Duplicate widget section removed.")
else:
    print("⚠️ Duplicate widget section not found. No changes made.")

# Save the updated file
with open(html_path, "w", encoding="utf-8") as file:
    file.write(content)

print("🎉 Cleanup complete.")
