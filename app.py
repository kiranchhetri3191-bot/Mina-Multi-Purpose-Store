import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

# --------------------------
# Detect DARK / LIGHT mode
# --------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# Dark / Light Variables
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#e6edf3"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.95)"
    TEXT = "#102a45"


# --------------------------
# CSS Styling
# --------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
}}

/* HEADER BOX */
.header-box {{
    background: #0d2340;
    padding: 42px 55px;
    border-radius: 26px;
    margin-bottom: 40px;
    border: 1px solid rgba(0, 112, 230, 0.55);
    box-shadow: 0px 0px 18px rgba(0, 112, 230, 0.28),
                0px 10px 26px rgba(0,0,0,0.45);
    position: relative;
}}

.header-flex {{
    display: flex;
    align-items: center;
    gap: 38px;
    position: relative;
}}

/* Logo */
.header-logo img {{
    width: 145px;
    border-radius: 14px;
}}

/* BASE FONT */
.header-title, .header-subtitle {{
    font-family: 'Segoe UI', sans-serif;
    font-weight: 800;
    line-height: 1.1;
}}

/* MAIN WHITE NEON LAYER */
.layer-white {{
    position: relative;
    z-index: 3;
    color: white !important;
    text-shadow:
        0px 0px 8px rgba(0, 60, 160, 0.60),
        0px 0px 16px rgba(0, 60, 160, 0.45),
        0px 0px 24px rgba(0, 60, 160, 0.38);
}}

/* BLACK TEXT UNDERLAY (VISIBLE IN LIGHT MODE) */
.layer-black {{
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
    color: black !important;
    opacity: 0.9;
}}

.header-title {{
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 5px;
}}

.header-subtitle {{
    font-size: 22px;
    font-weight: 400;
}}

/* SECTION TITLE */
.section-title {{
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: {TEXT};
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
    color: {TEXT};
}}

</style>
""", unsafe_allow_html=True)

# --------------------------
# HEADER
# --------------------------
st.markdown('<div class="header-box">', unsafe_allow_html=True)
st.markdown('<div class="header-flex">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.markdown('<div class="header-logo">', unsafe_allow_html=True)
    st.image("Mina Store Logo.png", width=145)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="position: relative; height: 110px;">

            <!-- WHITE NEON TEXT -->
            <div class="header-title layer-white">Mina Multi-Purpose Store</div>
            <div class="header-subtitle layer-white">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>

            <!-- BLACK UNDERLAY TEXT (for Light Mode) -->
            <div class="header-title layer-black">Mina Multi-Purpose Store</div>
            <div class="header-subtitle layer-black">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>

        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --------------------------
# ABOUT US
# --------------------------
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.<br><br>

✔ Gift Items 🎁<br>
✔ Grocery Essentials 🛒<br>
✔ Hardware Tools 🔧<br>
✔ Xerox & Printing Services 📝<br><br>

Our mission is to provide <b>quality, convenience, and fair pricing</b> daily.
</div>
""", unsafe_allow_html=True)

# --------------------------
# TIMINGS
# --------------------------
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>
We are open every day to serve our customers.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
