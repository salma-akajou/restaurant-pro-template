import os
import re

dir_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes"
files = ["index.html", "about.html", "space.html", "menu.html", "menu-photos.html"]

footer_html = """    <footer class="bg-[#FDF8F3] dark:bg-transparent text-black dark:text-gray-300 pt-16 pb-6 md:pt-24 md:pb-6 transition-colors duration-300 relative z-20">
        <div class="max-w-7xl mx-auto px-8 md:px-16 lg:px-24">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 mb-8">
                <!-- Col 1 -->
                <div class="flex flex-col gap-6">
                    <div>
                        <h2 class="font-serif text-3xl font-bold tracking-wide text-black dark:text-primary">Maison Lumière</h2>
                        <p class="text-[10px] tracking-[0.3em] uppercase text-gray-600 dark:text-gray-500 mt-1">Premium Restaurant</p>
                    </div>
                    <p class="text-sm font-light leading-relaxed max-w-sm" data-i18n="footer-desc">Découvrez une expérience culinaire inoubliable où tradition et modernité se rencontrent pour éveiller vos sens.</p>
                </div>
                <!-- Col 2 -->
                <div class="flex flex-col gap-4">
                    <h3 class="font-serif text-xl text-black dark:text-primary mb-2" data-i18n="footer-hours-title">Horaires</h3>
                    <div class="text-sm font-light space-y-4">
                        <p><strong class="font-medium" data-i18n="footer-services">Services :</strong></p>
                        <p>Lun - Ven: 12h00 - 14h30 | 19h30 - 22h30</p>
                        <p>Sam - Dim: 19h00 - 23h30</p>
                    </div>
                </div>
                <!-- Col 3 -->
                <div class="flex flex-col gap-4">
                    <h3 class="font-serif text-xl text-black dark:text-primary mb-2" data-i18n="footer-contact-title">Contact</h3>
                    <div class="text-sm font-light space-y-4 text-left">
                        <p data-i18n="footer-address">Avenue Mohammed VI, Hivernage, 40000 Marrakech, Maroc</p>
                        <p>+212 600 000 000</p>
                        <p>contact@maisonlumiere.fr</p>
                    </div>
                </div>
            </div>
            <!-- Bottom -->
            <div class="pt-8 border-t border-black/10 dark:border-white/10 flex flex-col md:flex-row justify-between items-center gap-4 text-xs font-light">
                <p data-i18n="footer-rights">&copy; 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin.</p>
                <div class="flex gap-6">
                    <a href="#" class="hover:text-primary transition-colors">Instagram</a>
                    <a href="#" class="hover:text-primary transition-colors">Facebook</a>
                    <a href="#" class="hover:text-primary transition-colors">TripAdvisor</a>
                </div>
            </div>
        </div>
    </footer>"""

en_keys = """
                "footer-desc": "Discover an unforgettable culinary experience where tradition and modernity meet to awaken your senses.",
                "footer-hours-title": "Opening Hours",
                "footer-services": "Services:",
                "footer-contact-title": "Contact",
                "footer-address": "Avenue Mohammed VI, Hivernage, 40000 Marrakech, Morocco",
                "footer-rights": "© 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin.",
"""
fr_keys = """
                "footer-desc": "Découvrez une expérience culinaire inoubliable où tradition et modernité se rencontrent pour éveiller vos sens.",
                "footer-hours-title": "Horaires",
                "footer-services": "Services :",
                "footer-contact-title": "Contact",
                "footer-address": "Avenue Mohammed VI, Hivernage, 40000 Marrakech, Maroc",
                "footer-rights": "© 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin.",
"""

about_js = """
        /* =================== TRANSLATIONS =================== */
        const translations = {
            en: {
                "nav-home": "Home",
                "nav-about": "About",
                "nav-space": "Space",
                "nav-menu": "Menu",
                "nav-reservation": "Reservation",
                "lang-indicator": "FR",
                "footer-desc": "Discover an unforgettable culinary experience where tradition and modernity meet to awaken your senses.",
                "footer-hours-title": "Opening Hours",
                "footer-services": "Services:",
                "footer-contact-title": "Contact",
                "footer-address": "Avenue Mohammed VI, Hivernage, 40000 Marrakech, Morocco",
                "footer-rights": "© 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin."
            },
            fr: {
                "nav-home": "Accueil",
                "nav-about": "À propos",
                "nav-space": "Espace",
                "nav-menu": "Menu",
                "nav-reservation": "Réservation",
                "lang-indicator": "EN",
                "footer-desc": "Découvrez une expérience culinaire inoubliable où tradition et modernité se rencontrent pour éveiller vos sens.",
                "footer-hours-title": "Horaires",
                "footer-services": "Services :",
                "footer-contact-title": "Contact",
                "footer-address": "Avenue Mohammed VI, Hivernage, 40000 Marrakech, Maroc",
                "footer-rights": "© 2026 Premium Restaurant Agency. All rights reserved. Made by Akajou Twin."
            }
        };

        let currentLang = localStorage.getItem('preferred-lang') || 'fr';

        document.addEventListener('DOMContentLoaded', () => {
            updateTexts();
        });

        function updateTexts() {
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[currentLang] && translations[currentLang][key]) {
                    el.innerHTML = translations[currentLang][key];
                }
            });

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

for filename in files:
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace Footer
    content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL | re.IGNORECASE)
    
    if filename == "about.html":
        # 2. Add Translations Script to about.html
        if "function toggleLanguage" not in content:
            content = content.replace("</script>\n</body>", about_js + "\n    </script>\n</body>")
    else:
        # 3. Add Footer keys to other files
        if '"footer-desc"' not in content:
            # find 'en: {' and add keys
            content = re.sub(r'(en:\s*\{)', r'\1' + en_keys, content)
            # find 'fr: {' and add keys
            content = re.sub(r'(fr:\s*\{)', r'\1' + fr_keys, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Translations fixed in all pages.")
