import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PROFESSIONAL NEON BLUE DESIGN ----
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* Soft Gradient Background (Professional) */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #e8f0ff, #d4e2ff, #eef3ff);
    z-index: -2;
}

/* HEADER WRAPPER */
.header-box {
    background: #0a1c33;
    padding: 42px 55px;
    border-radius: 26px;
    margin-bottom: 40px;

    /* Soft elegant neon outline */
    border: 1px solid rgba(0, 132, 255, 0.45);
    box-shadow: 0px 0px 14px rgba(0, 132, 255, 0.22);

    animation: fadeDown 0.9s ease;
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
    gap: 38px;
}

/* LOGO — Professional Look (No cartoon glow) */
.header-logo img {
    width: 145px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
}

/* MAIN TITLE — Clean Neon Accent */
.header-title {
    font-size: 54px;
    font-weight: 800;
    color: #e8f4ff;

    /* soft elegant neon edge */
    text-shadow:
        0px 0px 6px rgba(80, 160, 255, 0.35),
        0px 0px 12px rgba(80, 160, 255, 0.28);
}

/* SUBTITLE — Subtle & Professional */
.header-subtitle {
    font-size: 22px;
    font-weight: 400;
    color: #c9d9ea;
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

# ---- ABOUT ----
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

# ---- TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>
We are open every day to serve our customers.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
