import os

directory = r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes'
files = ['index.html', 'menu.html', 'menu-photos.html', 'about.html', 'space.html']

for f in files:
    filepath = os.path.join(directory, f)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace nav logo size
        content = content.replace('class="h-8 md:h-10 w-auto object-contain"', 'class="h-5 md:h-6 w-auto object-contain"')
        
        # Replace footer logo size
        content = content.replace('class="h-10 md:h-12 w-auto object-contain"', 'class="h-6 md:h-8 w-auto object-contain"')
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

print("Logo resizing complete.")
