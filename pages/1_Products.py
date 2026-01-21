import streamlit as st
import os

# -------------------------------------------------------
# FIX IMAGE PATHS (ALWAYS WORKS IN STREAMLIT)
# -------------------------------------------------------
BASE = os.path.dirname(os.path.abspath(__file__))     # pages folder
IMG_DIR = os.path.abspath(os.path.join(BASE, "..", "images"))

def img(path):
    return f"file:///{os.path.join(IMG_DIR, path).replace('\\', '/')}"


# -------------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------------
st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="../Mina Store Logo.png",
    layout="wide"
)

# -------------------------------------------------------
# Detect Dark / Light Mode
# -------------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

if is_dark:
    BG = "#0d1117"
    TEXT = "#ffffff"
    NEON = "#00ccff"
else:
    BG = "#f5f7fa"
    TEXT = "#000000"
    NEON = "#0077ff"


# -------------------------------------------------------
# PAGE HEADER (Matches Your Home Theme)
# -------------------------------------------------------
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

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# -------------------------------------------------------
# IMAGE STYLE
# -------------------------------------------------------
image_style = """
    display:block;
    width:90%;
    margin-left:auto;
    margin-right:auto;
    border-radius:20px;
    margin-top:15px;
"""


# -------------------------------------------------------
# PRODUCT IMAGES SECTION
# -------------------------------------------------------

# Gift Items
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🎁 Gift Items</h2>
<img src="{img("gift.png")}" style="{image_style}">
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Grocery
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🛍️ Grocery Essentials</h2>
<img src="{img("grocery.png")}" style="{image_style}">
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Hardware
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🛠️ Hardware Tools</h2>
<img src="{img("hardware.png")}" style="{image_style}">
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Printing
st.markdown(f"""
<h2 style="text-align:center; color:{NEON};">🖨️ Printing & Xerox</h2>
<img src="{img("print.png")}" style="{image_style}">
""", unsafe_allow_html=True)

