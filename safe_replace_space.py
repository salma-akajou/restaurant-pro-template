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
    original_tag = m.group(0)
    src_val = m.group(1)
    
    # Don't replace glovo logo
    if 'glovo' in src_val.lower():
        return original_tag
    
    # Otherwise replace it
    new_src = images_to_use[replacer.counter % len(images_to_use)]
    replacer.counter += 1
    
    # Reconstruct the tag with the new src
    return original_tag.replace(src_val, new_src)

replacer.counter = 0

# Match ONLY <img ... src="..." ...>
new_content = re.sub(r'<img[^>]+src=[\'\""]([^\'\""]+)[\'\""][^>]*>', replacer, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Replaced only images in space.html")
