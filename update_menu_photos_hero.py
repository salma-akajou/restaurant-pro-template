import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\menu-photos.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

pattern1 = r'src=[\'"]https://images\.unsplash\.com/photo-1544025162-d76694265947\?auto=format&amp;fit=crop&amp;w=1920&amp;q=80[\'"]'
pattern2 = r'src=[\'"]https://images\.unsplash\.com/photo-1544025162-d76694265947\?auto=format&fit=crop&w=1920&q=80[\'"]'

new_content = re.sub(pattern1, 'src="images/image_menu.png"', content)
new_content = re.sub(pattern2, 'src="images/image_menu.png"', new_content)

if content != new_content:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated menu-photos.html")
else:
    print("No match in menu-photos.html")
