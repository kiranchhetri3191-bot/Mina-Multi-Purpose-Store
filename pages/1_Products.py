import streamlit as st

st.set_page_config(
    page_title="Products - Mina Multi-Purpose Store",
    page_icon="./Mina Store Logo.png",
    layout="wide"
)

# ---------------------------------------------------
# Detect Dark / Light Mode
# ---------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# Auto Colors
if is_dark:
    TEXT = "#ffffff"
else:
    TEXT = "#000000"

# ---------------------------------------------------
# Page Heading
# ---------------------------------------------------
st.markdown(f"""
<h1 style="text-align:center; color:{TEXT}; margin-bottom:10px;">
    🛍️ Our Products
</h1>
<p style="text-align:center; color:{TEXT}; font-size:18px;">
    Explore all available categories at Mina Multi-Purpose Store.
</p>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# BIG LOGO STYLE IMAGES (NO BOX)
# ---------------------------------------------------

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown(f"<h2 style='text-align:center; color:{TEXT};'>Gift Items</h2>", unsafe_allow_html=True)
    st.image("./images/gift.png", use_column_width=True)

with col2:
    st.markdown(f"<h2 style='text-align:center; color:{TEXT};'>Grocery Essentials</h2>", unsafe_allow_html=True)
    st.image("./images/grocery.png", use_column_width=True)

with col3:
    st.markdown(f"<h2 style='text-align:center; color:{TEXT};'>Hardware Tools</h2>", unsafe_allow_html=True)
    st.image("./images/hardware.png", use_column_width=True)

with col4:
    st.markdown(f"<h2 style='text-align:center; color:{TEXT};'>Printing Services</h2>", unsafe_allow_html=True)
    st.image("./images/print.png", use_column_width=True)
