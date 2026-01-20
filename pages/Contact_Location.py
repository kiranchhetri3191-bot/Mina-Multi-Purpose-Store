import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact - Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# Detect DARK / LIGHT Mode
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    CARD_SHADOW = "0px 6px 20px rgba(0,150,255,0.25)"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT = "#0a0a0a"
    CARD_SHADOW = "0px 6px 20px rgba(0,100,255,0.25)"

# ---------- CSS ----------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
    color: {TEXT} !important;
}}

.section-title {{
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    color: #2ab7ff;
    text-shadow: 0 0 5px #2ab7ff, 0 0 12px #2ab7ff;
}}

.map-title {{
    font-size: 28px;
    font-weight: 900;
    text-align: center;
    color: #2ab7ff;
    text-shadow:
        0 0 5px #2ab7ff,
        0 0 10px #2ab7ff,
        0 0 15px #0a99e0;
}}

.card {{
    background: {CARD_BG};
    padding: 25px;
    border-radius: 18px;
    border-left: 5px solid #0a4ba6;
    box-shadow: {CARD_SHADOW};
    margin-bottom: 25px;
}}

.map-box {{
    background: {CARD_BG};
    padding: 15px;
    border-radius: 18px;
    border-left: 5px solid #0a4ba6;
    box-shadow: {CARD_SHADOW};
    margin-top: 25px;
}}

.call-btn {{
    display: inline-block;
    padding: 14px 28px;
    background: #2ab7ff;
    color: white !important;
    font-size: 22px;
    font-weight: 800;
    border-radius: 50px;
    text-decoration: none;
    box-shadow:
        0 0 6px #2ab7ff,
        0 0 12px #2ab7ff,
        0 0 18px #0a99e0;
}}

.email-btn {{
    display: inline-block;
    padding: 12px 24px;
    background: #2ab7ff;
    color: white !important;
    font-size: 18px;
    font-weight: 700;
    border-radius: 10px;
    text-decoration: none;
    box-shadow: 0 0 10px #2ab7ff;
}}

.linkedin-icon {{
    width: 45px;
    transition: 0.25s ease-in-out;
}}

.linkedin-icon:hover {{
    filter: drop-shadow(0 0 8px #2ab7ff)
            drop-shadow(0 0 12px #2ab7ff);
    transform: scale(1.15);
}}

.footer {{
    text-align: center;
    color: {TEXT};
    margin-top: 35px;
    padding-top: 20px;
    border-top: 2px solid #2ab7ff50;
}}

.float-whatsapp {{
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: #25D366;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 35px;
    text-align: center;
    padding-top: 8px;
    box-shadow: 0 0 12px #25D366;
    z-index: 999;
}}

.float-call {{
    position: fixed;
    bottom: 95px;
    right: 25px;
    background: #2ab7ff;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 32px;
    text-align: center;
    padding-top: 10px;
    box-shadow: 0 0 12px #2ab7ff;
    z-index: 999;
}}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='section-title'>📞 Contact & Location</div>", unsafe_allow_html=True)
st.write("---")

# ---------- CONTACT + LOCATION ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card">
        <h2>Contact Details</h2>
        📞 <b>Phone:</b> +91 9775410996 <br><br>
        💬 <b>WhatsApp:</b> +91 9775410996 <br><br>
        📧 <b>Email:</b> minamultipurposestore@gmail.com <br><br>
        <a href="mailto:minamultipurposestore@gmail.com" class="email-btn">✉️ Send Email</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h2>Store Location</h2>
        📍 <b>Mina Multi-Purpose Store<br>Near Pragati Club, Birpara, West Bengal</b>
        <br><br>
        🕙 <b>Opening:</b> 9:00 AM <br>
        🕖 <b>Closing:</b> 7:00 PM
    </div>
    """, unsafe_allow_html=True)

# ---------- CALL BUTTON ----------
st.markdown("""
<div style="text-align:center; margin-top:15px; margin-bottom:20px;">
    <a href="tel:+919775410996" class="call-btn">📞 Call Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- GOOGLE MAP ----------
st.markdown("<div class='map-box'><h2 class='map-title'>📍 Find Us on Google Maps</h2></div>", unsafe_allow_html=True)

components.html(
    """
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11509.41960234578!2d89.1368766!3d26.725808!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39e3bfb8052ef40d%3A0xec84f6cdedee5f4a!2sMina%20Multi-Purpose%20Store!5e0!3m2!1sen!2sin!4v1707120000000!5m2!1sen!2sin"
        width="100%" 
        height="350"
        style="border:0; border-radius:12px;"
        allowfullscreen=""
        loading="lazy"></iframe>
    """,
    height=380,
)

# ---------- SOCIAL LINKS (ONLY LINKEDIN) ----------
st.markdown(f"""
<div style="text-align:center; margin-top:35px;">
    <a href="https://www.linkedin.com/company/mina-multi-purpose-store" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png"
             class="linkedin-icon"
             style="filter: {'invert(1)' if is_dark else 'none'};">
    </a>
</div>
""", unsafe_allow_html=True)

# ---------- FLOATING BUTTONS ----------
st.markdown("""
<a href="https://wa.me/919775410996" class="float-whatsapp">💬</a>
<a href="tel:+919775410996" class="float-call">📞</a>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <b>Mina Multi-Purpose Store</b><br>
    Near Pragati Club, Birpara, West Bengal<br>
    © 2024 All Rights Reserved
</div>
""", unsafe_allow_html=True)
