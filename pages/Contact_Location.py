import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact - Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# ---------------------------------------------------
# RELIABLE DARK MODE DETECTION
# ---------------------------------------------------
bg_col = st.get_option("theme.backgroundColor")

is_dark = bg_col in ["#0e1117", "#000000", "#1e1e1e", "#0d1117"]

# ---------------------------------------------------
# THEME COLORS (STYLE 1)
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    ICON_FILTER = "invert(1)"  # makes emojis/icons visible
else:
    BG = "#eef3ff"
    CARD_BG = "#ffffff"
    TEXT = "#0a0a0a"
    ICON_FILTER = "none"


# ---------------------------------------------------
# CSS (CLEAN + FIXED)
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background-color: {BG};
    color: {TEXT};
}}

.section-title {{
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 25px;
    color: #2ab7ff;
    text-shadow: 0 0 6px #2ab7ff;
}}

.sub-title {{
    font-size: 26px;
    font-weight: 700;
    text-align: center;
    color: #2ab7ff;
    margin-bottom: 12px;
    text-shadow: 0 0 5px #2ab7ff;
}}

.card {{
    background: {CARD_BG};
    padding: 22px;
    border-radius: 14px;
    border-left: 5px solid #2ab7ff;
    box-shadow: 0 0 12px rgba(0,162,255,0.20);
    margin-bottom: 20px;
}}

.call-btn, .email-btn {{
    display: inline-block;
    padding: 12px 30px;
    background: #2ab7ff;
    color: white !important;
    font-size: 20px;
    font-weight: 800;
    border-radius: 40px;
    text-decoration: none;
    margin: 6px;
    box-shadow: 0 0 12px #2ab7ff;
}}

.linkedin-icon {{
    width: 45px;
    transition: 0.2s;
    filter: {ICON_FILTER};
}}

.linkedin-icon:hover {{
    transform: scale(1.12);
    filter: drop-shadow(0 0 8px #2ab7ff);
}}

.float-whatsapp {{
    position: fixed;
    bottom: 22px;
    right: 22px;
    background: #25D366;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 34px;
    text-align: center;
    padding-top: 8px;
    box-shadow: 0 0 12px #25d366;
    z-index: 999;
}}

.float-call {{
    position: fixed;
    bottom: 95px;
    right: 22px;
    background: #2ab7ff;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 30px;
    text-align: center;
    padding-top: 10px;
    box-shadow: 0 0 12px #2ab7ff;
    z-index: 999;
}}

.footer {{
    text-align: center;
    color: {TEXT};
    margin-top: 40px;
    padding-top: 15px;
    border-top: 1px solid #2ab7ff50;
}}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# 1️⃣ HEADER
# ---------------------------------------------------
st.markdown("<div class='section-title'>📞 Contact & Location</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# 2️⃣ GOOGLE MAP FIRST
# ---------------------------------------------------
st.markdown("<div class='sub-title'>📍 Find Us on Google Maps</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
<iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11509.41960234578!2d89.1368766!3d26.725808!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39e3bfb8052ef40d%3A0xec84f6cdedee5f4a!2sMina%20Multi-Purpose%20Store!5e0!3m2!1sen!2sin!4v1707120000000!5m2!1sen!2sin"
    width="100%" 
    height="330"
    style="border:0; border-radius:12px;"
    allowfullscreen=""
    loading="lazy"></iframe>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# 3️⃣ STORE LOCATION
# ---------------------------------------------------
st.markdown("<div class='sub-title'>🏪 Store Location</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
<b>Mina Multi-Purpose Store</b><br>
Near Pragati Club, Birpara, West Bengal <br><br>

🕙 Opening: 9:00 AM<br>
🕖 Closing: 7:00 PM
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# 4️⃣ CONTACT DETAILS
# ---------------------------------------------------
st.markdown("<div class='sub-title'>📞 Contact Details</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
📞 Phone: +91 9775410996 <br><br>
💬 WhatsApp: +91 9775410996 <br><br>
📧 Email: minamultipurposestore@gmail.com
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# 5️⃣ QUICK ACTION BUTTONS
# ---------------------------------------------------
st.markdown("<div class='sub-title'>⚡ Quick Actions</div>", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center;">

    <a href="tel:+919775410996" class="call-btn">📞 Call Now</a>

    <a href="mailto:minamultipurposestore@gmail.com" class="email-btn">✉️ Email Us</a>

    <a href="https://www.linkedin.com/company/mina-multi-purpose-store" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png"
             class="linkedin-icon">
    </a>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# FLOATING BUTTONS
# ---------------------------------------------------
st.markdown("""
<a href="https://wa.me/919775410996" class="float-whatsapp">💬</a>
<a href="tel:+919775410996" class="float-call">📞</a>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("""
<div class="footer">
<b>Mina Multi-Purpose Store</b><br>
Near Pragati Club, Birpara, West Bengal<br>
© 2024 All Rights Reserved
</div>
""", unsafe_allow_html=True)
