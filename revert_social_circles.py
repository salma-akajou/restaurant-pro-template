import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Revert the social media links class
new_link = 'class="text-white/50 hover:text-white transition-colors"'
old_link = 'class="w-10 h-10 rounded-full bg-primary flex items-center justify-center text-white hover:bg-primary/90 hover:scale-110 transition-all shadow-md"'

content = content.replace(old_link, new_link)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Reverted Social Icons styles back to original.")
