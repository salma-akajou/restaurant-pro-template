import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\space.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Tailwind
content = re.sub(r'<!-- Tailwind CSS -->\s*<script src="[^"]+"></script>', '<!-- Tailwind CSS -->\n    <script src="https://cdn.tailwindcss.com"></script>', content)

# Fix Lucide Icons
content = re.sub(r'<!-- Lucide Icons -->\s*<script src="[^"]+"></script>', '<!-- Lucide Icons -->\n    <script src="https://unpkg.com/lucide@latest"></script>', content)

# Also fix the translations and main js if they got messed up at the bottom
content = re.sub(r'<script src="[^"]+"></script>\s*</body>', '<script src="js/translations.js"></script>\n    <script src="js/main.js"></script>\n</body>', content)

# Also check for index.html if we did the same thing? 
# Wait, index.html replacement was limited to SPACES SECTION so it should be fine. 
# But space.html we applied to the whole file because there was no section match!

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed scripts in space.html")
