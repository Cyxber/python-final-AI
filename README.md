# Python-Programming-Logic
Programming Logic, Fall semester 2026

## Streamlit clothing store (`app.py`)

The Streamlit app recommends a clothing combination based on a shopper's
preferred color and size. It uses the choices in `menu.txt`, asks for a phone
number and delivery address at checkout, and offers a downloadable receipt.
Orders and customer details are not saved to a file or database.

The recommendation matches the selected color and size and uses the first
listed top and graphic from the menu.

### Requirements

- Python 3.10+
- Streamlit (install with `pip install -r requirements.txt`)
- `app.py`, `read_menu.py`, `recommendations.py`, and `menu.txt` in the project
  directory

### Run the Streamlit app locally

```bash
streamlit run app.py
```

### Deploy on Streamlit Community Cloud

Push this repository to GitHub, create a Community Cloud app from the repository,
select the `main` branch, and set the app file to `app.py`. Community Cloud
installs Streamlit from `requirements.txt`.

## Command-line clothing store (`finalproj.py`)

The original command-line order-entry program is retained. It asks for a phone
number, clothing selections, and a delivery address, then saves the order.

Run it from the project directory:

```bash
python3 finalproj.py
```

The menu is read from `menu.txt`, which should contain `TOPS`, `COLORS`,
`GRAPHICS`, and `SIZES` categories with comma-separated choices.

## Test the recommendation logic

```bash
python3 -m unittest discover -s tests
```
