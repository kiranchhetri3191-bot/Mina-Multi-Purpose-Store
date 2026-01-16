import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store",
                   page_icon="Mina Store Logo.png",
                   layout="wide")

# --------------------- STYLES: VIBRANT GRADIENT + ANIMATED BLOBS ---------------------
st.markdown("""
<style>
:root{
  --text: #072036;
  --card-glass: rgba(255,255,255,0.10);
  --card-border: rgba(255,255,255,0.14);
  --accent-white: rgba(255,255,255,0.95);
}

/* page background: vivid gradient */
body {
  background: radial-gradient(circle at 10% 10%, rgba(255,255,255,0.03), transparent 10%),
              linear-gradient(135deg, #00c6ff 0%, #0072ff 40%, #ff4d6d 100%);
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
  color: var(--text);
  -webkit-font-smoothing: antialiased;
}

/* Add animated floating blobs to create lively background */
.appview-container .main > div {
  position: relative;
  overflow: visible;
}

.bg-blob {
  position: absolute;
  filter: blur(40px);
  opacity: 0.18;
  pointer-events: none;
  mix-blend-mode: screen;
  z-index: 0;
}

/* blob styles & animation */
#blob1 { width: 420px; height: 420px; left: -80px; top: -60px; background: radial-gradient(circle, #ffffff 0%, rgba(255,255,255,0) 60%); animation: floatA 9s ease-in-out infinite; }
#blob2 { width: 380px; height: 380px; right: -100px; top: -20px; background: radial-gradient(circle, #ffd3e0 0%, rgba(255,255,255,0) 60%); animation: floatB 11s ease-in-out infinite; }
#blob3 { width: 520px; height: 520px; left: 30%; bottom: -220px; background: radial-gradient(circle, rgba(0,0,0,0.06), rgba(0,0,0,0)); animation: floatA 13s ease-in-out infinite; }

@keyframes floatA {
  0% { transform: translateY(0) translateX(0) rotate(0deg); }
  50% { transform: translateY(-30px) translateX(18px) rotate(8deg); }
  100% { transform: translateY(0) translateX(0) rotate(0deg); }
}
@keyframes floatB {
  0% { transform: translateY(0) translateX(0) rotate(0deg); }
  50% { transform: translateY(22px) translateX(-18px) rotate(-6deg); }
  100% { transform: translateY(0) translateX(0) rotate(0deg); }
}

/* HERO: compact logo + title block over gradient (front) */
.hero {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  margin: 18px auto 30px auto;
  padding: 22px;
  display: flex;
  gap: 20px;
  align-items: center;
  border-radius: 14px;
  background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
  border: 1px solid rgba(255,255,255,0.12);
  box-shadow: 0 12px 40px rgba(2,8,23,0.26);
}

/* small compact logo */
.logo-compact {
  width: 72px;
  height: 72px;
  border-radius: 12px;
  object-fit: cover;
  border: 2px solid rgba(255,255,255,0.15);
  box-shadow: 0 6px 18px rgba(2,8,23,0.3);
}

/* title area */
.title-block { display:flex; flex-direction:column; gap:6px; }
.title-main {
  font-size: 34px;
  font-weight: 800;
  color: white;
  text-shadow: 0 4px 18px rgba(2,8,23,0.45);
  margin:0;
}
.title-sub {
  font-size: 15px;
  color: rgba(255,255,255,0.92);
  margin:0;
  letter-spacing: 0.1px;
}

/* accent underline */
.accent-line {
  width: 160px;
  height: 4px;
  border-radius: 6px;
  margin-top: 8px;
  background: linear-gradient(90deg, rgba(255,255,255,0.96), rgba(255,255,255,0.55));
  box-shadow: 0 8px 30px rgba(255,255,255,0.06);
}

/* content cards (glass-like but tinted) */
.card {
  position: relative;
  z-index: 2;
  max-width: 1100px;
  margin: 18px auto;
  padding: 26px;
  border-radius: 14px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.12);
  box-shadow: 0 12px 40px rgba(2,8,23,0.18);
  backdrop-filter: blur(6px) saturate(140%);
}

/* headings inside */
.section-title { font-size: 22px; font-weight: 700; color: #051427; margin-bottom: 8px; }

/* list style */
.card ul { margin-left: 18px; color: #041827; }
.card li { margin: 8px 0; }

/* footer-ish note */
.footer-note { color: rgba(2,8,23,0.72); font-size: 14px; margin-top: 8px; }

/* responsiveness */
@media (max-width: 780px) {
  .hero { flex-direction: row; gap: 12px; padding: 16px; }
  .title-main { font-size: 22px; }
  .logo-compact { width: 56px; height: 56px; border-radius: 10px; }
  .accent-line { width: 110px; }
  .card { padding: 18px; margin: 14px 12px; border-radius: 12px; }
}
</style>
""", unsafe_allow_html=True)

# --------------------- BACKGROUND BLOBS (absolute positioned) ---------------------
st.markdown("""
<div class="bg-blob" id="blob1"></div>
<div class="bg-blob" id="blob2"></div>
<div class="bg-blob" id="blob3"></div>
""", unsafe_allow_html=True)

# --------------------- HERO (logo + title) ---------------------
logo_path = "Mina Store Logo.png"

st.markdown('<div class="hero">', unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 9])

with col1:
    st.image(logo_path, width=72, use_column_width=False)

with col2:
    st.markdown("""
      <div class="title-block">
        <div class="title-main">Mina Multi-Purpose Store</div>
        <div class="title-sub">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        <div class="accent-line"></div>
      </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------- ABOUT CARD ---------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<div class='section-title'>About Us</div>", unsafe_allow_html=True)
st.markdown("""
We are a trusted neighborhood store located <b>near Pragati Club, Birpara, West Bengal</b>.
We offer a wide range of everyday essentials at fair prices:
<ul>
  <li>🎁 Gift items</li>
  <li>🛒 Grocery items</li>
  <li>🔧 Basic hardware tools</li>
  <li>📝 Xerox & printing services</li>
</ul>
<p class="footer-note">Our mission: <b>quality products, great convenience, and friendly service</b>.</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- TIMINGS CARD ---------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<div class='section-title'>Store Timings</div>", unsafe_allow_html=True)
st.markdown("""
<strong>🕘 Opens:</strong> 9:00 AM<br>
<strong>🕖 Closes:</strong> 7:00 PM<br><br>
Open every day for your convenience.
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# small CTA / friendly note
st.markdown("""
<div style="max-width:1100px; margin:10px auto; text-align:center;">
  <span style="background:rgba(255,255,255,0.06); padding:10px 18px; border-radius:999px; color:white; border:1px solid rgba(255,255,255,0.08); box-shadow:0 6px 20px rgba(2,8,23,0.18);">
    ✨ Add our site to your LinkedIn or share the link — fully free & safe.
  </span>
</div>
""", unsafe_allow_html=True)
