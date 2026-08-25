```python
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

/* Title */
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

/* Bigger Soft Neon Captions */
.caption {
    font-size: 22px;
    font-weight: 800;
    margin-top: 12px;
    color: #39BFFF;
    text-shadow:
        0 0 3px rgba(57,191,255,0.5),
        0 0 6px rgba(57,191,255,0.3);
}

/* Description */
.desc {
    font-size: 14px;
    color: #e8f7ff;
    margin-top: 4px;
    opacity: 0.9;
}

/* Light mode softer glow */
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


/* =====================================================
   PREMIUM NEXT PAGE BUTTON
   ===================================================== */

.next-page-section {
    text-align: center;
    margin-top: 45px;
    margin-bottom: 30px;
}

.next-page-title {
    font-size: 25px;
    font-weight: 800;
    color: #008cff;
    margin-bottom: 6px;
}

.next-page-subtitle {
    font-size: 15px;
    color: #666;
    margin-bottom: 18px;
}

.next-page-button {
    display: inline-block;

    padding: 14px 30px;

    border-radius: 35px;

    background: linear-gradient(
        90deg,
        #007bff,
        #00c6ff
    );

    color: white !important;

    font-size: 18px;
    font-weight: 900;

    text-decoration: none !important;

    box-shadow:
        0 6px 20px rgba(0,140,255,0.35);

    transition: all 0.3s ease;

    animation: nextButtonPulse 2s infinite;
}

.next-page-button:hover {
    transform: translateY(-4px) scale(1.05);

    box-shadow:
        0 10px 30px rgba(0,140,255,0.55);
}

.next-page-arrow {
    display: inline-block;

    margin-left: 8px;

    font-size: 22px;

    animation: nextArrowMove 1s infinite;
}


/* Button Glow Animation */
@keyframes nextButtonPulse {

    0%, 100% {
        box-shadow:
            0 6px 20px rgba(0,140,255,0.30);
    }

    50% {
        box-shadow:
            0 8px 30px rgba(0,140,255,0.55);
    }

}


/* Arrow Animation */
@keyframes nextArrowMove {

    0%, 100% {
        transform: translateX(0);
    }

    50% {
        transform: translateX(7px);
    }

}


/* --------------------------
   Mobile Responsiveness
   -------------------------- */
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

    .next-page-title {
        font-size: 21px;
    }

    .next-page-subtitle {
        font-size: 13px;
    }

    .next-page-button {
        padding: 12px 22px;
        font-size: 16px;
    }

}

</style>
""", unsafe_allow_html=True)


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
        st.warning(f"Image not found: {img}")

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


# =====================================================
# PREMIUM NEXT PAGE SECTION
# =====================================================

st.markdown(
    """
    <div class="next-page-section">

        <div class="next-page-title">
            👇 Want to know more?
        </div>

        <div class="next-page-subtitle">
            Visit our next page for contact & location
        </div>

        <a
            href="/Contact_Location"
            target="_self"
            class="next-page-button"
        >
            VISIT OUR NEXT PAGE
            <span class="next-page-arrow">➜</span>
        </a>

    </div>
    """,
    unsafe_allow_html=True
)
```
