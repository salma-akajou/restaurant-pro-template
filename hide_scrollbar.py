import re

filepath = r"c:\Users\Gebruiker\Desktop\restaurant-pro-template\maquettes\about.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

css_to_add = """
        .scrollbar-hide::-webkit-scrollbar {
            display: none;
        }

        .scrollbar-hide {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
"""

if '</style>' in content:
    content = content.replace('</style>', css_to_add + '</style>')
else:
    # If not found, add a new style tag before head ends
    content = content.replace('</head>', '<style>' + css_to_add + '</style>\n</head>')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Added scrollbar-hide CSS")
