import streamlit as st

st.set_page_config(page_title="Contact - Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

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
    CARD_BG = "#161b22"
    TEXT = "#ffffff"
    CARD_SHADOW = "0px 6px 20px rgba(0, 150, 255, 0.25)"
else:
    BG = "#eef3ff"
    CARD_BG = "rgba(255,255,255,0.92)"
    TEXT = "#0a0a0a"
    CARD_SHADOW = "0px 6px 20px rgba(0, 100, 255, 0.25)"

# ---------------------------------------------------
# CSS (LED Header + Neon Cards)
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

@keyframes led-pulse {{
    0%   {{ opacity: 0.75; transform: scale(1); }}
    50%  {{ opacity: 1;    transform: scale(1.05); }}
    100% {{ opacity: 0.75; transform: scale(1); }}
}}

.section-title {{
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 10px;
    animation: led-color-shift 3s infinite linear, led-pulse 2s infinite ease-in-out;
}}

.card {{
    background: {CARD_BG};
    padding: 25px;
    border-radius: 18px;
    box-shadow: {CARD_SHADOW};
    border-left: 5px solid #0a4ba6;
}}

.card h2 {{
    margin-top: 0;
    color: {TEXT};
}}

.card p, .card b {{
    color: {TEXT};
    font-size: 18px;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------
st.markdown("<div class='section-title'>📞 Contact & Location</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------------------------------------
# CONTENT
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
        📍 <b>Near Pragati Club, Birpara, West Bengal</b>
    </div>
    """, unsafe_allow_html=True)

st.success("📌 We are always happy to serve you!")
