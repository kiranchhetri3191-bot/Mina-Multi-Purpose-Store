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

# Theme Colors
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    CARD_SHADOW = "0px 6px 18px rgba(0,150,255,0.25)"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT = "#0a0a0a"
    CARD_SHADOW = "0px 6px 18px rgba(0,100,255,0.20)"

# CSS Styling
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
    margin-bottom: 25px;
    text-shadow: 0 0 6px #2ab7ff, 0 0 12px #2ab7ff;
}}

.sub-title {{
    font-size: 26px;
    font-weight: 800;
    text-align: center;
    color: #2ab7ff;
    text-shadow: 0 0 5px #2ab7ff;
    margin-bottom: 10px;
}}

.card {{
    background: {CARD_BG};
    padding: 25px;
    border-radius: 18px;
    border-left: 5px solid #2ab7ff;
    box-shadow: {CARD_SHADOW};
    margin-bottom: 25px;
}}

.call-btn, .email-btn, .linkedin-btn {{
    display: inline-block;
    padding: 12px 28px;
    background: #2ab7ff;
    color: white !important;
    font-size: 20px;
    font-weight: 800;
    border-radius: 50px;
    text-decoration: none;
    margin: 8px;
    box-shadow: 0 0 10px #2ab7ff, 0 0 16px #0a99e0;
}}

.linkedin-icon {{
    width: 48px;
    transition: 0.2s ease-in-out;
}}

.linkedin-icon:hover {{
    transform: scale(1.15);
    filter: drop-shadow(0 0 8px #2ab7ff);
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
    font-size: 36px;
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

.footer {{
    text-align: center;
    color: {TEXT};
    margin-top: 45px;
    padding-top: 20px;
    border-top: 2px solid #2ab7ff50;
}}

</style>
""", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 1️⃣ PAGE HEADER
# -------------------------------------------------------------------
st.markdown("<div class='section-title'>📞 Contact & Location</div>", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 2️⃣ GOOGLE MAP FIRST (Requested Order)
# -------------------------------------------------------------------
st.markdown("<div class='sub-title'>📍 Find Us on Google Maps</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='card'>
<iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11509.41960234578!2d89.1368766!3d26.725808!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39e3bfb8052ef40d%3A0xec84f6cdedee5f4a!2sMina%20Multi-Purpose%20Store!5e0!3m2!1sen!2sin!4v1707120000000!5m2!1sen!2sin"
    width="100%" 
    height="350"
    style="border:0; border-radius:12px;"
    allowfullscreen=""
    loading="lazy"></iframe>
</div>
""", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 3️⃣ STORE LOCATION CARD
# -------------------------------------------------------------------
st.markdown("<div class='sub-title'>🏪 Store Location</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='card'>
<b>Mina Multi-Purpose Store</b><br>
Near Pragati Club, Birpara, West Bengal <br><br>

🕙 <b>Opening:</b> 9:00 AM<br>
🕖 <b>Closing:</b> 7:00 PM
</div>
""", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 4️⃣ CONTACT DETAILS
# -------------------------------------------------------------------
st.markdown("<div class='sub-title'>📞 Contact Details</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='card'>
📞 <b>Phone:</b> +91 9775410996 <br><br>
💬 <b>WhatsApp:</b> +91 9775410996 <br><br>
📧 <b>Email:</b> minamultipurposestore@gmail.com <br>
</div>
""", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 5️⃣ BUTTON GROUP (BOTTOM)
# -------------------------------------------------------------------
st.markdown("<div class='sub-title'>⚡ Quick Actions</div>", unsafe_allow_html=True)

# Buttons row
st.markdown(f"""
<div style="text-align:center;">

    <!-- Call -->
    <a href="tel:+919775410996" class="call-btn">📞 Call Now</a>

    <!-- Email -->
    <a href="mailto:minamultipurposestore@gmail.com" class="email-btn">✉️ Email Us</a>

    <!-- LinkedIn -->
    <a href="https://www.linkedin.com/company/mina-multi-purpose-store" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png"
             class="linkedin-icon"
             style="filter: {'invert(1)' if is_dark else 'none'};">
    </a>

</div>
""", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 6️⃣ FLOATING BUTTONS
# -------------------------------------------------------------------
st.markdown("""
<a href="https://wa.me/919775410996" class="float-whatsapp">💬</a>
<a href="tel:+919775410996" class="float-call">📞</a>
""", unsafe_allow_html=True)



# -------------------------------------------------------------------
# 7️⃣ FOOTER
# -------------------------------------------------------------------
st.markdown("""
<div class="footer">
<b>Mina Multi-Purpose Store</b><br>
Near Pragati Club, Birpara, West Bengal<br>
© 2024 All Rights Reserved
</div>
""", unsafe_allow_html=True)
