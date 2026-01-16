
import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="🛍️", layout="wide")

# ---- PREMIUM CSS ----
st.markdown("""
<style>
body {
    background-color: #f1f3f5;
    font-family: 'Segoe UI', sans-serif;
}
.header-box {
    background: linear-gradient(90deg, #4b79a1, #283e51);
    padding: 60px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}
.header-title {
    font-size: 55px;
    font-weight: bold;
}
.header-subtitle {
    font-size: 22px;
    margin-top: 10px;
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

# ---- HEADER SECTION ----
st.markdown("""
<div class="header-box">
    <div class="header-title">🛍️ Mina Multi-Purpose Store</div>
    <div class="header-subtitle">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
</div>
""", unsafe_allow_html=True)

# ---- ABOUT US ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a reliable local store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer a complete range of daily-use products including:
<br><br>
✔ Gift items  
✔ Grocery items  
✔ Basic hardware tools  
✔ Xerox & printing  
<br>
Our focus is on <b>fair pricing, convenience, and friendly service</b>.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opens:</b> 9:00 AM  
🕖 <b>Closes:</b> 7:00 PM  
<br>
We are open daily for customer convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Use the sidebar to explore other pages!")
