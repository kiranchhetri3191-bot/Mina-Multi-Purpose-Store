import streamlit as st
import os

# --------------------------
# FIX IMAGE PATH
# --------------------------
BASE = os.path.dirname(os.path.abspath(__file__))            # pages/
IMG_DIR = os.path.abspath(os.path.join(BASE, "..", "images"))  # images/

def load_img(name):
    return os.path.join(IMG_DIR, name)

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="🛒",
    layout="wide"
)

st.title("🛍️ Our Products")

# --------------------------
# SHOW IMAGES IN 4 COLUMNS
# --------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(load_img("gift.png"), caption="Gift Items", use_column_width=True)

with col2:
    st.image(load_img("grocery.png"), caption="Grocery", use_column_width=True)

with col3:
    st.image(load_img("hardware.png"), caption="Hardware", use_column_width=True)

with col4:
    st.image(load_img("print.png"), caption="Print & Xerox", use_column_width=True)
