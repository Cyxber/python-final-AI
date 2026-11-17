"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Online Clothing Store
"""

import datetime

from read_menu import read_menu

# Files used by the store
MENU_FILE = "menu.txt"
PHONE_FILE = "phone_number.txt"
DATA_FILE = "order_history.txt"
HUMAN_REPORT = "human_report.txt"

# This is where customer info is recieved
def get_customer_info():
    phone = input("What is your phone number?: ").strip()
    while not phone:
        print("Please enter your phone number.")
        phone = input("What is your phone number?: ").strip()

    with open(PHONE_FILE, "a") as f:
        f.write(f"{phone}\n")
    return phone
# Phone is returned

def get_menu_options(menu_items, category):
# Returns the menu options
    return [
        item.strip().lower()
        for item in menu_items[category].split(",")
        if item.strip()
    ]


def get_choice(prompt, options):
# Displays the menu options
    print(f"Available options: {', '.join(options)}")
    return input(prompt).strip().lower()


def take_order(menu_items):
# Collect and return the customer's clothing selections and address
    order = {
        "top": get_choice(
            "Would you like a T-shirt or hoodie? ",
            get_menu_options(menu_items, "TOPS"),
        ),
        "color": get_choice(
            "What color would you like? ",
            get_menu_options(menu_items, "COLORS"),
        ),
        "graphic": get_choice(
            "Which graphic would you like? ",
            get_menu_options(menu_items, "GRAPHICS"),
        ),
        "size": get_choice(
            "What size would you like? ",
            get_menu_options(menu_items, "SIZES"),
        ),
    }
    address = input("What is your address? ").strip()
    while not address:
        print("Please enter your address.")
        address = input("What is your address? ").strip()
    order["address"] = address
    return order


def save_data_and_label(phone, order):
# Append order history and overwrite with the newest reciept
    with open(DATA_FILE, "a") as f:
        f.write(
            f"{phone},{order['top']},{order['color']},"
            f"{order['graphic']},{order['size']},{order['address']}\n"
        )

    with open(HUMAN_REPORT, "w") as f:
        f.write("CLOTHING STORE ORDER RECEIPT\n")
        f.write(f"Phone Number: {phone}\n")
        f.write(f"Top: {order['top']}\n")
        f.write(f"Color: {order['color']}\n")
        f.write(f"Graphic: {order['graphic']}\n")
        f.write(f"Size: {order['size']}\n")
        f.write(f"Address: {order['address']}\n")


def main():
    menu_items = read_menu()
    if not menu_items:
        return
# ^ Stop only if read_menu.py cannot load menu.txt or the file is empty.

# This section finalizes the order
    phone = get_customer_info()
    order = take_order(menu_items)
    save_data_and_label(phone, order)
    print(f"\nFiles updated: {PHONE_FILE}, {DATA_FILE}, and {HUMAN_REPORT}.")


main()
