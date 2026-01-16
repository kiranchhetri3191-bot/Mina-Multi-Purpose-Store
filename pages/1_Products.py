import streamlit as st

st.set_page_config(layout="wide")

st.markdown("<h1 style='color:#2c3e50;'>🛒 Our Products</h1>", unsafe_allow_html=True)

st.write("---")

# ---- CSS ----
st.markdown("""
<style>
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'><h3>🎁 Gift Items</h3>Soft toys, greeting cards, toys.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>📚 Stationery</h3>Notebooks, pens, school supplies.</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><h3>🍫 Chocolates & Snacks</h3>Biscuits, chips, chocolates.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>🛒 Grocery Items</h3>Daily essentials, soaps, detergents.</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'><h3>🔧 Hardware Items</h3>Tapes, batteries, small tools.</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>📝 Xerox Services</h3>B/W Xerox, print-outs.</div>", unsafe_allow_html=True)
