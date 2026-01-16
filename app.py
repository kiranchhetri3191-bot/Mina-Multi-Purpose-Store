import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="🛍️", layout="wide")

# ---- CSS ----
st.markdown("""
<style>
body { background-color: #f5f5f5; }
.title { font-size: 50px; font-weight: bold; text-align: center; color: #2c3e50; }
.subtitle { font-size: 20px; text-align: center; color: #7f8c8d; }
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<div class='title'>🛍️ Mina Multi-Purpose Store</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your One-Stop Shop for Daily Essentials, Gifts & More</div>", unsafe_allow_html=True)

st.write("---")

# ---- ABOUT ----
st.markdown("<h2>About Us</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
Mina Multi-Purpose Store is a trusted neighborhood shop located near Pragati Club, Birpara, West Bengal.  
We provide a mix of gift items, groceries, hardware tools, and Xerox services at fair prices.  
Your convenience and satisfaction are our priority.
</div>
""", unsafe_allow_html=True)

# ---- HOURS ----
st.markdown("<h2>Store Timings</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
🕘 <b>Opens:</b> 9:00 AM  
🕖 <b>Closes:</b> 7:00 PM  
Open all days unless notified.
</div>
""", unsafe_allow_html=True)

st.success("✨ Explore our other pages using the sidebar menu!")
