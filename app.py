import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- DARK PREMIUM GLASSMORPHIC DESIGN ----
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* Smooth Background */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #081526, #0c1f38, #122a45);
    background-size: 300% 300%;
    animation: bgShift 14s infinite alternate ease-in-out;
    z-index: -2;
}

@keyframes bgShift {
    0% { background-position: 0% 0%; }
    100% { background-position: 80% 100%; }
}

/* HEADER BOX - Glass + Glow */
.header-box {
    background: rgba(15, 30, 55, 0.55);
    backdrop-filter: blur(14px);
    padding: 45px 58px;
    border-radius: 26px;
    margin-bottom: 45px;

    border: 1px solid rgba(130, 180, 255, 0.18);
    box-shadow: 0px 12px 28px rgba(0,0,0,0.35),
                0px 0px 22px rgba(90, 150, 255, 0.18);

    animation: fadeDown 1.1s ease;
}

@keyframes fadeDown {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* FLEX */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 42px;
}

/* LOGO */
.header-logo img {
    width: 150px;
    border-radius: 16px;
    box-shadow:
        0px 4px 10px rgba(0,0,0,0.45),
        0px 0px 18px rgba(110, 170, 255, 0.22);
}

/* MAIN TITLE */
.header-title {
    font-size: 56px;
    font-weight: 800;
    color: #eaf3ff;
    letter-spacing: 0.8px;

    text-shadow: 
        0px 0px 6px rgba(140, 185, 255, 0.25),
        0px 0px 16px rgba(110, 160, 255, 0.18);
}

/* SUBTITLE */
.header-subtitle {
    font-size: 22px;
    color: #ccdaeb;
    margin-top: 6px;
    font-weight: 400;
}

/* SECTION TITLE */
.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: #d9e7f7;
    padding-left: 12px;
    border-left: 6px solid #4fa3ff;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(12px);
    padding: 28px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.18);

    box-shadow: 
        0px 6px 20px rgba(0,0,0,0.35),
        inset 0px 0px 18px rgba(255,255,255,0.05);

    color: #e1e9f5;
    transition: 0.2s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 
        0px 10px 26px rgba(0,0,0,0.45),
        inset 0px 0px 18px rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
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
We offer a curated collection of everyday essentials:<br><br>

✔ Gift Items 🎁<br>
✔ Grocery Essentials 🛒<br>
✔ Hardware Tools 🔧<br>
✔ Xerox & Printing Services 📝<br><br>

Our mission is to offer <b>quality, convenience, and reliable service</b> every day.
</div>
""", unsafe_allow_html=True)

# ---- TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>
We stay open all days to serve our valued customers.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
