import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Revert to vertical flex-col but fixed at the bottom left
social_old = 'class="fixed bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex flex-row items-center gap-6 z-50"'
social_new = 'class="fixed bottom-6 md:bottom-10 left-6 md:left-12 flex flex-col items-center gap-6 z-50"'
content = content.replace(social_old, social_new)

# Revert the horizontal line back to vertical
line_old = '<div class="hidden md:block w-16 h-px bg-white/30 ml-2"></div>'
line_new = '<div class="w-px h-16 bg-white/30 mt-2"></div>'
content = content.replace(line_old, line_new)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Social Icons to vertical fixed at bottom left.")
