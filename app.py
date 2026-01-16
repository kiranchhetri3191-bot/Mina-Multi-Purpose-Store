import streamlit as st

st.set_page_config(
    page_title="Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# ------------------ CLEAN & PROFESSIONAL CSS ------------------
st.markdown("""
<style>
body {
    background: #f2f4f7; 
    font-family: 'Segoe UI', sans-serif;
}

/* elegant header */
.header-box {
    background: linear-gradient(120deg, #1a73e8, #0b3f89);
    padding: 28px;
    border-radius: 14px;
    margin-bottom: 30px;
    color: white;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

/* logo */
.header-logo {
    width: 70px;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
}

/* title */
.header-title {
    font-size: 32px;
    font-weight: 700;
    margin: 0;
}

.header-subtitle {
    font-size: 15px;
    margin-top: 2px;
    opacity: 0.95;
}

/* content card */
.card {
    background: white;
    padding: 24px;
    border-radius: 14px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.10);
    margin-bottom: 20px;
}

/* section headings */
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #102033;
    margin-bottom: 10px;
}

/* list styling */
.card ul {
    margin-left: 20px;
}
.card li {
    margin: 6px 0;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
logo_path = "Mina Store Logo.png"

st.markdown('<div class="header-box">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo_path, width=70)

with col2:
    st.markdown("""
        <p class="header-title">Mina Multi-Purpose Store</p>
        <p class="header-subtitle">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------ ABOUT US ------------------
st.markdown('<p class="section-title">About Us</p>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer daily-use essentials with a customer-friendly approach:

<ul>
  <li>🎁 Gift items</li>
  <li>🛒 Grocery items</li>
  <li>🔧 Hardware tools</li>
  <li>📝 Xerox & printing</li>
</ul>

Our goal is to provide <b>quality, convenience, and fair pricing</b>.
</div>
""", unsafe_allow_html=True)

# ------------------ STORE TIMINGS ------------------
st.markdown('<p class="section-title">Store Timings</p>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
<b>🕘 Opens:</b> 9:00 AM<br>
<b>🕖 Closes:</b> 7:00 PM<br><br>
Open daily.
</div>
""", unsafe_allow_html=True)

st.success("✔ Use the sidebar to navigate other pages.")
