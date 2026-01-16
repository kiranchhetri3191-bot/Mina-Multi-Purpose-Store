import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# --------------------------------------------------------
#                PREMIUM GLOBAL CSS
# --------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #eef1f6;
    font-family: 'Segoe UI', sans-serif;
}

/* Section Title */
.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-top: 40px;
    color: #1d3557;
    padding-left: 10px;
    border-left: 6px solid #457b9d;
}

/* Card Design */
.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
    border-left: 7px solid #1d4e89;
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 12px 25px rgba(0,0,0,0.18);
    border-left: 7px solid #0f2557;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------------
#                FLOATING HEADER (WORKING)
# --------------------------------------------------------
logo_path = "Mina Store Logo.png"

st.markdown("""
<div style="
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 40px;
    width: 100%;
">
""", unsafe_allow_html=True)

# ---- LEFT : Floating Logo Box ----
st.markdown("""
<div style="
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.18);
    width: 150px;
    height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: 0.35s;
">
""", unsafe_allow_html=True)

st.image(logo_path, width=120)

st.markdown("</div>", unsafe_allow_html=True)


# ---- RIGHT : Floating Blue Box with Glow ----
st.markdown("""
<style>
.header-float-box {
    background: linear-gradient(135deg, #1d4e89, #0f2557);
    padding: 35px 45px;
    border-radius: 22px;
    width: 72%;
    color: white;
    box-shadow: 0px 10px 35px rgba(0,0,0,0.30);
    transition: 0.35s ease-in-out;
}

/* Hover Glow + Lift */
.header-float-box:hover {
    transform: translateY(-8px);
    box-shadow: 0px 18px 45px rgba(0,0,0,0.40),
                0px 0px 25px rgba(29,78,137,0.70);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-float-box">
    <h1 style="margin: 0; font-size: 48px; font-weight: 800;">
        Mina Multi-Purpose Store
    </h1>
    <h3 style="margin: 0; margin-top: 10px; font-size: 22px; color: #e4e9f0;">
        Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox
    </h3>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)



# --------------------------------------------------------
#                ABOUT US SECTION
# --------------------------------------------------------
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
We are a friendly neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We provide daily-use essentials with a clean and customer-friendly approach:
<br><br>

✔ Gift items 🎁 <br>
✔ Grocery items 🛒 <br>
✔ Hardware tools 🔧 <br>
✔ Xerox & printing 📝 <br><br>

Our mission is simple: <b>Quality, Convenience & Fair Pricing</b>.
</div>
""", unsafe_allow_html=True)



# --------------------------------------------------------
#                STORE TIMINGS
# --------------------------------------------------------
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM <br>
🕖 <b>Closing:</b> 7:00 PM <br><br>
We are open daily for your convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
