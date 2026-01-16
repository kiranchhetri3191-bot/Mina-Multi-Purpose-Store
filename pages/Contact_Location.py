import streamlit as st

st.set_page_config(layout="wide")

# ---- CSS ----
st.markdown("""
<style>
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
    margin-bottom: 25px;
}
.section-title {
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>📞 Contact & Location</div>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h2>Contact Details</h2>
    📞 <b>Phone:</b> +919775410996 <br>
    💬 <b>WhatsApp:</b> +919775410996 <br>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>Store Location</h2>
    📍 <b>Near Pragati Club, Birpara, West Bengal</b>  
    </div>
    """, unsafe_allow_html=True)

st.success("📌 We are always happy to serve you!")
