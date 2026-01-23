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
# DARK/LIGHT TOGGLE
# --------------------------
mode = st.sidebar.radio("Theme Mode", ["Light", "Dark"], index=0)

if mode == "Dark":
    bg_color = "#0A0F24"
    card_bg = "rgba(255, 255, 255, 0.12)"
else:
    bg_color = "#F5F7FA"
    card_bg = "rgba(255, 255, 255, 0.65)"

# --------------------------
# CUSTOM CSS (Neon + Responsive + Modern)
# --------------------------
st.markdown(f"""
<style>

body {{
    background-color: {bg_color} !important;
}}

.main {{
    background-color: {bg_color} !important;
}}

/* NEON BLUE TITLE */
.title {{
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 25px;
    color: #00C8FF !important;
    text-shadow: 0 0 10px #00C8FF, 0 0 20px #0099CC, 0 0 30px #00C8FF;
}}

/* SUBTITLE */
.subtitle {{
    font-size: 22px;
    color: #00E1FF;
    text-align:center;
    margin-bottom: 10px;
    text-shadow: 0 0 5px #00D4FF;
}}

/* RESPONSIVE GRID */
.grid-container {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 22px;
    padding: 10px;
}}

/* PRODUCT CARDS */
.product-card {{
    padding: 15px;
    border-radius: 18px;
    background: {card_bg};
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    transition: 0.3s;
    text-align: center;
}}

.product-card:hover {{
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0, 200, 255, 0.4);
    border-color: #00C8FF;
}}

/* CAPTION */
.caption {{
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
    color: #00E1FF;
    text-shadow: 0 0 6px #00C8FF;
}}

/* SMALLER ON MOBILE */
@media (max-width: 480px) {{
    .title {{
        font-size: 32px;
    }}
    .product-card {{
        padding: 12px;
    }}
    .caption {{
        font-size: 16px;
    }}
}}

</style>
""", unsafe_allow_html=True)

# --------------------------
# TITLE
# --------------------------
st.markdown("<div class='title'>🛍️ Mina Multi-Purpose Store</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore our top categories</div>", unsafe_allow_html=True)

# --------------------------
# PRODUCT GRID
# --------------------------
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

categories = [
    ("gift.png", "Gift Items"),
    ("grocery.png", "Grocery"),
    ("hardware.png", "Hardware"),
    ("print.png", "Print & Xerox"),
]

for img, caption in categories:
    st.markdown(f"""
        <div class='product-card'>
            <img src="app://local/{load_img(img)}" style="width:100%; border-radius:12px;" />
            <div class='caption'>{caption}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
