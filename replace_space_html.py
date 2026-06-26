import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\space.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

images_to_use = [
    'images/new_space_1.jpeg', 
    'images/new_space_2.jpeg', 
    'images/new_space_3.jpeg', 
    'images/new_space_4.png',
    'images/new_space_5.png',
    'images/new_space_6.png'
]

def replacer(m):
    src = m.group(1)
    if 'glovo' in src.lower():
        return m.group(0) # Keep glovo
    
    # Otherwise replace it
    new_src = images_to_use[replacer.counter % len(images_to_use)]
    replacer.counter += 1
    return f'src="{new_src}"'
replacer.counter = 0

new_content = re.sub(r'src=[\'\""]([^\'\""]+)[\'\""]', replacer, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Replaced images in space.html")
