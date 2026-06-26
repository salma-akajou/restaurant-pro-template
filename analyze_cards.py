import re
from collections import Counter

content = open(r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\menu-photos.html', encoding='utf-8').read()
cards = re.findall(r'<div class="dish-photo-card.*?</p>\s*</div>\s*</div>', content, re.DOTALL)
print('Total cards in menu-photos.html:', len(cards))

categories = []
for c in cards:
    cat_match = re.search(r'data-category="([^"]+)"', c)
    if cat_match:
        categories.append(cat_match.group(1))
    else:
        categories.append('none')

print('Categories:', Counter(categories))
