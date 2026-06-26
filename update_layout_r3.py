import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Reviews Header Centering
# We replace the flex row with a flex col centered
old_review_header = 'class="flex flex-col md:flex-row justify-between items-start md:items-end mb-12"'
new_review_header = 'class="flex flex-col items-center justify-center text-center mb-12"'
content = content.replace(old_review_header, new_review_header)

# Center the inner div and eyebrow
old_eyebrow = 'class="text-[10px] md:text-xs text-gray-500 tracking-[0.2em] uppercase font-bold mb-4"'
new_eyebrow = 'class="text-[10px] md:text-xs text-gray-500 tracking-[0.2em] uppercase font-bold mb-4 text-center"'
content = content.replace(old_eyebrow, new_eyebrow)

# The inner div is currently <div> under the flex row container. We want <div class="flex flex-col items-center">
# Let's use regex to find and replace the <div> just before the reviews-eyebrow
content = re.sub(r'<div>(\s*<p data-i18n="reviews-eyebrow")', r'<div class="flex flex-col items-center">\1', content)

# 2. Update Menu Button design
old_menu_btn = 'class="inline-flex items-center gap-2 bg-primary text-white px-8 py-4 rounded-full hover:bg-primary/90 transition-all font-medium group"'
new_menu_btn = 'class="inline-flex items-center gap-2 px-8 py-3 rounded-full border border-primary text-primary font-medium text-sm hover:bg-primary hover:text-white transition-all shadow-lg shadow-primary/30 group"'
content = content.replace(old_menu_btn, new_menu_btn)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Layout updated.")
