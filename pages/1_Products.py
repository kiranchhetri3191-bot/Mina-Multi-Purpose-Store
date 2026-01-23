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
    page_title="Products - Mina Store",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------
# RESPONSIVE CSS
# --------------------------
st.markdown("""
<style>

/* Gradient Title */
.title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff7a18, #af002d, #319197);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 25px;
}

/* Grid Container */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 22px;
    padding: 10px;
}

/* Card Design */
.product-card {
    padding: 15px;
    border-radius: 18px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(7px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    transition: 0.3s;
    text-align: center;
}

.product-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

/* Caption */
.caption {
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
}

/* Mobile Responsiveness */
@media (max-width: 480px) {
    .title {
        font-size: 30px;
    }
    .product-card {
        padding: 12px;
        border-radius: 14px;
    }
    .caption {
        font-size: 16px;
    }
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# PAGE TITLE
# --------------------------
st.markdown("<div class='title'>🛍️ Mina Multi-Purpose Store</div>", unsafe_allow_html=True)
st.write("### Browse Categories:")

# --------------------------
# PRODUCT GRID RESPONSIVE
# --------------------------
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

categories = [
    ("gift.png", "Gift Items"),
    ("grocery.png", "Grocery"),
    ("hardware.png", "Hardware"),
    ("print.png", "Print & Xerox"),
]

for img, caption in categories:
    # OPEN CARD
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)

    # LOAD IMAGE SAFELY
    st.image(load_img(img), use_column_width=True)

    # CAPTION
    st.markdown(f"<div class='caption'>{caption}</div>", unsafe_allow_html=True)

    # CLOSE CARD
    st.markdown("</div>", unsafe_allow_html=True)

# CLOSE GRID
st.markdown("</div>", unsafe_allow_html=True)
