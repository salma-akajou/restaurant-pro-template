import re
content = open(r'c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html', encoding='utf-8').read()

print('--- REVIEWS SECTION ---')
match = re.search(r'<!-- ================= REVIEWS SECTION ================= -->.*?(<section.*?</section>)', content, re.DOTALL)
if match:
    print(match.group(1)[:1000])

print('\n--- ABOUT BUTTON ---')
about_match = re.search(r'(<a href="about\.html"[^>]*>.*?En savoir plus.*?</a>)', content, re.DOTALL)
if about_match:
    print(about_match.group(1))

print('\n--- MENU BUTTON ---')
menu_match = re.search(r'(<a href="menu\.html"[^>]*>.*?Découvrir le Menu Complet.*?</a>)', content, re.DOTALL)
if menu_match:
    print(menu_match.group(1))
