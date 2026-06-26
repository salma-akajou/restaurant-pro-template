import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# The user wants to replace section 2 (which is the one with L'âme de Maison Lumière)
sections = re.split(r'(<section.*?</section>)', content, flags=re.DOTALL)

# Let's find the section that contains "L'me de Maison Lumire" or "L'âme de Maison Lumière"
target_idx = -1
for i, sec in enumerate(sections):
    if "L\\'âme de Maison Lumière" in sec or "L\\'me de Maison Lumire" in sec or 'data-i18n="about-soul-title"' in sec:
        target_idx = i
        break

if target_idx != -1:
    print(f"Found target section at index {target_idx}")
else:
    print("Could not find target section")
