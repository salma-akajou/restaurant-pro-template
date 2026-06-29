import os
import re

directory = r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes'
files = ['index.html', 'menu.html', 'menu-photos.html', 'about.html', 'space.html']

nav_logo_pattern = re.compile(r'<a href="index\.html"[^>]*>\s*DON PEPE\s*</a>', re.IGNORECASE)
footer_logo_pattern = re.compile(r'<h2[^>]*>\s*DON PEPE\s*</h2>', re.IGNORECASE)

nav_replacement = r'''<a href="index.html" class="shrink-0 flex items-center">
          <img src="images/logo.png" alt="DON PEPE Logo" class="h-8 md:h-10 w-auto object-contain">
        </a>'''

footer_replacement = r'''<h2 class="font-serif text-3xl font-bold tracking-wide text-black dark:text-primary mb-2 flex items-center gap-2">
              <img src="images/logo.png" alt="DON PEPE Logo" class="h-10 md:h-12 w-auto object-contain">
            </h2>'''

for f in files:
    filepath = os.path.join(directory, f)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = nav_logo_pattern.sub(nav_replacement, content)
        content = footer_logo_pattern.sub(footer_replacement, content)

        if f == 'index.html':
            content = content.replace(
                '<div class="flex justify-center md:absolute md:right-0 md:bottom-0 gap-4 mt-8 md:mt-0">',
                '<div class="flex justify-end md:absolute md:right-0 md:bottom-0 gap-4 mt-8 md:mt-0">'
            )
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

print("Replacement complete.")
