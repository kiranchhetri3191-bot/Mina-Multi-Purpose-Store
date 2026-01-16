import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- EVEN DARKER PREMIUM HEADER DESIGN ----
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* Soft Background */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #dce3f7, #c8d4f0, #e6ecff);
    z-index: -2;
}

/* HEADER WRAPPER – DARKER, DEEP SHADE */
.header-box {
    background: rgba(3, 8, 20, 0.90);   /* even darker navy */
    backdrop-filter: blur(14px);
    padding: 45px 58px;
    border-radius: 26px;
    margin-bottom: 40px;

    border: 1px solid rgba(0, 98, 210, 0.55); /* darker neon edge */
    box-shadow:
        0px 0px 22px rgba(0, 98, 210, 0.28),
        0px 12px 30px rgba(0,0,0,0.55);       /* deeper shadow */

    animation: fadeDown 0.9s ease;
}

@keyframes fadeDown {
    0% { opacity: 0; transform: translateY(-22px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* FLEX */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 38px;
}

/* LOGO */
.header-logo img {
    width: 145px;
    border-radius: 14px;
    box-shadow: 
        0px 4px 14px rgba(0,0,0,0.55),
        0px 0px 12px rgba(70,130,255,0.25);
}

/* MAIN TITLE — Brighter & stronger visibility */
.header-title {
    font-size: 54px;
    font-weight: 800;
    color: #f6f9ff;   /* brighter white */

    text-shadow:
        0px 0px 8px rgba(120, 180, 255, 0.55),
        0px 0px 18px rgba(80, 150, 255, 0.35);
}

/* SUBTITLE — slightly darkened for match */
.header-subtitle {
    font-size: 22px;
    font-weight: 400;
    color: #d0dcee;
    margin-top: 8px;
}

/* SECTION TITLE */
.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: #102a45;
    padding-left: 12px;
    border-left: 6px solid #007bff;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.95);
    padding: 28px;
    border-radius: 20px;
    border-left: 6px solid #0a4ba6;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.10);
    transition: 0.2s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0px 12px 26px rgba(0,0,0,0.18);
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
    st.image(logo_path, width=145)
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

# ---- ABOUT SECTION ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.
We offer a curated selection of essential everyday products:<br><br>

✔ Gift Items 🎁<br>
✔ Grocery Essentials 🛒<br>
✔ Hardware Tools 🔧<br>
✔ Xerox & Printing Services 📝<br><br>

Our mission is to provide <b>quality, convenience, and fair pricing</b> daily.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>
We are open every day to serve our customers.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
