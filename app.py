import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- PREMIUM CSS ----
st.markdown("""
<style>

body {
    background-color: #eef2f7;
    font-family: 'Segoe UI', sans-serif;
}

/* BLUE HEADER BOX ON RIGHT */
.header-box {
    background: linear-gradient(135deg, #1d4e89, #0f2557);
    padding: 28px;
    border-radius: 20px;
    color: white;
    width: 100%;
    box-shadow: 0px 6px 22px rgba(0,0,0,0.25);
}

/* FLEX LAYOUT LEFT LOGO — RIGHT BLUE BOX */
.header-container {
    display: flex;
    align-items: center;
    justify-content: left;
    gap: 25px;
}

/* TITLE WHITE INSIDE BLUE BOX */
.header-title {
    font-size: 50px;
    font-weight: 800;
    margin-bottom: 5px;
    color: white;
}

/* TAGLINE WHITE */
.header-subtitle {
    font-size: 20px;
    margin-top: 0;
    color: white;
}

.card {
    background: white;
    padding: 32px;
    border-radius: 22px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.12);
    border-left: 7px solid #1d4e89;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-top: 50px;
    color: #1d3557;
    padding-left: 8px;
    border-left: 6px solid #457b9d;
}

</style>
""", unsafe_allow_html=True)


# ---- HEADER (NEW LAYOUT: LOGO LEFT + BLUE RIGHT BOX) ----
logo_path = "Mina Store Logo.png"

st.markdown('<div class="header-container">', unsafe_allow_html=True)

# LEFT SIDE LOGO
col1, col2 = st.columns([1, 3])

with col1:
    st.image(logo_path, width=140)

# RIGHT SIDE BLUE BOX WITH TEXT INSIDE
with col2:
    st.markdown("""
        <div class="header-box">
            <div class="header-title">Mina Multi-Purpose Store</div>
            <div class="header-subtitle">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT SECTION ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a friendly neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We provide daily essential products including:<br><br>

✔ Gift items 🎁  
✔ Grocery items 🛒  
✔ Hardware tools 🔧  
✔ Xerox & printing 📝  
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM<br>
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
