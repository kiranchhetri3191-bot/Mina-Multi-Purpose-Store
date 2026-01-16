import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PREMIUM PRO CSS ----
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* Soft Animated Background */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #dce8ff, #c7d4f0, #e9f0ff);
    animation: bgShift 12s infinite alternate ease-in-out;
    z-index: -2;
}

@keyframes bgShift {
    0% { background-position: 0% 0%; }
    100% { background-position: 80% 100%; }
}

/* HEADER BOX */
.header-box {
    background: linear-gradient(135deg, #123d73, #0a1f42);
    padding: 40px 55px;
    border-radius: 30px;
    margin-bottom: 40px;
    box-shadow: 0px 10px 35px rgba(0,0,0,0.25);
    animation: fadeDown 1s ease;
    border: 2px solid rgba(255,255,255,0.1);
    position: relative;
}

/* Glow Border */
.header-box::after {
    content: "";
    position: absolute;
    inset: -3px;
    border-radius: 35px;
    background: linear-gradient(135deg, #4fa3ff, #103e77);
    z-index: -1;
    filter: blur(18px);
    opacity: 0.55;
}

@keyframes fadeDown {
  0% { opacity: 0; transform: translateY(-25px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* FLEX */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 35px;
}

/* Logo */
.header-logo img {
    border-radius: 14px;
    box-shadow: 0px 8px 18px rgba(0,0,0,0.35);
}

/* MAIN TITLE */
.header-title {
    font-size: 58px;
    font-weight: 900;
    line-height: 1.15;
    color: white;
}

/* SUBTITLE */
.header-subtitle {
    font-size: 22px;
    color: #cfd7e6;
    margin-top: 6px;
    font-weight: 400;
}

/* Section Title */
.section-title {
    font-size: 38px;
    font-weight: 700;
    margin-top: 40px;
    color: #102a43;
    padding-left: 12px;
    border-left: 7px solid #376ba6;
}

/* Card */
.card {
    background: rgba(255,255,255,0.90);
    backdrop-filter: blur(6px);
    padding: 30px;
    border-radius: 22px;
    border-left: 7px solid #123d73;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 14px 35px rgba(0,0,0,0.20);
    border-left: 7px solid #0a1f42;
}

/* List */
ul li {
    font-size: 18px;
    color: #0f2557;
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
    st.image(logo_path, width=135)
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
