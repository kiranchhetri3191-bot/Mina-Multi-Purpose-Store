import streamlit as st

st.set_page_config(page_title="Products - Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

# ---------------------------------------------------
# Detect DARK / LIGHT Mode
# ---------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# ---------------------------------------------------
# Auto Colors for Both Modes
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT = "#0a0a0a"

# ---------------------------------------------------
# CSS (LED Header + Neon Section Titles + Neon Cards)
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
    color: {TEXT} !important;
}}

@keyframes led-color-shift {{
    0%   {{ color: #ff0000; text-shadow: 0 0 12px #ff0000; }}
    20%  {{ color: #ff9900; text-shadow: 0 0 14px #ff9900; }}
    40%  {{ color: #ffff00; text-shadow: 0 0 18px #ffff00; }}
    60%  {{ color: #00ff00; text-shadow: 0 0 14px #00ff00; }}
    80%  {{ color: #00ccff; text-shadow: 0 0 18px #00ccff; }}
    100% {{ color: #ff00ff; text-shadow: 0 0 18px #ff00ff; }}
}}

@keyframes led-pulse {{
    0%   {{ opacity: 0.75; transform: scale(1); }}
    50%  {{ opacity: 1;    transform: scale(1.05); }}
    100% {{ opacity: 0.75; transform: scale(1); }}
}}

.header-title {{
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 10px;
    animation: led-color-shift 3s infinite linear, led-pulse 2s infinite ease-in-out;
}}

.header-subtitle {{
    font-size: 18px;
    text-align: center;
    margin-bottom: 35px;
    animation: led-color-shift 4s infinite linear, led-pulse 3s infinite ease-in-out;
}}

.section-title {{
    font-size: 32px;
    font-weight: 700;
    margin-top: 20px;
    padding-left: 12px;
    color: {TEXT};
    border-left: 6px solid #007bff;
    text-shadow: 0 0 8px rgba(0,123,255,0.55);
}}

.product-card {{
    background: {CARD_BG};
    padding: 20px;
    border-radius: 18px;
    border-left: 5px solid #0a4ba6;
    box-shadow: 0px 6px 20px rgba(0, 100, 255, 0.25);
    margin-bottom: 18px;
}}

.product-img {{
    width: 120px;
    border-radius: 12px;
    margin-bottom: 10px;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------
st.markdown("<div class='header-title'>Our Products</div>", unsafe_allow_html=True)
st.markdown("<div class='header-subtitle'>Explore All Categories Available at Mina Multi-Purpose Store</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# UPDATED PRODUCT LIST WITH YOUR REAL FILE NAMES
# ---------------------------------------------------
products = [
    {
        "name": "Gift Items",
        "desc": "Gift toys, greeting cards & simple gift items.",
        "img": "gift item.png"
    },
    {
        "name": "Hardware Tools",
        "desc": "Bulbs, tools, tapes & repair items.",
        "img": "hardware item.png"
    },
    {
        "name": "Printing & Xerox",
        "desc": "Xerox, printout, lamination & form fill-up.",
        "img": "Xerox item.png"
    },
    {
        "name": "Snacks",
        "desc": "Cakes, biscuits, chocolate & snacks.",
        "img": "Snaks.png"
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
            <h3>{p['name']}</h3>
            <p>{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
