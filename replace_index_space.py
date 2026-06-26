import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'(<!-- ================= SPACES SECTION ================= -->.*?</section>)', content, re.DOTALL)
if match:
    section = match.group(1)
    images_to_use = [
        'images/new_space_1.jpeg', 
        'images/new_space_2.jpeg', 
        'images/new_space_3.jpeg', 
        'images/new_space_4.png'
    ]
    
    def replacer(m):
        if replacer.counter < len(images_to_use):
            new_src = images_to_use[replacer.counter]
            replacer.counter += 1
            return f'src="{new_src}"'
        return m.group(0)
    replacer.counter = 0
    
    new_section = re.sub(r'src=[\'\""]([^\'\""]+)[\'\""]', replacer, section)
    content = content[:match.start()] + new_section + content[match.end():]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced images in index.html")
else:
    print("Spaces section not found in index.html")
