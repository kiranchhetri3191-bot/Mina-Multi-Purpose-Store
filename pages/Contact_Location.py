import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contact - Mina Multi-Purpose Store",
    page_icon="Mina Store Logo.png",
    layout="wide"
)

# -------------------------
# Detect Dark / Light Mode
# -------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

if is_dark:
    BG = "#0d1117"
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    NEON_TEXT = "#00ccff"
else:
    BG = "#eef3ff"
    CARD_BG = "#ffffff"
    TEXT = "#000000"
    NEON_TEXT = "#000000"

# -------------------------
# Global CSS (Stable)
# -------------------------
st.markdown(f"""
<style>

body {{
    background-color: {BG} !important;
    color: {TEXT} !important;
}}

h2 {{
    margin-bottom: 10px;
}}

.card {{
    background: {CARD_BG};
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #0a4ba6;
    box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.25);
    margin-bottom: 20px;
}}

.card * {{
    color: {TEXT} !important;
}}

.social-btn {{
    display: inline-block;
    padding: 10px 20px;
    background: #0a4ba6;
    color: #fff !important;
    border-radius: 8px;
    font-weight: 700;
    margin: 5px;
    text-decoration: none;
}}

.gmail-btn {{
    background: #d93025 !important;
    color: #fff !important;
}}

.call-btn {{
    display: inline-block;
    padding: 15px 30px;
    background: linear-gradient(90deg, #ff0066, #ffcc00);
    color: #fff !important;
    font-weight: 700;
    font-size: 20px;
    border-radius: 50px;
    text-decoration: none;
    margin-top: 15px;
}}

.map-box {{
    background: {CARD_BG};
    padding: 15px;
    border-radius: 15px;
    border-left: 5px solid #0a4ba6;
    box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.25);
}}

.footer {{
    text-align: center;
    margin-top: 30px;
    opacity: 0.8;
}}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown(
    f"<h1 style='text-align:center; color:{NEON_TEXT}; font-weight:900;'>📞 Contact & Location</h1>",
    unsafe_allow_html=True
)
st.write("---")

# -------------------------
# Columns
# -------------------------
col1, col2 = st.columns(2)

# LEFT CARD
with col1:
    st.markdown(f"""
    <div class="card">
        <h2>Contact Details</h2>

        📞 <b>Phone:</b> +91 9775410996 <br><br>

        💬 <b>WhatsApp:</b> +91 9775410996 <br><br>

        ✉️ <b>Email:</b> 
        <a href="mailto:minamultipurposestore@gmail.com">
            minamultipurposestore@gmail.com
        </a><br><br>

        🔗 <b>LinkedIn:</b>
        <a href="https://www.linkedin.com/company/mina-multi-purpose-store" target="_blank">
            Mina Multi-Purpose Store
        </a><br><br>

        🕒 <b>Opening Hours:</b><br>
        Everyday: <b>7:00 AM – 10:00 PM</b>
    </div>
    """, unsafe_allow_html=True)

# RIGHT CARD
with col2:
    st.markdown(f"""
    <div class="card">
        <h2>Store Location</h2>
        📍 <b>Mina Multi-Purpose Store</b><br>
        Near Pragati Club, Birpara, West Bengal
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Social Buttons
# -------------------------
st.markdown("""
<div style="text-align:center;">
    <a href="https://wa.me/919775410996" class="social-btn">💬 WhatsApp</a>
    <a href="https://www.linkedin.com/company/mina-multi-purpose-store" class="social-btn">🔗 LinkedIn</a>
    <a href="mailto:minamultipurposestore@gmail.com" class="social-btn gmail-btn">📧 Gmail</a>
    <a href="tel:+919775410996" class="social-btn">📞 Call</a>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Call Now Big Button
# -------------------------
st.markdown("""
<div style="text-align:center;">
    <a href="tel:+919775410996" class="call-btn">📞 Call Now</a>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Google Map
# -------------------------
st.markdown("<div class='map-box'><h2 style='text-align:center;'>📍 Find Us on Google Maps</h2></div>", unsafe_allow_html=True)

components.html(
    """
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11509.41960234578!2d89.1368766!3d26.725808!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39e3bfb8052ef40d%3A0xec84f6cdedee5f4a!2sMina%20Multi-Purpose%20Store!5e0!3m2!1sen!2sin!4v1707120000000!5m2!1sen!2sin"
        width="100%" 
        height="350"
        style="border:0; border-radius:12px;"
        allowfullscreen=""
        loading="lazy"
    ></iframe>
    """,
    height=380,
)

# -------------------------
# Footer
# -------------------------
st.markdown("""
<div class="footer">
    ❤️ Thank you for choosing Mina Multi-Purpose Store!
</div>
""", unsafe_allow_html=True)
