import os
import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add data-i18n to HTML

replacements = [
    (r'<p class="text-\[10px\] text-primary tracking-\[0.2em\] uppercase font-bold mb-6">Notre Histoire</p>',
     r'<p class="text-[10px] text-primary tracking-[0.2em] uppercase font-bold mb-6" data-i18n="about-hero-eyebrow">Notre Histoire</p>'),
    
    (r'<h1 class="font-serif text-4xl md:text-5xl lg:text-6xl text-white mb-6 leading-tight">\s*L\'Art de Vivre,<br>\s*notre signature\.\s*</h1>',
     r'<h1 class="font-serif text-4xl md:text-5xl lg:text-6xl text-white mb-6 leading-tight" data-i18n="about-hero-title">\n                    L\'Art de Vivre,<br>\n                    notre signature.\n                </h1>'),

    (r'<p>\s*Maison Lumière est né d\'un rêve simple : créer un lieu où chaque détail célèbre l\'art de vivre\.\s*</p>',
     r'<p data-i18n="about-hero-desc1">\n                        Maison Lumière est né d\'un rêve simple : créer un lieu où chaque détail célèbre l\'art de vivre.\n                    </p>'),
     
    (r'<p>\s*Inspirée par la gastronomie française et les influences du monde entier, notre cuisine allie\s*tradition et modernité dans une harmonie parfaite\.\s*</p>',
     r'<p data-i18n="about-hero-desc2">\n                        Inspirée par la gastronomie française et les influences du monde entier, notre cuisine allie tradition et modernité dans une harmonie parfaite.\n                    </p>'),
     
    (r'<p>\s*Plus qu\'un restaurant, Maison Lumière est une expérience — un voyage sensoriel où chaque moment\s*devient un souvenir inoubliable\.\s*</p>',
     r'<p data-i18n="about-hero-desc3">\n                        Plus qu\'un restaurant, Maison Lumière est une expérience — un voyage sensoriel où chaque moment devient un souvenir inoubliable.\n                    </p>'),

    (r'<h2 class="font-serif text-4xl md:text-5xl text-white mb-4">L\'Âme de Maison Lumière</h2>',
     r'<h2 class="font-serif text-4xl md:text-5xl text-white mb-4" data-i18n="about-soul-title">L\'Âme de Maison Lumière</h2>'),

    (r'<h2 class="font-serif text-3xl md:text-4xl text-white mb-6">Nous sommes ouverts pour vous\s*accueillir\.</h2>',
     r'<h2 class="font-serif text-3xl md:text-4xl text-white mb-6" data-i18n="about-hours-title">Nous sommes ouverts pour vous accueillir.</h2>'),

    (r'<p class="text-gray-400 font-light text-sm mb-10 leading-relaxed">\s*Pour un déjeuner d\'affaires ou un dîner romantique, nos portes vous sont ouvertes pour vous\s*offrir un moment d\'exception\.\s*</p>',
     r'<p class="text-gray-400 font-light text-sm mb-10 leading-relaxed" data-i18n="about-hours-desc">\n                        Pour un déjeuner d\'affaires ou un dîner romantique, nos portes vous sont ouvertes pour vous offrir un moment d\'exception.\n                    </p>'),

    (r'Réserver une table\s*<i data-lucide="arrow-right"',
     r'<span data-i18n="about-hours-btn">Réserver une table</span>\n                        <i data-lucide="arrow-right"'),

    (r'<p class="text-\[10px\] text-primary tracking-\[0.2em\] uppercase font-bold mb-4">Informations Importantes\s*</p>',
     r'<p class="text-[10px] text-primary tracking-[0.2em] uppercase font-bold mb-4" data-i18n="about-info-eyebrow">Informations Importantes</p>'),
     
    (r'<h2 class="font-serif text-3xl md:text-4xl text-white">Conditions de Vente & Générales</h2>',
     r'<h2 class="font-serif text-3xl md:text-4xl text-white" data-i18n="about-info-title">Conditions de Vente & Générales</h2>'),

    (r'<h3 class="font-serif text-xl text-white mb-3">Conditions de Réservation</h3>',
     r'<h3 class="font-serif text-xl text-white mb-3" data-i18n="about-info-card1-title">Conditions de Réservation</h3>'),

    (r'<p class="text-gray-400 font-light text-sm leading-relaxed">\s*Toute réservation de plus de 6 personnes nécessite une empreinte bancaire\. Annulation gratuite\s*jusqu\'à 24h à l\'avance\.\s*</p>',
     r'<p class="text-gray-400 font-light text-sm leading-relaxed" data-i18n="about-info-card1-desc">\n                        Toute réservation de plus de 6 personnes nécessite une empreinte bancaire. Annulation gratuite jusqu\'à 24h à l\'avance.\n                    </p>'),

    (r'<h3 class="font-serif text-xl text-white mb-3">Conditions de Vente</h3>',
     r'<h3 class="font-serif text-xl text-white mb-3" data-i18n="about-info-card2-title">Conditions de Vente</h3>'),

    (r'<p class="text-gray-400 font-light text-sm leading-relaxed">\s*Nos prix s\'entendent nets, taxes et service compris\. Les menus et millésimes peuvent varier\s*selon les arrivages du marché\.\s*</p>',
     r'<p class="text-gray-400 font-light text-sm leading-relaxed" data-i18n="about-info-card2-desc">\n                        Nos prix s\'entendent nets, taxes et service compris. Les menus et millésimes peuvent varier selon les arrivages du marché.\n                    </p>'),

    (r'<h3 class="font-serif text-xl text-white mb-3">Terms & Conditions</h3>',
     r'<h3 class="font-serif text-xl text-white mb-3" data-i18n="about-info-card3-title">Terms & Conditions</h3>'),

    (r'<p class="text-gray-400 font-light text-sm leading-relaxed">\s*Une tenue correcte est exigée\. La direction se réserve le droit d\'entrée pour préserver\s*l\'atmosphère élégante de l\'établissement\.\s*</p>',
     r'<p class="text-gray-400 font-light text-sm leading-relaxed" data-i18n="about-info-card3-desc">\n                        Une tenue correcte est exigée. La direction se réserve le droit d\'entrée pour préserver l\'atmosphère élégante de l\'établissement.\n                    </p>'),

    (r'<h2 class="font-serif text-3xl md:text-4xl text-white mb-8">Venez nous rendre visite</h2>',
     r'<h2 class="font-serif text-3xl md:text-4xl text-white mb-8" data-i18n="about-loc-title">Venez nous rendre visite</h2>'),

    (r'<h4 class="text-white font-medium mb-1">Adresse</h4>',
     r'<h4 class="text-white font-medium mb-1" data-i18n="about-loc-addr-title">Adresse</h4>'),

    (r'<p class="text-gray-400 font-light text-sm">Avenue Mohammed VI, Hivernage<br>40000 Marrakech, Maroc</p>',
     r'<p class="text-gray-400 font-light text-sm" data-i18n="about-loc-addr-desc">Avenue Mohammed VI, Hivernage<br>40000 Marrakech, Maroc</p>'),

    (r'<h4 class="text-white font-medium mb-1">Téléphone</h4>',
     r'<h4 class="text-white font-medium mb-1" data-i18n="about-loc-phone-title">Téléphone</h4>'),

    (r'<h4 class="text-white font-medium mb-1">Email</h4>',
     r'<h4 class="text-white font-medium mb-1" data-i18n="about-loc-email-title">Email</h4>'),

    (r'Obtenir l\'itinéraire\s*<i data-lucide="navigation"',
     r'<span data-i18n="about-loc-btn">Obtenir l\'itinéraire</span>\n                        <i data-lucide="navigation"')
]

