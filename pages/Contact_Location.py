import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact - Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# ---------------------------------------------------
# Detect DARK / LIGHT Mode
# ---------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# ---------------------------------------------------
# Auto Colors for Both Modes
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#11161c"
    TEXT = "#ffffff"
    NEON_BORDER = "0 0 18px #00bfff, 0 0 28px #00bfff"
else:
    BG = "#eef3ff"
    CARD_BG = "white"
    TEXT = "#000000"
    NEON_BORDER = "0 0 15px #00bfff, 0 0 25px #00bfff"

# ---------------------------------------------------
# CSS — Neon + Icon Buttons + Map Box
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
    color: {TEXT} !important;
}}

@keyframes led-color-shift {{
    0% {{ color: #00ccff; text-shadow: 0 0 10px #00ccff; }}
    50% {{ color: #0099ff; text-shadow: 0 0 16px #0099ff; }}
    100% {{ color: #00ccff; text-shadow: 0 0 10px #00ccff; }}
}}

.double-text {{
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    animation: led-color-shift 2.8s infinite linear;
}}

.neon-title {{
    font-size: 28px;
    font-weight: 900;
    color: #00ccff !important;
    text-shadow: 0 0 10px #00ccff;
}}

.card {{
    background: {CARD_BG};
    padding: 25px;
    border-radius: 16px;
    border: 3px solid #00bfff;
    box-shadow: {NEON_BORDER};
    margin-bottom: 25px;
}}

.card, .card * {{
    color: {TEXT} !important;
}}

/* -------- Floating Round Neon Icons -------- */

.floating-icon {{
    position: fixed;
    right: 25px;
    width: 58px;
    height: 58px;
    border-radius: 50%;
    background: #00bfff;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 22px #00bfff;
    transition: 0.25s;
    z-index: 9999;
}}

.floating-icon img {{
    width: 30px;
    filter: invert(1); /* Makes icons white */
}}

.floating-icon:hover {{
    transform: scale(1.15);
}}

/* Perfect Equal Spacing */
.floating-whatsapp {{ bottom: 260px; }}
.floating-linkedin {{ bottom: 200px; }}
.floating-email {{ bottom: 140px; }}
.floating-call {{ bottom: 80px; }}

/* MAP BOX */
.map-box {{
    background: {CARD_BG};
    padding: 18px;
    border-radius: 16px;
    border: 3px solid #00bfff;
    box-shadow: {NEON_BORDER};
    margin-top: 35px;
    margin-bottom: 10px;
}}

.map-title {{
    font-size: 26px;
    font-weight: 900;
    color: #00ccff;
    text-shadow: 0 0 10px #00ccff;
    text-align: center;
}}

.footer {{
    text-align:center;
    margin-top:40px;
    font-size:18px;
    opacity:0.8;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("<div class='double-text'>📞 Contact & Location</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------------------------------------
# CONTACT + LOCATION CARDS
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card">
        <h2 class='neon-title'>Contact Details</h2>
        📞 <b>Phone:</b> +91 9775410996 <br><br>
        💬 <b>WhatsApp:</b> +91 9775410996 <br><br>
        ✉️ <b>Email:</b> minamultipurposestore@gmail.com <br><br>
        🔗 <b>LinkedIn:</b>
        <a href="https://www.linkedin.com/company/mina-multi-purpose-store" target="_blank">
            Mina Multi-Purpose Store
        </a><br><br>
        🕒 <b>Opening Hours:</b> 9 AM – 7 PM
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h2 class='neon-title'>Store Location</h2>
        📍 <b>Mina Multi-Purpose Store</b><br>
        Near Pragati Club, Birpara, West Bengal <br><br>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# FLOATING ICON BUTTONS (SAFE + NO COPYRIGHT)
# ---------------------------------------------------
st.markdown("""
<a href="https://wa.me/919775410996" class="floating-icon floating-whatsapp">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/whatsapp.svg">
</a>

<a href="https://www.linkedin.com/company/mina-multi-purpose-store"
   class="floating-icon floating-linkedin">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg">
</a>

<a href="https://mail.google.com/mail/?view=cm&fs=1&to=minamultipurposestore@gmail.com" 
   class="floating-icon floating-email">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/gmail.svg">
</a>

<!-- FINAL SAFE CALL ICON (MIT LICENSE) -->
<a href="tel:+919775410996" class="floating-icon floating-call">
    <img src="data:image/svg+xml;utf8,
    <svg xmlns='http://www.w3.org/2000/svg' fill='white' viewBox='0 0 24 24'>
        <path d='M2 4.5C2 3.12 3.12 2 4.5 2h3c.66 0 1.25.32 1.65.85l2 2.62c.43.56.5 1.31.18 1.94L9.7 9.7a1 1 0 0 0-.13 1.04c.62 1.33 1.69 2.71 3.02 3.75 1.33 1.03 2.66 1.7 4 2a1 1 0 0 0 1.06-.46l1.06-1.7c.37-.6 1.05-.93 1.74-.82l2.76.46c.82.14 1.45.85 1.45 1.69v3c0 1.38-1.12 2.5-2.5 2.5C10.19 22 2 13.81 2 4.5z'/>
    </svg>
    ">
</a>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAP BOX
# ---------------------------------------------------
st.markdown("<div class='map-box'><div class='map-title'>📍 Find Us on Google Maps</div></div>",
            unsafe_allow_html=True)

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

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("""
<div class='footer'>
    ❤️ Thank you for choosing Mina Multi-Purpose Store — Birpara’s Most Trusted Shop
</div>
""", unsafe_allow_html=True)
