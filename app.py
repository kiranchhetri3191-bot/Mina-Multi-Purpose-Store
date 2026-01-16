import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# ---- CREATIVE COLORS + GLASSMORPHISM CSS ----
st.markdown("""
<style>
/* Page background: soft creative gradient with subtle diagonal pattern */
:root{
  --bg1: #f6f3ff; /* light lavender */
  --bg2: #e6fff7; /* mint */
  --accent: #3b82f6; /* blue accent */
  --accent-2: #7c3aed; /* purple accent */
  --card-bg: rgba(255,255,255,0.55);
  --glass-border: rgba(255,255,255,0.45);
  --muted: #2f3b45;
}

/* Overall page */
body {
  background: linear-gradient(120deg, var(--bg1) 0%, var(--bg2) 60%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: var(--muted);
}

/* Decorative soft diagonal overlay */
.appview-container .main > div {
  background-image: radial-gradient(circle at 10% 10%, rgba(60,99,246,0.05), transparent 10%),
                    radial-gradient(circle at 90% 90%, rgba(124,58,237,0.04), transparent 12%);
}

/* Hero / compact header styling */
.hero {
  padding: 18px 22px;
  border-radius: 14px;
  margin-bottom: 28px;
  /* soft two-tone inner gradient for hero */
  background: linear-gradient(90deg, rgba(59,130,246,0.95), rgba(124,58,237,0.92));
  color: white;
  box-shadow: 0 12px 40px rgba(21,30,61,0.12);
}

/* hero inner layout */
.hero-inner {
  display:flex;
  align-items:center;
  gap:18px;
  max-width:1200px;
  margin:0 auto;
}

/* compact logo */
.logo-compact {
  width:72px;
  height:72px;
  border-radius:12px;
  object-fit:cover;
  border: 2px solid rgba(255,255,255,0.18);
  box-shadow: 0 8px 20px rgba(12,20,40,0.28);
  background: rgba(255,255,255,0.03);
}

/* brand text */
.brand { display:flex; flex-direction:column; justify-content:center; }
.brand-title { font-size:34px; font-weight:700; margin:0; letter-spacing:-0.4px; }
.brand-sub { margin-top:4px; font-size:14.5px; color: rgba(255,255,255,0.92); }

/* accent line under brand (glass-ish) */
.accent {
  height:4px;
  width:140px;
  border-radius:6px;
  margin-top:10px;
  background: linear-gradient(90deg, rgba(255,255,255,0.95), rgba(255,255,255,0.65));
  box-shadow: 0 6px 16px rgba(59,130,246,0.18);
}

/* glass card style for content */
.card {
  background: var(--card-bg);
  padding: 24px;
  border-radius: 14px;
  border: 1px solid var(--glass-border);
  box-shadow: 0 8px 30px rgba(19,24,44,0.06);
  backdrop-filter: blur(6px) saturate(120%);
  -webkit-backdrop-filter: blur(6px) saturate(120%);
  margin-bottom: 20px;
}

/* section title */
.section-title {
  font-size:24px;
  font-weight:700;
  color: #0f2430;
  margin-bottom:12px;
}

/* list style */
.card ul { padding-left: 18px; margin: 8px 0 0 0; }
.card li { margin: 8px 0; }

/* subtle footer notice */
.footer-note { font-size:13px; color:#33414a; margin-top:8px; }

/* responsive tweaks */
@media (max-width:720px) {
  .brand-title { font-size:22px; }
  .brand-sub { font-size:13px; }
  .logo-compact { width:56px; height:56px; border-radius:10px;}
  .accent { width:110px; }
}
</style>
""", unsafe_allow_html=True)

# ---- HERO (compact logo + brand text) ----
logo_path = "Mina Store Logo.png"   # keep this file in same folder

st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="hero-inner">', unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 9])

with col1:
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

# ---- ABOUT US (glass card) ----
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.  
We offer a wide range of everyday essentials at fair prices:
<ul>
  <li>🎁 Gift items</li>
  <li>🛒 Grocery items</li>
  <li>🔧 Basic hardware tools</li>
  <li>📝 Xerox & printing services</li>
</ul>
<p class="footer-note">Our mission is to offer <b>quality products, great convenience, and friendly service</b> to everyone.</p>
</div>
""", unsafe_allow_html=True)

# ---- TIMINGS (glass card with a slightly tinted accent) ----
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
  <strong>🕘 Opens:</strong> 9:00 AM<br>
  <strong>🕖 Closes:</strong> 7:00 PM<br><br>
  Open daily for your convenience.
</div>
""", unsafe_allow_html=True)

st.success("✨ Use the sidebar to explore other pages!")
