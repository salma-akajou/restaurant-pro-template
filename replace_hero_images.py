import re

def update_hero(filepath, old_src_pattern, new_src):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = re.sub(r'src=[\'\""]' + old_src_pattern + r'[\'\""]', f'src="{new_src}"', content)
        
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated hero image in {filepath}")
        else:
            print(f"No match found for {old_src_pattern} in {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# about.html
about_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html"
update_hero(about_path, r"images/restaurant\.jpg", "images/image_about.png")

# menu.html
menu_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\menu.html"
update_hero(menu_path, r"https://images\.unsplash\.com/photo-1414235077428-338989a2e8c0\?auto=format&amp;fit=crop&amp;w=1920&amp;q=80|https://images\.unsplash\.com/photo-1414235077428-338989a2e8c0\?auto=format&fit=crop&w=1920&q=80", "images/image_menu.png")

# Also check menu-photos.html just in case
menu_photos_path = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\menu-photos.html"
update_hero(menu_photos_path, r"https://images\.unsplash\.com/photo-1414235077428-338989a2e8c0\?auto=format&amp;fit=crop&amp;w=1920&amp;q=80|https://images\.unsplash\.com/photo-1414235077428-338989a2e8c0\?auto=format&fit=crop&w=1920&q=80", "images/image_menu.png")
