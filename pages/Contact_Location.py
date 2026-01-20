import streamlit as st
import streamlit.components.v1 as components
import datetime
import pytz

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
# Auto Colors
# ---------------------------------------------------
if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    TEXT_GLOW = "#ffffff"
    NEON_TEXT = "#00ccff"
    CARD_SHADOW = "0px 6px 20px rgba(0,150,255,0.25)"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT = "#000000"
    TEXT_GLOW = "#000000"
    NEON_TEXT = "#000000"
    CARD_SHADOW = "0px 6px 20px rgba(0,100,255,0.25)"

# ---------------------------------------------------
# CSS + Floating Buttons
# ---------------------------------------------------
st.markdown(f"""
<style>

body {{
    background: {BG} !important;
    color: {TEXT} !important;
}}

@keyframes led-color-shift {{
    0%   {{ color: #ff0000; text-shadow: 0 0 12px #ff0000; }}
    20%  {{ color: #ff9900; text-shadow: 0 0 14px #ff9900; }}
    40%  {{ color: #ffff00; text-shadow: 0 0 18px #ffff00; }}
    60%  {{ color: #00ff00; text-shadow: 0 0 14px #00ff00; }}
    80%  {{ color: #00ccff; text-shadow: 0 0 18px #00ccff; }}
    100% {{ color: #ff00ff; text-shadow: 0 0 18px #ff00ff; }}
}}

.double-text {{
    position: relative;
    font-size: 40px;
    font-weight: 900;
    text-align: center;
}}

.double-text::before {{
    content: "📞 Contact & Location";
    position: absolute;
    top: 0;
    left: 0;
    color: {TEXT_GLOW};
    z-index: -1; 
    filter: blur(3px);
}}

.double-text {{
    color: {NEON_TEXT};
    animation: led-color-shift 3s infinite linear;
}}

.map-title {{
    font-size: 28px;
    font-weight: 900;
    text-align: center;
    animation: led-color-shift 3s infinite linear;
}}

.card {{
    background: {CARD_BG};
    padding: 25px;
    border-radius: 18px;
    border-left: 5px solid #0a4ba6;
    box-shadow: {CARD_SHADOW};
    margin-bottom: 25px;
}}

.card, .card * {{
    color: {TEXT} !important;
}}

.map-box {{
    background: {CARD_BG};
    padding: 15px;
    border-radius: 18px;
    border-left: 5px solid #0a4ba6;
    box-shadow: {CARD_SHADOW};
    margin-top: 25px;
}}

.map-box, .map-box * {{
    color: {TEXT} !important;
}}

.call-btn {{
    display: inline-block;
    padding: 14px 28px;
    background: linear-gradient(90deg, #ff0066, #ffcc00);
    color: white !important;
    font-size: 22px;
    font-weight: 800;
    border-radius: 50px;
    text-align: center;
    text-decoration: none;
    box-shadow: 0px 0px 20px rgba(255, 0, 150, 0.6);
}}

 /* Floating Buttons */
.floating-container {{
    position: fixed;
    bottom: 25px;
    right: 25px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    z-index: 9999;
}}

.float-btn {{
    width: 55px;
    height: 55px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    color: white;
    background: linear-gradient(135deg, #ff0099, #ff6600);
    text-decoration: none;
    box-shadow: 0 0 18px rgba(255,0,150,0.7);
    transition: 0.2s;
    pointer-events: auto !important;
}}

.float-btn:hover {{
    transform: scale(1.12);
    box-shadow: 0 0 25px rgba(255,200,0,0.9);
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# STORE TIMING (9 AM – 7 PM)
# ---------------------------------------------------
OPEN_HOUR = 9
CLOSE_HOUR = 19

india = pytz.timezone("Asia/Kolkata")
now = datetime.datetime.now(india)
current_hour = now.hour

if OPEN_HOUR <= current_hour < CLOSE_HOUR:
    STATUS_TEXT = "🟢 OPEN NOW"
    STATUS_COLOR = "#00ff66"
else:
    STATUS_TEXT = "🔴 CLOSED NOW"
    STATUS_COLOR = "#ff3333"

st.markdown(f"""
<div style="
    padding: 14px;
    text-align: center;
    font-size: 26px;
    font-weight: 900;
    margin-bottom: 15px;
    border-radius: 14px;
    background: rgba(0,0,0,0.25);
    color: {STATUS_COLOR};
    text-shadow: 0 0 18px {STATUS_COLOR};
">
    {STATUS_TEXT}
</div>
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
        <h2>Contact Details</h2>
        📞 <b>Phone:</b> +91 9775410996 <br><br>
        💬 <b>WhatsApp:</b> +91 9775410996 <br>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h2>Store Location</h2>
        📍 <b>Mina Multi-Purpose Store<br>Near Pragati Club, Birpara, West Bengal</b>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# CALL BUTTON
# ---------------------------------------------------
st.markdown("""
<div style="text-align:center; margin-top:15px; margin-bottom:20px;">
    <a href="tel:+919775410996" class="call-btn">📞 Call Now</a>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAP
# ---------------------------------------------------
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

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.success("📌 We are always happy to serve you!")

# ---------------------------------------------------
# FLOATING CONTACT BUTTONS (CLICKABLE)
# ---------------------------------------------------
st.markdown("""
<div class="floating-container">

    <!-- CALL -->
    <a class="float-btn" href="tel:+919775410996" target="_blank" style="pointer-events:auto;">📞</a>

    <!-- LINKEDIN -->
    <a class="float-btn" href="https://www.linkedin.com/company/mina-multi-purpose-store" target="_blank" style="pointer-events:auto;">🔗</a>

    <!-- EMAIL -->
    <a class="float-btn" href="mailto:minamultipurposestore@gmail.com" target="_blank" style="pointer-events:auto;">✉️</a>

</div>
""", unsafe_allow_html=True)
