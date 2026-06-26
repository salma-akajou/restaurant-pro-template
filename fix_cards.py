index_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("menu-item-card hidden group", "menu-item-card group")
content = content.replace('data-category="starters" class="', 'style="display: none;" data-category="starters" class="')
content = content.replace('data-category="desserts" class="', 'style="display: none;" data-category="desserts" class="')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed initial display of hidden cards.")
