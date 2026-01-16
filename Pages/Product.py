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
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.15);
}
.section-title {
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🛒 Our Products</div>", unsafe_allow_html=True)
st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'><h3>🎁 Gift Items</h3>Soft toys, greeting cards, toys, showpieces.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>📚 Stationery</h3>School notebooks, pens, files, supplies.</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><h3>🍫 Chocolates & Snacks</h3>Biscuits, chips, candies, chocolates.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>🛒 Grocery Items</h3>Daily essentials, soaps, detergents, dry foods.</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'><h3>🔧 Hardware Items</h3>Tapes, batteries, tools, small hardware.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>📝 Xerox & Printing</h3>Black & white Xerox, printouts.</div>", unsafe_allow_html=True)
