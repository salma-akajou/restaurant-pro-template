import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Current HTML structure around top header row
# <!-- Top header row -->
# <div class="flex flex-col items-center justify-center text-center mb-12">
#     <div class="flex flex-col items-center">
# ...
#     <!-- Navigation Buttons -->
#     <div class="flex gap-4 mt-8 md:mt-0 flex-shrink-0">

new_structure = """<!-- Top header row -->
            <div class="relative mb-12">
                <div class="flex flex-col items-center text-center">
                    <p data-i18n="reviews-eyebrow"
                        class="text-primary font-medium tracking-widest text-sm uppercase mb-3">CE QU'ILS
                        EN
                        DISENT</p>
                    <div class="flex flex-col gap-1">
                        <h2 class="font-serif text-4xl md:text-5xl lg:text-5xl font-bold mb-4">4.9 sur Google.</h2>
                        <div class="w-24 h-[1px] bg-primary/30 mx-auto"></div>
                    </div>
                </div>

                <!-- Navigation Buttons -->
                <div class="flex justify-center md:absolute md:right-0 md:bottom-0 gap-4 mt-8 md:mt-0">"""

# Replace the block from <!-- Top header row --> to <!-- Navigation Buttons --> + <div class="...">
match = re.search(r'<!-- Top header row -->.*?<!-- Navigation Buttons -->\s*<div class="[^"]*">', content, re.DOTALL)
if match:
    content = content[:match.start()] + new_structure + content[match.end():]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Reviews scroll buttons moved to the right.")
else:
    print("Could not find the target block.")
