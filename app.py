import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PREMIUM V3 CSS (Animated) ----
st.markdown("""
<style>
body {
    background-color: #edf1f7;
    font-family: 'Segoe UI', sans-serif;
}

/* Header Box */
.header-box {
    background: linear-gradient(135deg, #1d4e89, #0f2557);
    padding: 50px;
    border-radius: 25px;
    margin-bottom: 35px;
    box-shadow: 0px 8px 35px rgba(0,0,0,0.25);
    animation: fadeInDown 1.2s ease-in-out;
}

/* Header Animation */
@keyframes fadeInDown {
  0% { opacity: 0; transform: translateY(-25px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* Flex Layout */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Title */
.header-title {
    font-size: 60px;
    font-weight: 900;
    margin-bottom: 5px;
    color: white;
    animation: fadeIn 1.5s ease-in-out;
}

/* Subtitle */
.header-subtitle {
    font-size: 24px;
    color: #e0e6ee;
    margin-top: 0px;
    animation: fadeIn 1.8s ease-in-out;
}

/* Fade animation */
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

/* Section Title */
.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: #1d3557;
    padding-left: 10px;
    border-left: 7px solid #457b9d;
    animation: slideInLeft 1.2s ease-in-out;
}

/* Slide animation */
@keyframes slideInLeft {
  0% { opacity: 0; transform: translateX(-25px); }
  100% { opacity: 1; transform: translateX(0); }
}

/* Animated Card */
.card {
    background: white;
    padding: 32px;
    border-radius: 22px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
    transition: 0.3s ease-in-out;
    border-left: 7px solid #1d4e89;
    animation: fadeInUp 1s ease-in-out;
}

/* Card animation */
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* Card Hover Animation */
.card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.20);
    border-left: 7px solid #0f2557;
}

/* Nice Bullet Points */
ul li {
    font-size: 18px;
    color: #0f2557;
}

</style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION WITH LOGO ----
logo_path = "Mina Store Logo.png"

st.markdown('<div class="header-box">', unsafe_allow_html=True)
st.markdown('<div class="header-flex">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo_path, width=125)

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
We are a friendly neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We serve the community with a well-selected collection of daily essentials:<br><br>

✔ Gift items 🎁  
✔ Grocery items 🛒  
✔ Hardware tools 🔧  
✔ Xerox & printing 📝  
<br>

Our mission is to deliver <b>quality, convenience, and fair pricing</b> every day.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br><br>
We remain open daily to assist customers in the area.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
