import streamlit
st.markdown(f"""
<style>

@keyframes led-color-shift {{
    0%   {{ color: #ff0000; text-shadow: 0 0 12px #ff0000, 0 0 25px #ff0000; }}
    20%  {{ color: #ff9900; text-shadow: 0 0 12px #ff9900, 0 0 25px #ff9900; }}
    40%  {{ color: #ffff00; text-shadow: 0 0 15px #ffff00, 0 0 30px #ffff00; }}
    60%  {{ color: #00ff00; text-shadow: 0 0 12px #00ff00, 0 0 25px #00ff00; }}
    80%  {{ color: #00ccff; text-shadow: 0 0 15px #00ccff, 0 0 30px #00ccff; }}
    100% {{ color: #ff00ff; text-shadow: 0 0 15px #ff00ff, 0 0 30px #ff00ff; }}
}}

@keyframes led-pulse {{
    0%   {{ opacity: 0.75; transform: scale(1); }}
    50%  {{ opacity: 1;    transform: scale(1.05); }}
    100% {{ opacity: 0.75; transform: scale(1); }}
}}

.header-title {{
    font-size: 40px;
    font-weight: 900;
    animation: led-color-shift 3s infinite linear, led-pulse 2s infinite ease-in-out;
}}

.header-subtitle {{
    font-size: 20px;
    font-weight: 600;
    animation: led-color-shift 4s infinite linear, led-pulse 3s infinite ease-in-out;
}}

</style>
""", unsafe_allow_html=True)
