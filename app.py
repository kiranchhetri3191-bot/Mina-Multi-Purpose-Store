import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PREMIUM COLORFUL CSS ----
st.markdown("""
<style>
body {
    background-color: #eef2f7;
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER BAR */
.header-box {
    background: linear-gradient(135deg, #1d4e89, #0f2557);
    padding: 45px;
    border-radius: 22px;
    margin-bottom: 35px;
    box-shadow: 0px 6px 22px rgba(0,0,0,0.20);
}

/* FLEX FOR HEADER */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* HEADER TITLE */
.header-title {
    font-size: 58px;
    font-weight: 800;
    margin-bottom: 5px;
    color: #ffffff;
}

/* HEADER SUBTITLE */
.header-subtitle {
    font-size: 22px;
    color: #dfe6ee;
    margin-top: 0px;
}

/* SECTION TITLE */
.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-top: 40px;
    color: #1d3557;
    padding-left: 8px;
    border-left: 6px solid #457b9d;
}

/* CARD DESIGN */
.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.12);
    transition: 0.2s ease-in-out;
    border-left: 6px solid #1d4e89;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 10px 28px rgba(0, 0, 0, 0.18);
    border-left: 6px solid #0f2557;
}

/* LIST BULLET COLORS */
ul li {
    color: #0f2557;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION WITH LOGO ----
logo_path = "Mina Store Logo.png"

st.markdown('<div class="header-box">', unsafe_allow_html=True)
st.markdown('<div class="header-flex">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo_path, width=120)

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
We offer daily-use essentials with a customer-friendly approach:<br><br>

✔ Gift items  
✔ Grocery items  
✔ Hardware tools  
✔ Xerox & printing  
<br>

Our goal is to provide quality, convenience, and fair pricing.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opens:</b> 9:00 AM<br>
🕖 <b>Closes:</b> 7:00 PM<br><br>
We operate daily for your convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Use the sidebar to explore Products & Contact pages!")
