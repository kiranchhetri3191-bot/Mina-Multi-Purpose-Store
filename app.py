import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PREMIUM CSS (MODERN UI) ----
st.markdown("""
<style>
body {
    background-color: #eef1f5;
    font-family: 'Segoe UI', sans-serif;
}

/* Elegant header container */
.hero-section {
    background: linear-gradient(135deg, #3358f4, #051d3f);
    padding: 40px 20px;
    border-radius: 18px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

/* Logo styling */
.logo-style {
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

/* Title text */
.big-title {
    font-size: 56px;
    font-weight: bold;
    margin-top: 10px;
}

/* Tagline text */
.tagline {
    font-size: 22px;
    color: #f2f2f2;
    margin-top: -10px;
}

/* Main cards */
.card {
    background: white;
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.10);
    margin-bottom: 25px;
}

/* Section headers */
.section-title {
    font-size: 32px;
    font-weight: bold;
    color: #1c2a3a;
}
</style>
""", unsafe_allow_html=True)

# ---- HERO HEADER WITH LOGO ----
logo_path = "Mina Store Logo.png"

st.markdown('<div class="hero-section">', unsafe_allow_html=True)

st.image(logo_path, width=140, output_format="PNG", use_column_width=False)

st.markdown("""
<div class="big-title">Mina Multi-Purpose Store</div>
<div class="tagline">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT US ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer a wide range of everyday essential items at fair and affordable prices:<br><br>

✔ Gift items  
✔ Grocery items  
✔ Basic hardware tools  
✔ Xerox & printing services  
<br>

Our mission is to offer <b>quality products, great convenience, and friendly service</b> to everyone.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opens:</b> 9:00 AM<br>
🕖 <b>Closes:</b> 7:00 PM<br><br>
We are open every day for customer convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Use the sidebar to explore more!")
