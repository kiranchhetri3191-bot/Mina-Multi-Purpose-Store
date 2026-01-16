import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# --------------------------------------------------------
#                GLOBAL PREMIUM CSS
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
#      PREMIUM HEADER (Working, No Glitch)
# --------------------------------------------------------

logo_path = "Mina Store Logo.png"

st.markdown(f"""
<div style='display: flex; align-items: center; gap: 30px; margin-bottom: 40px;'>

    <!-- LEFT : LOGO FRAME  -->
    <div style="
        background: linear-gradient(135deg, #1d4e89, #0f2557);
        padding: 18px;
        border-radius: 22px;
        height: 150px;
        width: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.20);
    ">
        <div style="
            background: white;
            padding: 12px;
            border-radius: 16px;
            width: 120px;
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
        ">
            <img src='{logo_path}' width='100' style='border-radius:10px;' />
        </div>
    </div>

    <!-- RIGHT : BLUE HEADER BOX -->
    <div style="
        background: linear-gradient(135deg, #1d4e89, #0f2557);
        padding: 32px 45px;
        border-radius: 22px;
        color: white;
        width: 70%;
        box-shadow: 0px 12px 40px rgba(0,0,0,0.28);
    ">
        <h1 style="margin: 0; font-size: 46px; font-weight: 800;">
            Mina Multi-Purpose Store
        </h1>

        <p style="margin: 0; margin-top: 10px; font-size: 20px; color: #dce3eb;">
            Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox
        </p>
    </div>

</div>
""", unsafe_allow_html=True)



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

st.success("✨ Use the sidebar to explore Products & Contact pages!")
