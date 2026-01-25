import os

file_path = r"d:\Our Projects\index.xml"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Re-apply Gallery CSS Fix
# Search for the old CSS block and replace it with the new one
old_gallery_css = """      @media (max-width: 768px) {
        .gallery-grid {
          grid-template-columns: repeat(2, 1fr);
          gap: 10px;
        }

        .gallery-grid img {
          height: 150px;
        }
      }"""

new_gallery_css = """      @media (max-width: 768px) {
        .gallery-grid {
          grid-template-columns: 1fr;
          gap: 25px;
        }

        .gallery-grid img {
          height: auto;
          min-height: 300px;
        }
      }"""

if old_gallery_css in content:
    content = content.replace(old_gallery_css, new_gallery_css)
    print("Gallery CSS fix applied.")
else:
    # It might be that the content is slightly different or already applied (unlikely given the user report, but good to check)
    # Let's try a more robust check or just print a warning.
    # Since I know the file state from previous reads, exact match should work if I copied it correctly from the file read.
    # I'll double check the file read output if this fails.
    print("Gallery CSS block not found (might be already applied or different).")

# 2. Re-apply JS Fixes (Remove conflicting lines)
# The lines to remove are:
# const mobileNav = document.getElementById('mobileNav');
# if (mobileNav) mobileNav.classList.remove('active');

js_conflict_block = """      const mobileNav = document.getElementById('mobileNav');
      if (mobileNav) mobileNav.classList.remove('active');"""

# This block appears twice: once in showGallery and once in showMeals.
# We want to remove both occurrences.

count = content.count(js_conflict_block)
if count > 0:
    content = content.replace(js_conflict_block, "")
    print(f"Removed {count} occurrences of conflicting JS.")
else:
    print("Conflicting JS block not found.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")
