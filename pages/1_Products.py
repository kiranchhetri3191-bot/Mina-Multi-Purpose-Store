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
   SUBTITLE
   ========================== */
.subtitle-text {
    font-size: 22px;
    font-weight: 700;
    color: #1FA8FF;
    text-shadow:
        0 0 3px rgba(31,168,255,0.6),
        0 0 6px rgba(31,168,255,0.3);
}


/* =====================================================
   NEXT PAGE BUTTON
   ===================================================== */

.next-page-button {
    position: fixed;

    left: 18px;
    top: 95px;

    width: 58px;
    height: 58px;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #006eff,
        #00c6ff
    );

    color: white !important;

    font-size: 34px;
    font-weight: 900;

    text-align: center;
    line-height: 58px;

    text-decoration: none !important;

    z-index: 999999;

    box-shadow:
        0 0 10px rgba(0,174,255,0.7),
        0 0 25px rgba(0,174,255,0.45);

    transition: all 0.25s ease;

    animation: arrowPulse 1.8s infinite;
}


/* Button hover */
.next-page-button:hover {
    transform: scale(1.15);

    box-shadow:
        0 0 15px rgba(0,174,255,0.9),
        0 0 35px rgba(0,174,255,0.7);
}


/* ==========================
   NEXT PAGE LABEL
   ========================== */

.next-page-label {
    position: fixed;

    left: 88px;
    top: 101px;

    z-index: 999998;

    background: rgba(0, 119, 255, 0.95);

    color: white;

    padding: 10px 18px;

    border-radius: 25px;

    font-size: 16px;
    font-weight: 800;

    letter-spacing: 0.5px;

    box-shadow:
        0 4px 15px rgba(0,100,255,0.35);

    white-space: nowrap;

    animation: labelPulse 1.8s infinite;
}


/* Little pointing arrow */
.next-page-label::before {
    content: "←";

    font-size: 25px;
    font-weight: 900;

    margin-right: 7px;

    vertical-align: middle;
}


/* ==========================
   ANIMATION
   ========================== */

@keyframes arrowPulse {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.08);
    }

}


@keyframes labelPulse {

    0%, 100% {
        opacity: 0.9;
    }

    50% {
        opacity: 1;
        transform: translateX(4px);
    }

}


/* ==========================
   GRID CONTAINER
   ========================== */

.grid-container {
    display: grid;

    grid-template-columns:
        repeat(auto-fill, minmax(180px, 1fr));

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
   MOBILE
   ========================== */

@media (max-width: 600px) {

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


    /* Smaller navigation button */
    .next-page-button {

        width: 48px;
        height: 48px;

        line-height: 48px;

        font-size: 27px;

        left: 12px;
        top: 85px;
    }


    /* Smaller label */
    .next-page-label {

        left: 70px;
        top: 88px;

        padding: 8px 12px;

        font-size: 13px;
    }

    .next-page-label::before {
        font-size: 20px;
    }

}

</style>
""", unsafe_allow_html=True)


# =====================================================
# NEXT PAGE NAVIGATION
# =====================================================

# Change /Gift_Items to your actual next page URL
st.markdown(
    """
    <a
        class="next-page-button"
        href="/Gift_Items"
        target="_self"
        title="Go to Next Page"
    >
        ➜
    </a>

    <div class="next-page-label">
        CLICK HERE FOR NEXT PAGE
    </div>
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
