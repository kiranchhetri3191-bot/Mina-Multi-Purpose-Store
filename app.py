import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- MODERN, COMPACT HEADER CSS ----
st.markdown("""
<style>
body { background-color: #f6f8fb; font-family: 'Segoe UI', sans-serif; }

/* Hero */
.hero {
  background: linear-gradient(90deg, #1f6feb, #0f2545);
  padding: 18px 22px;
  border-radius: 14px;
  color: white;
  margin-bottom: 28px;
}

/* Layout inside hero */
.hero-inner {
  display: flex;
  align-items: center;
  gap: 18px;
  justify-content: flex-start;
  max-width: 1100px;
  margin: 0 auto;
}

/* Small circular logo */
.logo-compact {
  width: 72px;
  height: 72px;
  border-radius: 14px;
  object-fit: cover;
  box-shadow: 0 6px 18px rgba(4,12,30,0.35);
  border: 2px solid rgba(255,255,255,0.08);
}

/* Brand text */
.brand {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.brand-title {
  font-size: 36px;
  font-weight: 700;
  letter-spacing: -0.6px;
  margin: 0;
}
.brand-sub {
  margin: 4px 0 0 0;
  font-size: 15px;
  color: rgba(255,255,255,0.9);
}

/* Decorative accent line under brand */
.accent {
  height: 4px;
  width: 160px;
  margin-top: 12px;
  border-radius: 6px;
  background: linear-gradient(90deg, rgba(255,255,255,0.9), rgba(255,255,255,0.35));
}

/* Card style used below */
.card {
  background: white;
  padding: 26px;
  border-radius: 14px;
  box-shadow: 0 10px 30px rgba(13,30,60,0.06);
  margin-bottom: 22px;
}
.section-title {
  font-size: 26px;
  font-weight: 700;
  color: #12202f;
  margin-bottom: 12px;
}
@media(max-width:700px){
  .brand-title { font-size: 26px; }
  .logo-compact { width:56px; height:56px; border-radius:12px; }
  .accent { width: 120px; }
}
</style>
""", unsafe_allow_html=True)

# ---- HERO (compact logo + brand text) ----
logo_path = "Mina Store Logo.png"   # keep this file in same folder

st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="hero-inner">', unsafe_allow_html=True)

col1, col2 = st.columns([0.8, 8])  # column layout to align nicely

with col1:
    # show compact circular/rounded logo
    st.image(logo_path, width=72, use_column_width=False, output_format="PNG")

with col2:
    st.markdown("""
    <div class="brand">
      <div class="brand-title">Mina Multi-Purpose Store</div>
      <div class="brand-sub">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
      <div class="accent"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT US ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer a wide range of everyday essentials at fair prices:<br><br>

✔ Gift items  
✔ Grocery items  
✔ Basic hardware tools  
✔ Xerox & printing services  
<br>

Our mission is to offer <b>quality products, great convenience, and friendly service</b>.
</div>
""", unsafe_allow_html=True)

# ---- STORE TIMINGS ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
🕘 <b>Opens:</b> 9:00 AM<br>
🕖 <b>Closes:</b> 7:00 PM<br><br>
Open daily for your convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Use the sidebar to explore other pages!")
