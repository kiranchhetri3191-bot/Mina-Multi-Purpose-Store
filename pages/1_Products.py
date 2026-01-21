import streamlit as st

st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# ---------------------------------------------------
# Detect Dark / Light Mode
# ---------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# ---------------------------------------------------
# Auto Colors
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    SUBTEXT = "#d0d0d0"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT = "#0a0a0a"
    SUBTEXT = "#303030"

NEON_BLUE = "#00c6ff"
NEON_GLOW = "0px 0px 12px rgba(0,198,255,0.7)"

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
}}

.header-title {{
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 10px;
    color: {NEON_BLUE};
    text-shadow: {NEON_GLOW};
}}

.header-subtitle {{
    font-size: 18px;
    text-align: center;
    margin-bottom: 35px;
    color: {TEXT};
}}

.product-card {{
    background: {CARD_BG};
    padding: 22px;
    border-radius: 20px;
    border: 2px solid {NEON_BLUE};
    box-shadow: {NEON_GLOW};
    transition: 0.25s ease-in-out;
    text-align: center;
    margin-bottom: 25px;
}}

.product-card:hover {{
    transform: translateY(-6px);
    box-shadow: 0px 0px 20px rgba(0,198,255,0.9);
}}

.product-img {{
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 14px;
    border: 2px solid {NEON_BLUE};
    background: rgba(0,0,0,0.1);
    box-shadow: {NEON_GLOW};
}}

.product-name {{
    margin-top: 14px;
    font-size: 24px;
    font-weight: 700;
    color: {NEON_BLUE};
    text-shadow: {NEON_GLOW};
}}

.product-desc {{
    margin-top: 6px;
    font-size: 16px;
    color: {SUBTEXT};
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------
st.markdown("<div class='header-title'>Our Products</div>", unsafe_allow_html=True)
st.markdown("<div class='header-subtitle'>Explore all available categories at Mina Multi-Purpose Store</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# PRODUCT LIST  (Correct image paths)
# ---------------------------------------------------
products = [
    {
        "name": "Gift Items",
        "desc": "Decorations, soft toys, greeting cards, keychains & more.",
        "img": "images/gift.png"
    },
    {
        "name": "Grocery Essentials",
        "desc": "Rice, oil, biscuits, spices, pulses & daily items.",
        "img": "images/grocery.png"
    },
    {
        "name": "Hardware Tools",
        "desc": "Tape, hammer, screwdrivers, cutters & repair tools.",
        "img": "images/hardware.png"
    },
    {
        "name": "Printing & Xerox",
        "desc": "Xerox, printing, lamination & online form fill-up.",
        "img": "images/print.png"
    }
]

# ---------------------------------------------------
# PRODUCT GRID
# ---------------------------------------------------
cols = st.columns(2)

for i, p in enumerate(products):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="product-card">
            <img src="{p['img']}" class="product-img">
            <div class="product-name">{p['name']}</div>
            <div class="product-desc">{p['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
