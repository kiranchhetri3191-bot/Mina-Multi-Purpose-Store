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
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Mina Multi-Purpose Store",
    page_icon="favicon_v3.png",
    layout="wide"
)


# --------------------------
# RESPONSIVE + SOFT NEON CSS
# --------------------------
st.markdown("""
<style>

/* ==========================
   TITLE
   ========================== */
.title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff7a18, #af002d, #319197);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 25px;
}


/* ==========================
   SOFT NEON SUBTITLE
   ========================== */
.subtitle-text {
    font-size: 22px;
    font-weight: 700;
    color: #1FA8FF;
    text-shadow:
        0 0 3px rgba(31,168,255,0.6),
        0 0 6px rgba(31,168,255,0.3);
}


/* ==========================
   CLICKABLE NAVIGATION ARROW
   ========================== */
.nav-arrow {
    position: fixed;
    left: 18px;
    top: 95px;

    z-index: 999999;

    width: 55px;
    height: 55px;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #1677ff,
        #00c6ff
    );

    color: white !important;

    font-size: 32px;
    font-weight: 900;

    text-align: center;
    line-height: 55px;

    text-decoration: none !important;

    box-shadow:
        0 4px 15px rgba(0,150,255,0.45);

    transition: all 0.25s ease;
}


/* Arrow hover effect */
.nav-arrow:hover {
    transform: scale(1.12);

    box-shadow:
        0 6px 25px rgba(0,150,255,0.70);
}


/* ==========================
   GRID CONTAINER
   ========================== */
.grid-container {
    display: grid;
    grid-template-columns: repeat(
        auto-fill,
        minmax(180px, 1fr)
    );
    gap: 22px;
    padding: 10px;
}


/* ==========================
   CARD DESIGN
   ========================== */
.product-card {
    padding: 15px;

    border-radius: 18px;

    background: rgba(255,255,255,0.15);

    border: 1px solid rgba(255,255,255,0.2);

    backdrop-filter: blur(7px);

    box-shadow:
        0 4px 15px rgba(0,0,0,0.15);

    transition: 0.3s;

    text-align: center;
}


.product-card:hover {
    transform: scale(1.05);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.25);
}


/* ==========================
   CAPTION
   ========================== */
.caption {
    font-size: 22px;
    font-weight: 800;

    margin-top: 12px;

    color: #39BFFF;

    text-shadow:
        0 0 3px rgba(57,191,255,0.5),
        0 0 6px rgba(57,191,255,0.3);
}


/* ==========================
   DESCRIPTION
   ========================== */
.desc {
    font-size: 14px;

    color: #e8f7ff;

    margin-top: 4px;

    opacity: 0.9;
}


/* ==========================
   LIGHT MODE
   ========================== */
@media (prefers-color-scheme: light) {

    .caption {
        text-shadow:
            0 0 2px rgba(57,191,255,0.4),
            0 0 4px rgba(57,191,255,0.2);
    }

    .desc {
        color: #0b4c66;
    }
}


/* ==========================
   MOBILE RESPONSIVENESS
   ========================== */
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
        font-size: 19px;
    }

    .desc {
        font-size: 13px;
    }

    /* Smaller arrow on mobile */
    .nav-arrow {
        width: 45px;
        height: 45px;

        line-height: 45px;

        font-size: 26px;

        left: 12px;
        top: 85px;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------
# CLICKABLE NEXT PAGE ARROW
# --------------------------
# Change /Gift_Items if your
# next page has another filename.
st.markdown(
    """
    <a
        class="nav-arrow"
        href="/Gift_Items"
        target="_self"
        title="Go to Gift Items"
    >
        ➜
    </a>
    """,
    unsafe_allow_html=True
)


# --------------------------
# PAGE TITLE
# --------------------------
st.markdown(
    "<div class='title'>🛍️ Mina Multi-Purpose Store</div>",
    unsafe_allow_html=True
)


# --------------------------
# SUBTITLE
# --------------------------
st.markdown(
    "<h3 class='subtitle-text'>Browse Categories:</h3>",
    unsafe_allow_html=True
)


# --------------------------
# PRODUCT GRID
# --------------------------
st.markdown(
    "<div class='grid-container'>",
    unsafe_allow_html=True
)


# --------------------------
# CATEGORIES
# --------------------------
categories = [

    (
        "gift.png",
        "Gift Items",
        "Unique and thoughtful gifts for all occasions."
    ),

    (
        "grocery.png",
        "Grocery",
        "Daily essentials and quality grocery products."
    ),

    (
        "hardware.png",
        "Hardware",
        "Reliable tools and hardware items for home needs."
    ),

    (
        "print.png",
        "Print & Xerox",
        "Xerox and Color Print Services."
    ),

]


# --------------------------
# DISPLAY PRODUCTS
# --------------------------
for img, caption, desc in categories:

    st.markdown(
        "<div class='product-card'>",
        unsafe_allow_html=True
    )

    image_path = load_img(img)

    # Check whether image exists
    if os.path.exists(image_path):

        st.image(
            image_path,
            width="stretch"
        )

    else:

        st.warning(
            f"Image not found: {img}"
        )

    st.markdown(
        f"<div class='caption'>{caption}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='desc'>{desc}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# --------------------------
# CLOSE GRID
# --------------------------
st.markdown(
    "</div>",
    unsafe_allow_html=True
)
