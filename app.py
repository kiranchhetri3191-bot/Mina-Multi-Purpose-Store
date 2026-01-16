import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PREMIUM CSS ----
st.markdown("""
<style>
body {
    background-color: #f1f3f5;
    font-family: 'Segoe UI', sans-serif;
}
.header-box {
    background: linear-gradient(90deg, #4b79a1, #283e51);
    padding: 40px;
    border-radius: 20px;
    color: white;
    margin-bottom: 30px;
}
.header-title {
    font-size: 50px;
    font-weight: bold;
}
.header-subtitle {
    font-size: 20px;
    margin-top: 8px;
    color: #ffffff;   /* ✔ FIXED – now subtitle is visible */
    font-weight: 500;
}
.card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
}
.section-title {
    font-size: 32px;
    margin-top: 40px;
    font-weight: bold;
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION WITH WORKING LOGO ----
logo_path = "Mina Store Logo.png"   # Your uploaded logo file

st.markdown('<div class="header-box">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo_path, width=130)   # ✔ Logo appears correctly

with col2:
    st.markdown("""
        <div style="padding-top: 10px;">
            <div class="header-title">Mina Multi-Purpose Store</div>
            <div class="header-subtitle">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT US ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a reliable neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer a complete range of daily-use products including:<br><br>

✔ Gift items  
✔ Grocery items  
✔ Basic hardware tools  
✔ Xerox & printing  
<br>

Our focus is always on <b>fair pricing, convenience, and friendly customer service</b>.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opens:</b> 9:00 AM  
🕖 <b>Closes:</b> 7:00 PM  
<br>
We operate daily for your convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Use the sidebar to explore other pages!")
