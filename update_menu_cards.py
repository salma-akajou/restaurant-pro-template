import re

content = open(r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\menu-photos.html', encoding='utf-8').read()

sections = re.split(r'<h2[^>]*>', content)

def get_4_cards(section_text, category):
    cards = re.findall(r'(<div class="dish-photo-card.*?</p>\s*</div>\s*</div>)', section_text, re.DOTALL)
    out = []
    for c in cards[:4]:
        c = c.replace('class="dish-photo-card', f'data-category="{category}" class="dish-photo-card menu-item-card')
        if category != 'mains':
            c = c.replace('class="dish-photo-card menu-item-card', 'class="dish-photo-card menu-item-card hidden')
        out.append(c)
    return out

starters = get_4_cards(sections[2], 'starters')
mains = get_4_cards(sections[3], 'mains')
desserts = get_4_cards(sections[5], 'desserts')

print(f'Got {len(starters)} starters, {len(mains)} mains, {len(desserts)} desserts')

# Now apply to index.html
index_path = r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html'
idx_content = open(index_path, encoding='utf-8').read()

# Find the grid
grid_match = re.search(r'(<!-- Grid -->\s*<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 max-w-6xl mx-auto">)(.*?)(</div>\s*<div class="mt-16 text-center fade-up">)', idx_content, re.DOTALL)

if grid_match:
    all_cards = starters + mains + desserts
    cards_html = '\n                <!-- Card -->\n                '.join(all_cards)
    
    new_idx_content = idx_content[:grid_match.start(2)] + '\n' + cards_html + '\n            ' + idx_content[grid_match.end(2):]
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_idx_content)
    print("index.html updated successfully with 12 new cards.")
else:
    print("Could not find the grid in index.html")
