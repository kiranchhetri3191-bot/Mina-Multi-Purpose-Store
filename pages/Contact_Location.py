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
# CSS — Neon + Floating Buttons
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
    color: {TEXT} !important;
}}

@keyframes led-color-shift {{
    0% {{ color: #00ccff; text-shadow: 0 0 12px #00ccff; }}
    50% {{ color: #0099ff; text-shadow: 0 0 18px #0099ff; }}
    100% {{ color: #00ccff; text-shadow: 0 0 12px #00ccff; }}
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
    text-shadow: 0 0 10px #00ccff, 0 0 20px #00ccff;
}}

.neon-title-black {{
    font-size: 28px;
    font-weight: 900;
    color: black !important;
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

/* -------- NEW FLOATING BUTTONS (Perfect equal spacing) -------- */

.floating-btn {{
    position: fixed;
    right: 25px;
    background: #00bfff;
    color: white !important;
    padding: 14px 22px;
    font-size: 20px;
    font-weight: 800;
    border-radius: 50px;
    text-decoration: none;
    box-shadow: 0 0 20px #00bfff;
    transition: 0.25s;
    z-index: 9999;
}}

.floating-btn:hover {{
    transform: scale(1.09);
}}

/* Equal vertical spacing = 60px */
.floating-whatsapp {{ bottom: 260px; }}
.floating-linkedin {{ bottom: 200px; }}
.floating-email {{ bottom: 140px; }}
.floating-call {{ bottom: 80px; }}

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
# CONTACT + LOCATION
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
# REMOVE OLD BUTTONS (WhatsApp + LinkedIn) — Already removed
# ---------------------------------------------------

# ---------------------------------------------------
# FLOATING BUTTONS — ONLY THESE REMAIN
# ---------------------------------------------------
st.markdown("""
<a href="https://wa.me/919775410996"
   class="floating-btn floating-whatsapp">💬 WhatsApp</a>

<a href="https://www.linkedin.com/company/mina-multi-purpose-store"
   class="floating-btn floating-linkedin">🔗 LinkedIn</a>

<a href="https://mail.google.com/mail/?view=cm&fs=1&to=minamultipurposestore@gmail.com" 
   class="floating-btn floating-email">✉️ Email</a>

<a href="tel:+919775410996" 
   class="floating-btn floating-call">📞 Call</a>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAP
# ---------------------------------------------------
st.markdown("<div class='map-box'><h2 class='neon-title-black'>📍 Find Us on Google Maps</h2></div>", unsafe_allow_html=True)

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
