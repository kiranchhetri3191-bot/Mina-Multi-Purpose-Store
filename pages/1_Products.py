import streamlit as st
import os

# --------------------------
# FIX IMAGE PATH
# --------------------------
BASE = os.path.dirname(os.path.abspath(__file__))           
IMG_DIR = os.path.abspath(os.path.join(BASE, "..", "images"))  

def load_img(name):
    return os.path.join(IMG_DIR, name)

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------
# CUSTOM CSS for Modern Look
# --------------------------
st.markdown(
    """
    <style>
        /* Title Gradient */
        .title {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(90deg, #ff7a18, #af002d, #319197);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 10px;
            text-align:center;
        }

        /* Product Cards */
        .product-card {
            padding: 18px;
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(8px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            transition: 0.3s ease-in-out;
            text-align:center;
        }

        .product-card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 25px rgba(0,0,0,0.25);
            cursor: pointer;
        }

        .caption {
            font-size: 20px;
            font-weight: 700;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# PAGE TITLE
# --------------------------
st.markdown("<div class='title'>🛍️ Mina Multi-Purpose Store – Product Categories</div>", unsafe_allow_html=True)

st.write("### Explore our categories below:")

# --------------------------
# PRODUCT GRID
# --------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(load_img("gift.png"), use_column_width=True)
    st.markdown("<div class='caption'>Gift Items</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(load_img("grocery.png"), use_column_width=True)
    st.markdown("<div class='caption'>Grocery</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(load_img("hardware.png"), use_column_width=True)
    st.markdown("<div class='caption'>Hardware</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(load_img("print.png"), use_column_width=True)
    st.markdown("<div class='caption'>Print & Xerox</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
