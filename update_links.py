import os
import re

dir_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes"
files = ["index.html", "about.html", "space.html", "menu.html", "menu-photos.html"]

replacements = {
    "nav-home": "index.html",
    "nav-about": "about.html",
    "nav-space": "space.html",
    "nav-menu": "menu.html",
    "nav-reservation": "index.html#reservation"
}

for filename in files:
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # We need to replace href="..." inside the <a> tag that has data-i18n="<key>"
    for key, new_href in replacements.items():
        # Match <a ... href="..." ... data-i18n="key" ... >
        # Need to be careful because attributes can be in any order, 
        # but usually href comes before data-i18n.
        # Let's just use a regex that finds the href before the data-i18n in the same tag.
        pattern = re.compile(r'(<a\s+[^>]*?)href="[^"]*"([^>]*?data-i18n="' + key + r'")', re.DOTALL | re.IGNORECASE)
        content = pattern.sub(r'\1href="' + new_href + r'"\2', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Links updated successfully.")
