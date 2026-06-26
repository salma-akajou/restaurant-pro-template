import os
import glob
import re

directory = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes"
extensions = ["*.html", "js/*.js"]

files_to_process = []
for ext in extensions:
    files_to_process.extend(glob.glob(os.path.join(directory, ext)))

replaced_count = 0

for filepath in files_to_process:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We need to replace "Maison Lumière" with "DON PEPE"
        # Since 'Lumière' might be escaped or case-varied, let's use a case-insensitive regex
        new_content = re.sub(r'Maison Lumière', 'DON PEPE', content, flags=re.IGNORECASE)
        
        # What if it's L'âme de Maison Lumière ? Wait, we should just replace "Maison Lumière"
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
            replaced_count += 1
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Total files updated: {replaced_count}")
