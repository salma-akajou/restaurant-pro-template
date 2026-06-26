import re

with open(r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'data-i18n=["\']([^"\']+)["\']', html)
print(set(matches))
