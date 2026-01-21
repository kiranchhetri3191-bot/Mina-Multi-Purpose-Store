import streamlit as st

st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="../Mina Store Logo.png",
    layout="wide"
)

# Detect Dark / Light Mode
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# Theme Colors (same as Home Page)
if is_dark:
    BG = "#0d1117"
    TEXT = "#ffffff"
    NEON = "#00ccff"
else:
    BG = "#f5f7fa"
    TEXT = "#000000"
    NEON = "#0077ff"

# PAGE TITLE (Matches Home Page)
st.markdown(f"""
<div style="text-align:center; padding-top:10px;">
    <img src="../Mina Store Logo.png" width="150">
    <h1 style="color:{NEON}; margin-top:5px;">
        Mina Multi-Purpose Store
    </h1>
    <p style="font-size:20px; color:{TEXT}; margin-top:-10px;">
        Our Product Collections
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)
st.write("")

# Image Style (full width & rounded like banner)
image_style = """
    display:block;
    width:90%;
    margin-left:auto;
    margin-right:auto;
    border-radius:20px;
"""

# ----------- PRODUCT: GIFT ITEMS -----------
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🎁 Gift Items</h2>
<img src="../images/gift.png" style="{image_style}">
<br><br>
""", unsafe_allow_html=True)

# ----------- PRODUCT: GROCERY -----------
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🛍️ Grocery Essentials</h2>
<img src="../images/grocery.png" style="{image_style}">
<br><br>
""", unsafe_allow_html=True)

# ----------- PRODUCT: HARDWARE -----------
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🛠️ Hardware Tools</h2>
<img src="../images/hardware.png" style="{image_style}">
<br><br>
""", unsafe_allow_html=True)

# ----------- PRODUCT: PRINTING SERVICES -----------
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🖨️ Printing & Xerox</h2>
<img src="../images/print.png" style="{image_style}">
<br><br>
""", unsafe_allow_html=True)
