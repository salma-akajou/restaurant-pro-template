import os
import re
import json

dir_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes"
files = ["index.html", "about.html", "space.html", "menu.html", "menu-photos.html"]

merged_en = {}
merged_fr = {}

for filename in files:
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract the JS translations object
    match = re.search(r'const translations\s*=\s*(\{.*?\});\s*(let currentLang|function)', html, re.DOTALL)
    if match:
        obj_str = match.group(1)
        
        # This is a bit hacky, but we can try to find en: { ... } and fr: { ... }
        en_match = re.search(r'en:\s*\{(.*?)\}\s*,\s*fr:', obj_str, re.DOTALL)
        fr_match = re.search(r'fr:\s*\{(.*?)\}\s*\}', obj_str, re.DOTALL)
        
        if en_match:
            en_str = en_match.group(1)
            # Find all "key": "value" pairs
            pairs = re.findall(r'"([^"]+)"\s*:\s*"((?:[^"\\]|\\.)*)"', en_str)
            for k, v in pairs:
                merged_en[k] = v
        
        if fr_match:
            fr_str = fr_match.group(1)
            pairs = re.findall(r'"([^"]+)"\s*:\s*"((?:[^"\\]|\\.)*)"', fr_str)
            for k, v in pairs:
                merged_fr[k] = v

# Add translations for the footer (since they are new/untranslated in about.html)
new_footer_en = {
    "footer-desc": "Discover an unforgettable culinary experience where tradition and modernity meet to awaken your senses.",
    "footer-hours-title": "Opening Hours",
    "footer-services": "Services:",
    "footer-contact-title": "Contact",
    "footer-address": "Avenue Mohammed VI, Hivernage, 40000 Marrakech, Morocco",
    "footer-rights": "© 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin."
}
new_footer_fr = {
    "footer-desc": "Découvrez une expérience culinaire inoubliable où tradition et modernité se rencontrent pour éveiller vos sens.",
    "footer-hours-title": "Horaires",
    "footer-services": "Services :",
    "footer-contact-title": "Contact",
    "footer-address": "Avenue Mohammed VI, Hivernage, 40000 Marrakech, Maroc",
    "footer-rights": "© 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin."
}

merged_en.update(new_footer_en)
merged_fr.update(new_footer_fr)

# Ensure nav translations are complete
nav_en = {
    "nav-home": "Home",
    "nav-about": "About",
    "nav-space": "Space",
    "nav-menu": "Menu",
    "nav-reservation": "Reservation",
    "lang-indicator": "FR"
}
nav_fr = {
    "nav-home": "Accueil",
    "nav-about": "À propos",
    "nav-space": "Espace",
    "nav-menu": "Menu",
    "nav-reservation": "Réservation",
    "lang-indicator": "EN"
}
merged_en.update(nav_en)
merged_fr.update(nav_fr)

# Generate translations.js
js_content = """const translations = {
    en: """ + json.dumps(merged_en, indent=4, ensure_ascii=False) + """,
    fr: """ + json.dumps(merged_fr, indent=4, ensure_ascii=False) + """
};

let currentLang = localStorage.getItem('preferred-lang') || 'fr';

document.addEventListener('DOMContentLoaded', () => {
    updateTexts();
});

function updateTexts() {
    // Update normal texts
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[currentLang] && translations[currentLang][key]) {
            el.innerHTML = translations[currentLang][key];
        }
    });

    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[currentLang] && translations[currentLang][key]) {
            el.placeholder = translations[currentLang][key];
        }
    });

    // Update indicator
    const langInd = document.getElementById('lang-indicator');
    if (langInd && translations[currentLang]["lang-indicator"]) {
        langInd.innerText = translations[currentLang]["lang-indicator"];
    }
}

function toggleLanguage() {
    currentLang = currentLang === 'en' ? 'fr' : 'en';
    localStorage.setItem('preferred-lang', currentLang);
    updateTexts();
}
"""

js_dir = os.path.join(dir_path, "js")
os.makedirs(js_dir, exist_ok=True)
with open(os.path.join(js_dir, "translations.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated translations.js with {len(merged_en)} EN keys and {len(merged_fr)} FR keys.")
