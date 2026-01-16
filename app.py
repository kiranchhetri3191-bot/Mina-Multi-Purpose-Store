# ---- PREMIUM V5 FLOATING GLOW HEADER ----
logo_path = "Mina Store Logo.png"

# Header Wrapper
st.markdown("""
<div style="
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 40px;
">
""", unsafe_allow_html=True)

# LEFT — Floating Logo Box
st.markdown("""
<div style="
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.18);
    display: flex;
    align-items: center;
    justify-content: center;
    width: 150px;
    height: 150px;
    transition: 0.35s ease-in-out;
">
""", unsafe_allow_html=True)

st.image(logo_path, width=120)

st.markdown("</div>", unsafe_allow_html=True)

# RIGHT — Floating Blue Box WITH Glow & Hover Rise
st.markdown("""
<style>
.header-float-box {
    background: linear-gradient(135deg, #1d4e89, #0f2557);
    padding: 35px 45px;
    border-radius: 22px;
    width: 70%;
    color: white;
    text-align: left;
    box-shadow: 0px 10px 35px rgba(0,0,0,0.30);
    transition: 0.35s ease-in-out;
}

/* Hover Glow + Lift */
.header-float-box:hover {
    transform: translateY(-8px);
    box-shadow: 0px 18px 45px rgba(0,0,0,0.40),
                0px 0px 25px rgba(29,78,137,0.70); /* Blue Glow */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-float-box">
    <h1 style="margin: 0; font-size: 48px; font-weight: 800;">
        Mina Multi-Purpose Store
    </h1>
    <h3 style="margin: 0; margin-top: 10px; font-size: 22px; color: #dce3eb;">
        Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox
    </h3>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
