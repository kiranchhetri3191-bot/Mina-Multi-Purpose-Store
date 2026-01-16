import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- NEON BLUE GLOW PRO CSS ----
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* Soft animated gradient background */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at 20% 20%, #dbe6ff, #c7d4ff, #e7eeff);
    z-index: -2;
    animation: bgShift 10s infinite alternate ease-in-out;
}
@keyframes bgShift {
    0% { opacity: 0.8; }
    100% { opacity: 1; }
}

/* HEADER BOX */
.header-box {
    background: #00152e;
    padding: 45px 55px;
    border-radius: 28px;
    margin-bottom: 40px;
    position: relative;
    box-shadow: 0 0 25px rgba(0, 146, 255, 0.35);
    animation: fadeDown 1s ease;
}

/* Outer neon glow */
.header-box::after {
    content: "";
    position: absolute;
    inset: -5px;
    border-radius: 32px;
    background: linear-gradient(135deg, #008cff, #00b6ff, #0090ff);
    filter: blur(22px);
    z-index: -1;
    opacity: 0.6;
}

/* Fade animation */
@keyframes fadeDown {
    0% { opacity: 0; transform: translateY(-25px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* FLEX - Logo + Title */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 38px;
}

/* Logo */
.header-logo img {
    border-radius: 16px;
    width: 150px;
    box-shadow: 0px 0px 18px rgba(0, 162, 255, 0.55);
}

/* MAIN TITLE with NEON GLOW */
.header-title {
    font-size: 60px;
    font-weight: 900;
    color: #dff2ff;
    letter-spacing: 1px;
    text-shadow:
        0 0 8px #00aaff,
        0 0 12px #0099ff,
        0 0 18px #0099ff,
        0 0 25px #00c8ff;
}

/* SUBTITLE */
.header-subtitle {
    font-size: 22px;
    font-weight: 400;
    margin-top: 8px;
    color: #c6e4ff;
    text-shadow: 0 0 10px rgba(0, 136, 255, 0.35);
}

/* Section Title */
.section-title {
    font-size: 38px;
    font-weight: 700;
    color: #0f2a45;
    padding-left: 12px;
    border-left: 7px solid #0094ff;
    margin-top: 40px;
}

/* Card */
.card {
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(6px);
    padding: 30px;
    border-radius: 22px;
    border-left: 7px solid #0074d4;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 14px 35px rgba(0, 140, 255, 0.28);
    border-left: 7px solid #004c99;
}

</style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION ----
logo_path = "Mina Store Logo.png"

st.markdown('<div class="header-box">', unsafe_allow_html=True)
st.markdown('<div class="header-flex">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.markdown('<div class="header-logo">', unsafe_allow_html=True)
    st.image(logo_path, width=150)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div>
            <div class="header-title">Mina Multi-Purpose Store</div>
            <div class="header-subtitle">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT US ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a trusted neighborhood retail store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer a carefully selected collection of daily-use products:<br><br>

✔ Gift Items 🎁<br>
✔ Grocery Essentials 🛒<br>
✔ Hardware Tools 🔧<br>
✔ Xerox & Printing Services 📝<br><br>

Our promise is to deliver <b>quality, convenience, and fair pricing</b> every single day.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>
We remain open all days to serve the local community.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