for old, new in replacements:
    content = re.sub(old, new, content)

# 2. Update Translations JS Object

en_keys = """
                "about-hero-eyebrow": "Our History",
                "about-hero-title": "The Art of Living,<br>our signature.",
                "about-hero-desc1": "Maison Lumière was born from a simple dream: to create a place where every detail celebrates the art of living.",
                "about-hero-desc2": "Inspired by French gastronomy and worldwide influences, our cuisine combines tradition and modernity in perfect harmony.",
                "about-hero-desc3": "More than a restaurant, Maison Lumière is an experience — a sensory journey where every moment becomes an unforgettable memory.",
                "about-soul-title": "The Soul of Maison Lumière",
                "about-hours-title": "We are open to welcome you.",
                "about-hours-desc": "For a business lunch or a romantic dinner, our doors are open to offer you an exceptional moment.",
                "about-hours-btn": "Book a table",
                "about-info-eyebrow": "Important Information",
                "about-info-title": "Terms & Conditions of Sale",
                "about-info-card1-title": "Reservation Terms",
                "about-info-card1-desc": "Any reservation for more than 6 people requires a credit card guarantee. Free cancellation up to 24h in advance.",
                "about-info-card2-title": "Sales Terms",
                "about-info-card2-desc": "Our prices are net, taxes and service included. Menus and vintages may vary depending on market arrivals.",
                "about-info-card3-title": "Terms & Conditions",
                "about-info-card3-desc": "Proper attire is required. Management reserves the right of admission to preserve the elegant atmosphere of the establishment.",
                "about-loc-title": "Come visit us",
                "about-loc-addr-title": "Address",
                "about-loc-addr-desc": "Avenue Mohammed VI, Hivernage<br>40000 Marrakech, Morocco",
                "about-loc-phone-title": "Phone",
                "about-loc-email-title": "Email",
                "about-loc-btn": "Get Directions",
"""

