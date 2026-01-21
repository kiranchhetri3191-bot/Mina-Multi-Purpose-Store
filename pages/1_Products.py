import streamlit as st

st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="../Mina Store Logo.png",
    layout="wide"
)

# Detect Dark / Light Mode
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

TEXT = "#ffffff" if is_dark else "#000000"

# Page Title
st.markdown(f"""
<h1 style='text-align:center; color:{TEXT};'>
    🛒 Our Products
</h1>
<p style='text-align:center; color:{TEXT}; font-size:18px;'>
    Explore all the categories at Mina Multi-Purpose Store
</p>
""", unsafe_allow_html=True)

st.write("")

# ---------- IMAGE STYLE (BIG LOGO STYLE) ----------
image_style = """
    display:block;
    margin-left:auto;
    margin-right:auto;
    width:80%;
    border-radius:20px;
"""

# ---------- SHOW 4 IMAGES (BIG SIZE LIKE LOGO) ----------
st.markdown(f"""
<h2 style='text-align:center; color:{TEXT};'>Gift Items</h2>
<img src="../images/gift.png" style="{image_style}">
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(f"""
<h2 style='text-align:center; color:{TEXT};'>Grocery Essentials</h2>
<img src="../images/grocery.png" style="{image_style}">
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(f"""
<h2 style='text-align:center; color:{TEXT};'>Hardware Tools</h2>
<img src="../images/hardware.png" style="{image_style}">
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(f"""
<h2 style='text-align:center; color:{TEXT};'>Printing Services</h2>
<img src="../images/print.png" style="{image_style}">
""", unsafe_allow_html=True)
