import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

# ---------------------------------------------------
# Detect DARK / LIGHT Mode
# ---------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# ---------------------------------------------------
# Colors
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT_MAIN = "#ffffff"
    TEXT_SECOND = "#e6edf3"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT_MAIN = "#0a0a0a"
    TEXT_SECOND = "#102a45"

# ---------------------------------------------------
# CSS FIX — UPDATED WITH NEON GRADIENT
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
}}

.header-box {{
    background: #0d2340;
    padding: 42px 55px;
    border-radius: 26px;
    margin-bottom: 40px;
    border: 1px solid rgba(0, 112, 230, 0.55);
    box-shadow: 0px 0px 18px rgba(0, 112, 230, 0.28),
                0px 10px 26px rgba(0,0,0,0.45);
}}

.header-flex {{
    display: flex;
    align-items: center;
    gap: 38px;
}}

.header-logo img {{
    width: 145px;
    border-radius: 14px;
}}

/* 🌟 NEON GRADIENT TITLE + SUBTITLE */
.header-title, .header-subtitle {{
    background: linear-gradient(90deg, #ffff00, #ff8c00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    text-shadow: 0px 0px 12px rgba(255,200,0,0.55),
                 0px 0px 18px rgba(255,150,0,0.55);
}}

.header-title {{
    font-size: 40px;
}}

.header-subtitle {{
    font-size: 20px;
    font-weight: 600;
}}

/* SECTION TITLES */
.section-title {{
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: {TEXT_MAIN};
    padding-left: 12px;
    border-left: 6px solid #007bff;
}}

/* CARD */
.card {{
    background: {CARD_BG};
    padding: 28px;
    border-radius: 20px;
    border-left: 6px solid #0a4ba6;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.10);
    font-size: 18px;
    line-height: 1.55;
    color: {TEXT_MAIN};
}}

.card * {{
    color: {TEXT_MAIN} !important;
}}

.card a {{
    color: #58a6ff !important;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown('<div class="header-box">', unsafe_allow_html=True)
st.markdown('<div class="header-flex">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.markdown('<div class="header-logo">', unsafe_allow_html=True)
    st.image("Mina Store Logo.png", width=145)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div>
            <div class="header-title">Mina Multi-Purpose Store</div>
            <div class="header-subtitle">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# ABOUT US
# ---------------------------------------------------
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.<br><br>

✔ Gift Items 🎁<br>
✔ Grocery Essentials 🛒<br>
✔ Hardware Tools 🔧<br>
✔ Xerox & Printing Services 📝<br><br>

Our mission is to provide <b>quality, convenience, and fair pricing</b> every day.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TIMINGS
# ---------------------------------------------------
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>

We are open every day to serve our customers.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
