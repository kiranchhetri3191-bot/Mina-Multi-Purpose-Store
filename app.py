import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

# ================================
#        DARK + LIGHT MODE CSS
# ================================
st.markdown("""
<style>

/* THEME VARIABLES */
:root {
    --bg-color: var(--background-color);
    --text-color: var(--text-color);
    --primary-color: var(--primary-color);
    --secondary-bg: rgba(255, 255, 255, 0.95);
    --card-border: rgba(0, 112, 230, 0.55);
}

/* DARK MODE OVERRIDES */
[data-theme="dark"] {
    --bg-color: #0d1117;
    --text-color: #e6edf3;
    --secondary-bg: rgba(22, 27, 34, 0.85);
    --card-border: rgba(0, 132, 255, 0.55);
}

/* Background */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: var(--bg-color);
    z-index: -2;
}

/* HEADER */
.header-box {
    background: #0d2340;
    padding: 42px 55px;
    border-radius: 26px;
    margin-bottom: 40px;
    border: 1px solid var(--card-border);
    box-shadow: 
        0px 0px 18px rgba(0, 112, 230, 0.28),
        0px 10px 26px rgba(0,0,0,0.45);
    animation: fadeDown 0.9s ease;
}

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
        0px 4px 14px rgba(0,0,0,0.45),
        0px 0px 12px rgba(80,150,255,0.25);
}

/* Titles */
.header-title {
    font-size: 40px;
    font-weight: 800;
    color: #ffffff;
    text-shadow:
        0px 0px 8px rgba(0, 60, 160, 0.60),
        0px 0px 16px rgba(0, 60, 160, 0.45),
        0px 0px 24px rgba(0, 60, 160, 0.38);
}

.header-subtitle {
    font-size: 20px;
    font-weight: 400;
    color: #ffffff;
    text-shadow:
        0px 0px 6px rgba(0, 60, 160, 0.60),
        0px 0px 14px rgba(0, 60, 160, 0.45),
        0px 0px 20px rgba(0, 60, 160, 0.35);
}

/* Section Title */
.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: var(--text-color);
    padding-left: 12px;
    border-left: 6px solid var(--primary-color);
}

/* CARD */
.card {
    background: var(--secondary-bg);
    padding: 28px;
    border-radius: 20px;
    border-left: 6px solid var(--primary-color);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.10);
    transition: 0.2s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0px 12px 26px rgba(0,0,0,0.18);
}

/* Animation */
@keyframes fadeDown {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)


# ================================
#            HEADER
# ================================
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
            <div class="header-subtitle">
                Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ================================
#            ABOUT US
# ================================
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


# ================================
#             TIMINGS
# ================================
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>

We are open every day to serve our customers.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
