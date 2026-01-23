import streamlit as st
import os

# --------------------------
# FIX IMAGE PATH
# --------------------------
BASE = os.path.dirname(os.path.abspath(__file__))           
IMG_DIR = os.path.abspath(os.path.join(BASE, "..", "images"))

def load_img(name):
    return os.path.join(IMG_DIR, name)

# --------------------------
# PAGE CONFIGimport streamlit as st
import os

# --------------------------
# FIX IMAGE PATH
# --------------------------
BASE = os.path.dirname(os.path.abspath(__file__))           
IMG_DIR = os.path.abspath(os.path.join(BASE, "..", "images"))

def load_img(name):
    return os.path.join(IMG_DIR, name)

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Products - Mina Store",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------
# RESPONSIVE + SOFT NEON CSS
# --------------------------
st.markdown("""
<style>

/* Title (original gradient) */
.title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff7a18, #af002d, #319197);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 25px;
}

/* Soft Neon Subtitle */
.subtitle-text {
    font-size: 22px;
    font-weight: 700;
    color: #1FA8FF;
    text-shadow: 
        0 0 3px rgba(31,168,255,0.6),
        0 0 6px rgba(31,168,255,0.3);
}

/* Grid Container */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 22px;
    padding: 10px;
}

/* Card Design */
.product-card {
    padding: 15px;
    border-radius: 18px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(7px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    transition: 0.3s;
    text-align: center;
}

.product-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

/* BIGGER Soft Neon Captions */
.caption {
    font-size: 22px;        /* Bigger text */
    font-weight: 800;       /* Bolder */
    margin-top: 12px;
    color: #39BFFF;
    text-shadow: 
        0 0 3px rgba(57,191,255,0.5),
        0 0 6px rgba(57,191,255,0.3);
}

/* Light mode softer glow */
@media (prefers-color-scheme: light) {
    .caption {
        text-shadow:
            0 0 2px rgba(57,191,255,0.4),
            0 0 4px rgba(57,191,255,0.2);
    }
}

/* Mobile Responsiveness */
@media (max-width: 480px) {
    .title {
        font-size: 30px;
    }
    .subtitle-text {
        font-size: 18px;
    }
    .product-card {
        padding: 12px;
        border-radius: 14px;
    }
    .caption {
        font-size: 19px;   /* Slightly smaller on phones */
    }
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# PAGE TITLE
# --------------------------
st.markdown("<div class='title'>🛍️ Mina Multi-Purpose Store</div>", unsafe_allow_html=True)

# Soft neon subtitle
st.markdown("<h3 class='subtitle-text'>Browse Categories:</h3>", unsafe_allow_html=True)

# --------------------------
# PRODUCT GRID RESPONSIVE
# --------------------------
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

categories = [
    ("gift.png", "Gift Items"),
    ("grocery.png", "Grocery"),
    ("hardware.png", "Hardware"),
    ("print.png", "Print & Xerox"),
]

for img, caption in categories:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(load_img(img), use_column_width=True)
    st.markdown(f"<div class='caption'>{caption}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
st.set_page_config(
    page_title="Products - Mina Store",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------
# RESPONSIVE + SOFT NEON CSS
# --------------------------
st.markdown("""
<style>

/* Title (original gradient) */
.title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff7a18, #af002d, #319197);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 25px;
}

/* Soft Neon Subtitle */
.subtitle-text {
    font-size: 22px;
    font-weight: 700;
    color: #1FA8FF;
    text-shadow: 
        0 0 3px rgba(31,168,255,0.6),
        0 0 6px rgba(31,168,255,0.3);
}

/* Grid Container */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 22px;
    padding: 10px;
}

/* Card Design */
.product-card {
    padding: 15px;
    border-radius: 18px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(7px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    transition: 0.3s;
    text-align: center;
}

.product-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

/* BIGGER Soft Neon Captions */
.caption {
    font-size: 22px;        /* Bigger text */
    font-weight: 800;       /* Bolder */
    margin-top: 12px;
    color: #39BFFF;
    text-shadow: 
        0 0 3px rgba(57,191,255,0.5),
        0 0 6px rgba(57,191,255,0.3);
}

/* Light mode softer glow */
@media (prefers-color-scheme: light) {
    .caption {
        text-shadow:
            0 0 2px rgba(57,191,255,0.4),
            0 0 4px rgba(57,191,255,0.2);
    }
}

/* Mobile Responsiveness */
@media (max-width: 480px) {
    .title {
        font-size: 30px;
    }
    .subtitle-text {
        font-size: 18px;
    }
    .product-card {
        padding: 12px;
        border-radius: 14px;
    }
    .caption {
        font-size: 19px;   /* Slightly smaller on phones */
    }
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# PAGE TITLE
# --------------------------
st.markdown("<div class='title'>🛍️ Mina Multi-Purpose Store</div>", unsafe_allow_html=True)

# Soft neon subtitle
st.markdown("<h3 class='subtitle-text'>Browse Categories:</h3>", unsafe_allow_html=True)

# --------------------------
# PRODUCT GRID RESPONSIVE
# --------------------------
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

categories = [
    ("gift.png", "Gift Items"),
    ("grocery.png", "Grocery"),
    ("hardware.png", "Hardware"),
    ("print.png", "Print & Xerox"),
]

for img, caption in categories:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(load_img(img), use_column_width=True)
    st.markdown(f"<div class='caption'>{caption}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
