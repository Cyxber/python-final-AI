"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. PHASE 1: External menu.txt file created in workspace.
[X] 3. Program reads and parses the .txt file into a Dictionary.
[X] 4. PHASE 2: break the dictionary into individual variables.
[X] 6. Print each category and its details
[] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

from pathlib import Path

MENU_FILE = Path(__file__).with_name("menu.txt")

# Read_menu is defined
def read_menu():
    menus = {}
    try:
        with open(MENU_FILE, "r") as f:
            for line in f:
                print(line.strip())
                if not line.strip():
                    continue
                category, detail = line.strip().split(":", 1)
                menus[category.strip()] = detail.strip()
        return menus
    except FileNotFoundError:
        print('Please create the file or check the file name. It should be "menu.txt"')
        return {}
# Split into variables to pass each category separately
def split_into_variables(menu_items):
    tops = menu_items.get("TOPS")
    colors = menu_items.get("COLORS")
    graphics = menu_items.get("GRAPHICS")
    sizes = menu_items.get("SIZES")
    return tops, colors, graphics, sizes

#Print the menu for the user to see
def print_menu(tops, colors, graphics, sizes):
    print("Menu\n")
    print("Tops:")
    tops_item = tops.split(',')
    for item in tops_item:
        print(f"\t{item.strip()}")

    print("\nColors:")
    colors_item = colors.split(',')
    for item in colors_item:
        print(f"\t{item.strip()}")

    print("\nGraphics:")
    graphics_item = graphics.split(',')
    for item in graphics_item:
        print(f"\t{item.strip()}")

    print("\nSizes:")
    sizes_item = sizes.split(',')
    for item in sizes_item:
        print(f"\t{item.strip()}")

# Main is defined 
def main():
    menu_items = read_menu()
    if menu_items == {}:
        return
    tops, colors, graphics, sizes = split_into_variables(menu_items)
    print_menu(tops, colors, graphics, sizes)


if __name__ == "__main__":
    read_menu()