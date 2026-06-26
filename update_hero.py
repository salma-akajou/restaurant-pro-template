import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Buttons Size
btn1_old = 'px-8 py-3.5 rounded-full bg-primary text-white border border-transparent hover:bg-transparent hover:border-[#FDF8F3] hover:text-[#FDF8F3] font-semibold text-sm'
btn1_new = 'px-6 py-2.5 md:px-8 md:py-3.5 rounded-full bg-primary text-white border border-transparent hover:bg-transparent hover:border-[#FDF8F3] hover:text-[#FDF8F3] font-semibold text-xs md:text-sm'
content = content.replace(btn1_old, btn1_new)

btn2_old = 'px-8 py-3.5 rounded-full bg-black/20 backdrop-blur-sm border border-white/40 text-white font-medium text-sm'
btn2_new = 'px-6 py-2.5 md:px-8 md:py-3.5 rounded-full bg-black/20 backdrop-blur-sm border border-white/40 text-white font-medium text-xs md:text-sm'
content = content.replace(btn2_old, btn2_new)

# 2. Title Font size
title_old = 'text-3xl md:text-[4.5rem] text-white mb-6 drop-shadow-2xl leading-[1.1]'
title_new = 'text-3xl md:text-[6rem] text-white mb-6 drop-shadow-2xl leading-[1.1]'
content = content.replace(title_old, title_new)

# 3. Social Icons
social_old = 'class="absolute left-6 md:left-12 top-1/2 -translate-y-1/2 flex flex-col items-center gap-6 z-20"'
social_new = 'class="fixed bottom-6 md:bottom-10 left-1/2 -translate-x-1/2 flex flex-row items-center gap-6 z-50"'
content = content.replace(social_old, social_new)

# also change the vertical line to horizontal line
line_old = '<div class="w-px h-16 bg-white/30 mt-2"></div>'
line_new = '<div class="hidden md:block w-16 h-px bg-white/30 ml-2"></div>'
content = content.replace(line_old, line_new)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Hero section layout.")
