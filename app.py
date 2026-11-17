from datetime import datetime

import streamlit as st

from read_menu import read_menu
from recommendations import menu_options, recommend_outfit


st.set_page_config(page_title="Online Clothing Store", layout="centered")
st.title("Online Clothing Store")
st.write("Find a clothing match, then download a receipt for your order.")

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

st.subheader("Your preferences")
color_column, size_column = st.columns(2)
with color_column:
    preferred_color = st.selectbox("Preferred color", options["COLORS"])
with size_column:
    preferred_size = st.selectbox("Size", options["SIZES"])

recommendation = recommend_outfit(menu_items, preferred_color, preferred_size)
if recommendation is None:
    st.error("No matching clothing option is available for those preferences.")
    st.stop()

st.subheader("Recommended match")
top_column, color_column, graphic_column, size_column = st.columns(4)
top_column.metric("Top", recommendation["top"])
color_column.metric("Color", recommendation["color"])
graphic_column.metric("Graphic", recommendation["graphic"])
size_column.metric("Size", recommendation["size"])
st.caption(
    "The menu only contains category options, so this suggestion matches your "
    "selected color and size and uses the first listed top and graphic."
)

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
                f"Top: {recommendation['top']}",
                f"Color: {recommendation['color']}",
                f"Graphic: {recommendation['graphic']}",
                f"Size: {recommendation['size']}",
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
