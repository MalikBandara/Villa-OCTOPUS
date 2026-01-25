import os

file_path = r"d:\Our Projects\index.xml"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update showHome function
old_show_home = """    function showHome() {
      // Toggle visibility
      const homeView = document.getElementById('home-view');
      const mainContent = document.getElementById('main-content');
      const roomsSection = document.getElementById('rooms-section');
      const mealsSection = document.getElementById('meals-section');
      const gallerySection = document.getElementById('gallery-section');

      if (roomsSection) roomsSection.style.display = 'none';
      if (mealsSection) mealsSection.style.display = 'none';
      if (gallerySection) gallerySection.style.display = 'none';
      if (homeView) homeView.style.display = 'block';
      if (mainContent) mainContent.style.display = 'block';

      // Scroll to top
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }"""

new_show_home = """    function showHome(scrollToTop = true) {
      // Toggle visibility
      const homeView = document.getElementById('home-view');
      const mainContent = document.getElementById('main-content');
      const roomsSection = document.getElementById('rooms-section');
      const mealsSection = document.getElementById('meals-section');
      const gallerySection = document.getElementById('gallery-section');

      if (roomsSection) roomsSection.style.display = 'none';
      if (mealsSection) mealsSection.style.display = 'none';
      if (gallerySection) gallerySection.style.display = 'none';
      if (homeView) homeView.style.display = 'block';
      if (mainContent) mainContent.style.display = 'block';

      // Scroll to top only if requested
      if (scrollToTop) {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      }
    }"""

if old_show_home in content:
    content = content.replace(old_show_home, new_show_home)
    print("Updated showHome function.")
else:
    print("Could not find exact showHome function to replace.")

# 2. Update Logo Link
old_logo_link = "<a class='logo logo-link' href='#home'>"
new_logo_link = "<a class='logo logo-link' href='#home' onclick='showHome()'>"

if old_logo_link in content:
    content = content.replace(old_logo_link, new_logo_link)
    print("Updated Logo link.")
else:
    print("Could not find Logo link.")

# 3. Update About Link
# This appears in both desktop and mobile menus
old_about_link = "<a href='#about'>About</a>"
new_about_link = "<a href='#about' onclick='showHome(false)'>About</a>"

count_about = content.count(old_about_link)
if count_about > 0:
    content = content.replace(old_about_link, new_about_link)
    print(f"Updated {count_about} About links.")
else:
    print("Could not find About links.")

# 4. Update Contact Link
# This appears in both desktop and mobile menus
old_contact_link = "<a href='#contact'>Contact</a>"
new_contact_link = "<a href='#contact' onclick='showHome(false)'>Contact</a>"

count_contact = content.count(old_contact_link)
if count_contact > 0:
    content = content.replace(old_contact_link, new_contact_link)
    print(f"Updated {count_contact} Contact links.")
else:
    print("Could not find Contact links.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")
