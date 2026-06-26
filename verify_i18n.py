import os
import re

dir_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes"
files = ["index.html", "about.html", "space.html", "menu.html", "menu-photos.html"]

for filename in files:
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    keys = set(re.findall(r'data-i18n=["\']([^"\']+)["\']', html))
    
    # Try to extract the translations object
    translations_match = re.search(r'const translations = (\{.*?\});\s*let currentLang', html, re.DOTALL)
    if translations_match:
        # Just check if 'fr: {' or 'en: {' is in there, and check if all keys are present
        trans_str = translations_match.group(1)
        missing_keys = []
        for key in keys:
            if f'"{key}":' not in trans_str and f"'{key}':" not in trans_str:
                missing_keys.append(key)
        print(f"{filename}: Found translations object. Missing keys: {missing_keys}")
    else:
        print(f"{filename}: Missing translations object! Found keys: {keys}")
