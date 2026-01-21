import streamlit as st

st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# ---------------------------------------------------
# Detect DARK / LIGHT Mode
# ---------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# ---------------------------------------------------
# Colors
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
else:
    BG = "#ffffff"
    CARD_BG = "#f4f4f4"
    TEXT = "#000000"

# ---------------------------------------------------
# Page Title
# ---------------------------------------------------
st.markdown(
    f"""
    <h1 style='text-align:center; color:{TEXT};'>
        🛒 Our Products
    </h1>
    <p style='text-align:center; color:{TEXT}; font-size:18px;'>
        Explore all available categories at Mina Multi-Purpose Store
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Product Data (Correct Image Paths!)
# ---------------------------------------------------
products = [
    {
        "name": "Gift Items",
        "image": "../images/gift.png",
        "desc": "Decorations, soft toys, greeting cards, keychains & more."
    },
    {
        "name": "Grocery Essentials",
        "image": "../images/grocery.png",
        "desc": "Rice, oil, biscuits, spices, pulses & daily items."
    },
    {
        "name": "Hardware Tools",
        "image": "../images/hardware.png",
        "desc": "Tools, nails, locks, wires, screwdrivers & more."
    },
    {
        "name": "Printing Services",
        "image": "../images/print.png",
        "desc": "Color print, Xerox, ID photo, lamination & more."
    }
]

# ---------------------------------------------------
# Display Grid
# ---------------------------------------------------
cols = st.columns(2)

for i, product in enumerate(products):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div style="
                background:{CARD_BG};
                padding:20px;
                border-radius:15px;
                margin-bottom:25px;
                text-align:center;
                box-shadow:0px 0px 15px rgba(0,0,0,0.1);
            ">
                <img src="{product['image']}" width="180" 
                style="border-radius:12px; border:2px solid #00ccff;">
                <h2 style="color:{TEXT}; margin-top:15px;">{product['name']}</h2>
                <p style="color:{TEXT};">{product['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
