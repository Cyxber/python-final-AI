# Python-Progamming-Logic
Programming Logic, Fall semester 2026

## Online Clothing Store (`finalproj.py`)
# Readme made with AI

`finalproj.py` is a command-line order-entry program for an online clothing
store. It asks for a phone number, clothing selections, and a delivery address,
then saves the order.

### Requirements

- Python 3
- `finalproj.py`, `read_menu.py`, and `menu.txt` in the project directory
- Run the program from the project directory so its output files are written
  there

There are no third-party package dependencies.

### Run

```bash
python3 finalproj.py
```

The menu is loaded from `menu.txt`. It should contain the categories `TOPS`,
`COLORS`, `GRAPHICS`, and `SIZES`, with comma-separated choices after each
category.

### Order flow

1. The program displays the menu loaded by `read_menu.py`.
2. It asks for a phone number, top, color, graphic, size, and address.
3. It appends the phone number to `phone_number.txt` and the order to
   `order_history.txt`.
4. It replaces `human_report.txt` with a receipt for the latest order.

Phone number and address prompts require a non-empty response. The clothing
choices are recorded as entered; they are not checked against the menu.
