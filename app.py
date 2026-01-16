import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

# --------------------------------------------------------
#                GLOBAL CSS
# --------------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #eef1f6;
    font-family: 'Segoe UI', sans-serif;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-top: 40px;
    color: #1d3557;
    padding-left: 10px;
    border-left: 6px solid #457b9d;
}

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
#           FLOATING HEADER WITH WORKING LOGO
# --------------------------------------------------------
left, right = st.columns([1, 4])

# ---------------- LEFT: LOGO CARD (fixed) ----------------
with left:
    st.markdown("""
        <div style="
            background: white;
            padding: 15px;
            border-radius: 18px;
            height: 150px;
            width: 150px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
            margin-bottom: 10px;
        ">
        """, unsafe_allow_html=True)

    st.image("Mina Store Logo.png", width=120)   # 100% working fix

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RIGHT: FLOATING BLUE HEADER BOX ----------------
with right:
    st.markdown("""
    <style>
    .header-final-box {
        background: linear-gradient(135deg, #1d4e89, #0f2557);
        padding: 32px 45px;
        border-radius: 22px;
        color: white;
        box-shadow: 0px 10px 35px rgba(0,0,0,0.28);
        transition: 0.3s ease-in-out;
        width: 100%;
    }
    .header-final-box:hover {
        transform: translateY(-5px);
        box-shadow: 0px 14px 45px rgba(0,0,0,0.35);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header-final-box">
        <h1 style="margin: 0; font-size: 46px; font-weight: 800;">
            Mina Multi-Purpose Store
        </h1>
        <h3 style="margin: 0; margin-top: 10px; font-size: 20px; color: #e4e9f0;">
            Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox
        </h3>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------------
#                ABOUT US SECTION
# --------------------------------------------------------
st.markdown("<div class='section-title'>About Us</div>",
            unsafe_allow_html=True)

st.markdown("""
<div class="card">
We are a friendly neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.
We provide daily-use essentials including:
<br><br>

✔ Gift items 🎁 <br>
✔ Grocery items 🛒 <br>
✔ Hardware tools 🔧 <br>
✔ Xerox & printing 📝 <br><br>

Our mission is simple: <b>Quality, Convenience & Fair Pricing</b>.
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------------
#                STORE TIMINGS SECTION
# --------------------------------------------------------
st.markdown("<div class='section-title'>Store Timings</div>",
            unsafe_allow_html=True)

st.markdown("""
<div class="card">
🕘 <b>Opening:</b> 9:00 AM <br>
🕖 <b>Closing:</b> 7:00 PM <br><br>

We are open daily for your convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore Products & Contact pages using the sidebar!")
