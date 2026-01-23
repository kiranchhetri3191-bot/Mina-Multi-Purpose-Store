import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mina Multi-Purpose Store",
    page_icon="Mina_Store_Logo.png",  # replace with your file name
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
    filter: invert(1); /* makes icons white */
}}

.floating-icon:hover {{
    transform: scale(1.15);
}}

/* Equal Spacing */
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
# FLOATING ICON BUTTONS (INCLUDING WHITE EMOJI-STYLE 📞)
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

<!-- PURE WHITE EMOJI-STYLE PHONE ICON -->
<a href="tel:+919775410996" class="floating-icon floating-call">
    <img src="data:image/svg+xml;utf8,
    <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'>
        <path fill='white' d='M34.6 30.8 29 35.4c-5.8-3.1-10.4-7.7-13.5-13.5l4.6-5.6c.5-.6.6-1.4.3-2.1l-3-7.2c-.6-1.6-2.4-2.3-3.9-1.6L7 8.4c-1.3.6-2.1 2-2 3.4C6 28.7 19.3 42 36.2 43c1.4.1 2.8-.7 3.4-2l2.9-6.5c.7-1.5 0-3.3-1.6-3.9l-7.2-3c-.7-.3-1.5-.2-2.1.2z'/>
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
