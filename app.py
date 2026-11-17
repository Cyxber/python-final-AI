from datetime import datetime

import streamlit as st

from read_menu import read_menu
from store_menu import menu_options


st.set_page_config(page_title="Online Clothing Store", layout="centered")
st.title("Online Clothing Store")
st.write("Choose items from the menu, then download a receipt for your order.")

menu_items = read_menu()
categories = ("TOPS", "COLORS", "GRAPHICS", "SIZES")
options = {category: menu_options(menu_items, category) for category in categories}
missing_categories = [category for category, items in options.items() if not items]

if missing_categories:
    st.error(
        "The menu is missing valid options for: "
        + ", ".join(missing_categories)
        + ". Update menu.txt and restart the app."
    )
    st.stop()

st.subheader("Choose your clothing")
top_column, color_column = st.columns(2)
with top_column:
    top = st.selectbox("Top", options["TOPS"])
with color_column:
    color = st.selectbox("Color", options["COLORS"])
graphic_column, size_column = st.columns(2)
with graphic_column:
    graphic = st.selectbox("Graphic", options["GRAPHICS"])
with size_column:
    size = st.selectbox("Size", options["SIZES"])

st.subheader("Order summary")
summary_columns = st.columns(4)
summary_columns[0].metric("Top", top)
summary_columns[1].metric("Color", color)
summary_columns[2].metric("Graphic", graphic)
summary_columns[3].metric("Size", size)

st.subheader("Checkout")
with st.form("checkout_form"):
    phone = st.text_input("Phone number")
    address = st.text_area("Delivery address")
    submitted = st.form_submit_button("Place order")

if submitted:
    if not phone.strip() or not address.strip():
        st.error("Enter both a phone number and a delivery address.")
    else:
        receipt = "\n".join(
            (
                "CLOTHING STORE ORDER RECEIPT",
                f"Date: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
                f"Phone Number: {phone.strip()}",
                f"Top: {top}",
                f"Color: {color}",
                f"Graphic: {graphic}",
                f"Size: {size}",
                f"Address: {address.strip()}",
                "",
            )
        )
        st.success("Your order is ready. Download the receipt below.")
        st.download_button(
            "Download receipt",
            data=receipt,
            file_name="clothing_store_receipt.txt",
            mime="text/plain",
        )
        st.caption(
            "This demo does not save orders to a file or database. "
            "Streamlit holds the receipt data in memory while you are connected."
        )