fr_keys = """
                "about-hero-eyebrow": "Notre Histoire",
                "about-hero-title": "L'Art de Vivre,<br>notre signature.",
                "about-hero-desc1": "Maison Lumière est né d'un rêve simple : créer un lieu où chaque détail célèbre l'art de vivre.",
                "about-hero-desc2": "Inspirée par la gastronomie française et les influences du monde entier, notre cuisine allie tradition et modernité dans une harmonie parfaite.",
                "about-hero-desc3": "Plus qu'un restaurant, Maison Lumière est une expérience — un voyage sensoriel où chaque moment devient un souvenir inoubliable.",
                "about-soul-title": "L'Âme de Maison Lumière",
                "about-hours-title": "Nous sommes ouverts pour vous accueillir.",
                "about-hours-desc": "Pour un déjeuner d'affaires ou un dîner romantique, nos portes vous sont ouvertes pour vous offrir un moment d'exception.",
                "about-hours-btn": "Réserver une table",
                "about-info-eyebrow": "Informations Importantes",
                "about-info-title": "Conditions de Vente & Générales",
                "about-info-card1-title": "Conditions de Réservation",
                "about-info-card1-desc": "Toute réservation de plus de 6 personnes nécessite une empreinte bancaire. Annulation gratuite jusqu'à 24h à l'avance.",
                "about-info-card2-title": "Conditions de Vente",
                "about-info-card2-desc": "Nos prix s'entendent nets, taxes et service compris. Les menus et millésimes peuvent varier selon les arrivages du marché.",
                "about-info-card3-title": "Terms & Conditions",
                "about-info-card3-desc": "Une tenue correcte est exigée. La direction se réserve le droit d'entrée pour préserver l'atmosphère élégante de l'établissement.",
                "about-loc-title": "Venez nous rendre visite",
                "about-loc-addr-title": "Adresse",
                "about-loc-addr-desc": "Avenue Mohammed VI, Hivernage<br>40000 Marrakech, Maroc",
                "about-loc-phone-title": "Téléphone",
                "about-loc-email-title": "Email",
                "about-loc-btn": "Obtenir l'itinéraire",
"""

# Insert keys into the en: { ... } block
content = re.sub(r'(en:\s*\{)', r'\1' + en_keys, content)
# Insert keys into the fr: { ... } block
content = re.sub(r'(fr:\s*\{)', r'\1' + fr_keys, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("about.html translations updated.")
