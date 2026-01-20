import streamlit as st

st.set_page_config(page_title="Mina Multi-Purpose Store", page_icon="Mina Store Logo.png", layout="wide")

# -------------------------------------------------
# Detect Streamlit Theme (Dark / Light)
# -------------------------------------------------
theme_bg = st.get_option("theme.backgroundColor")
is_dark = theme_bg and theme_bg.lower() in ["#0e1117", "#000000", "#1e1e1e"]

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>

.header-wrapper {
    position: relative;
    height: 115px;
}

/* BLACK NEON TEXT (Shown only in Light Mode) */
.text-light {
    position: absolute;
    top: 0;
    left: 0;
    color: black;
    font-size: 42px;
    font-weight: 800;
    text-shadow:
        0px 0px 6px rgba(0,0,0,0.45),
        0px 0px 12px rgba(0,0,0,0.30);
}

/* WHITE COPY TEXT (Shown only in Dark Mode) */
.text-dark {
    position: absolute;
    top: 0;
    left: 0;
    color: white;
    font-size: 42px;
    font-weight: 800;
    text-shadow:
        0px 0px 10px rgba(0, 60, 160, 0.80),
        0px 0px 20px rgba(0, 60, 160, 0.60);
}

/* Subtitle (same logic) */
.sub-light {
    position: absolute;
    top: 55px;
    left: 0;
    color: black;
    font-size: 22px;
    font-weight: 500;
    text-shadow:
        0px 0px 5px rgba(0,0,0,0.45),
        0px 0px 8px rgba(0,0,0,0.25);
}

.sub-dark {
    position: absolute;
    top: 55px;
    left: 0;
    color: white;
    font-size: 22px;
    font-weight: 500;
    text-shadow:
        0px 0px 10px rgba(0, 60, 160, 0.80),
        0px 0px 20px rgba(0, 60, 160, 0.60);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown('<div class="header-box" style="background:#0d2340;padding:40px;border-radius:20px;">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.image("Mina Store Logo.png", width=145)

with col2:
    st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)

    # Light Mode (Black Neon Text)
    if not is_dark:
        st.markdown("""
            <div class="text-light">Mina Multi-Purpose Store</div>
            <div class="sub-light">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        """, unsafe_allow_html=True)

    # Dark Mode (White Text Copy)
    else:
        st.markdown("""
            <div class="text-dark">Mina Multi-Purpose Store</div>
            <div class="sub-dark">Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox</div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
