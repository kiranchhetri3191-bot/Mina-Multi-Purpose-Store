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
        font-size: 19px;
    }

    .desc {
        font-size: 13px;
    }
}


/* =====================================================
   NEXT PAGE BUTTON
   ===================================================== */

.next-page-section {
    text-align: center;
    margin-top: 45px;
    margin-bottom: 30px;
}

.next-page-title {
    font-size: 24px;
    font-weight: 800;
    color: #008cff;
    margin-bottom: 8px;
}

.next-page-subtitle {
    font-size: 15px;
    color: #666;
    margin-bottom: 18px;
}


/* Make Streamlit page link look like a button */
.next-page-section [data-testid="stPageLink-NavLink"] {
    display: inline-flex !important;
    justify-content: center !important;
    align-items: center !important;

    width: 280px !important;

    padding: 14px 25px !important;

    border-radius: 30px !important;

    background: linear-gradient(
        90deg,
        #007bff,
        #00c6ff
    ) !important;

    color: white !important;

    font-size: 17px !important;
    font-weight: 900 !important;

    text-decoration: none !important;

    box-shadow:
        0 6px 20px rgba(0,140,255,0.35) !important;

    transition: all 0.3s ease !important;
}


/* Hover effect */
.next-page-section [data-testid="stPageLink-NavLink"]:hover {
    transform: translateY(-4px) scale(1.03);

    box-shadow:
        0 10px 30px rgba(0,140,255,0.55) !important;
}


/* Mobile button */
@media (max-width: 480px) {

    .next-page-section [data-testid="stPageLink-NavLink"] {
        width: 85% !important;
        font-size: 15px !important;
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


# =====================================================
# DIRECT NEXT PAGE BUTTON
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

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------
# STREAMLIT PAGE LINK
# --------------------------
st.page_link(
    "pages/Contact_Location.py",
    label="📍  VISIT CONTACT & LOCATION  ➜",
    icon="➡️"
)
```

**Important:** Because `1_Products.py` and `Contact_Location.py` are both inside your `pages` folder, if Streamlit gives an error with `"pages/Contact_Location.py"`, change that one line to:

```python
st.page_link(
    "Contact_Location.py",
    label="📍  VISIT CONTACT & LOCATION  ➜",
    icon="➡️"
)
```

The rest of the code does not need to change.
