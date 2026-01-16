import streamlit as st

st.set_page_config(layout="wide")

st.markdown("<h1 style='color:#2c3e50;'>📞 Contact & Location</h1>", unsafe_allow_html=True)
st.write("---")

# ---- CSS ----
st.markdown("""
<style>
.card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---- CONTACT ----
st.markdown("""
<div class='card'>
<h2>Contact Us</h2>
📞 <b>Phone:</b> +91-9775411040 <br>
💬 <b>WhatsApp:</b> +91-9775411040 <br>
</div>
""", unsafe_allow_html=True)

# ---- LOCATION ----
st.markdown("""
<div class='card'>
<h2>Location</h2>
📍 <b>Near Pragati Club, Birpara, West Bengal</b>  
Easily accessible for all local customers.
</div>
""", unsafe_allow_html=True)
