import os
import re

dir_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes"
files = ["index.html", "about.html", "space.html", "menu.html", "menu-photos.html"]

# 1. Read about.html to extract its footer
about_path = os.path.join(dir_path, "about.html")
with open(about_path, "r", encoding="utf-8") as f:
    about_content = f.read()

# Extract footer from about.html
footer_match = re.search(r'(<!-- =* FOOTER =* -->\s*)?<footer.*?</footer>', about_content, re.DOTALL | re.IGNORECASE)
if not footer_match:
    print("Could not find footer in about.html")
    exit(1)

footer_html = footer_match.group(0)

# 2. Modify footer padding to minimize space at the bottom
# Replace 'py-16 md:py-24' with 'pt-16 pb-8 md:pt-24 md:pb-8'
footer_html = re.sub(r'py-16 md:py-24', r'pt-16 pb-6 md:pt-24 md:pb-6', footer_html)

# Also update mb-16 on the grid to mb-8 to reduce space between columns and bottom bar
footer_html = re.sub(r'mb-16', r'mb-8', footer_html)

# 3. Replace footer in all files (including about.html itself to apply the padding fix)
for filename in files:
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace existing footer with the new one
    new_content = re.sub(r'(<!-- =* FOOTER =* -->\s*)?<footer.*?</footer>', footer_html, content, flags=re.DOTALL | re.IGNORECASE)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Footers updated successfully.")
