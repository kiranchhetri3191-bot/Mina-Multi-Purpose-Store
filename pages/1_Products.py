import streamlit as st

st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="../Mina Store Logo.png",
    layout="wide"
)

# Detect Dark / Light Mode
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# Auto Colors
if is_dark:
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
else:
    CARD_BG = "#f4f4f4"
    TEXT = "#000000"


# Page Heading
st.markdown(f"""
<h1 style='text-align:center; color:{TEXT};'>
    🛍️ Our Products
</h1>
<p style='text-align:center; color:{TEXT}; font-size:18px;'>
    Explore all available categories at Mina Multi-Purpose Store
</p>
""", unsafe_allow_html=True)


# PRODUCT LIST (Fixed image paths)
products = [
    {
        "name": "Gift Items",
        "img": "../images/gift.png",
        "desc": "Decorations, soft toys, greeting cards, keychains & more."
    },
    {
        "name": "Grocery Essentials",
        "img": "../images/grocery.png",
        "desc": "Rice, oil, biscuits, spices, pulses & daily items."
    },
    {
        "name": "Hardware Tools",
        "img": "../images/hardware.png",
        "desc": "Tools, nails, locks, wires, screwdrivers & more."
    },
    {
        "name": "Printing Services",
        "img": "../images/print.png",
        "desc": "Color print, Xerox, ID photo, lamination & more."
    }
]


# DISPLAY IN GRID FORMAT
cols = st.columns(2)

for i, product in enumerate(products):
    col = cols[i % 2]
    with col:
        st.markdown(
            f"""
            <div style="
                background:{CARD_BG};
                padding:20px;
                border-radius:20px;
                margin:20px;
                text-align:center;
                box-shadow:0px 0px 10px rgba(0,0,0,0.15);
            ">
                <img src="{product['img']}" width="150" style="border-radius:10px;">
                <h2 style="color:{TEXT}; margin-top:10px;">{product['name']}</h2>
                <p style="color:{TEXT};">{product['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
