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


# ==========================================================
# CSS
# ==========================================================
st.markdown("""
<style>

/* ==========================================================
   MAIN BACKGROUND
   ========================================================== */

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 10% 10%, rgba(0,174,255,0.08), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(255,122,24,0.08), transparent 25%),
        linear-gradient(135deg, #ffffff 0%, #f4fbff 50%, #ffffff 100%);
}


/* ==========================================================
   TITLE
   ========================================================== */

.title {
    font-size: 46px;
    font-weight: 900;
    text-align: center;

    background: linear-gradient(
        90deg,
        #007bff,
        #00bfff,
        #ff7a18,
        #007bff
    );

    background-size: 300%;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: titleGlow 5s ease infinite;

    margin-top: 15px;
    margin-bottom: 8px;
}


@keyframes titleGlow {
    0% {
        background-position: 0%;
    }

    50% {
        background-position: 100%;
    }

    100% {
        background-position: 0%;
    }
}


/* ==========================================================
   WELCOME TEXT
   ========================================================== */

.welcome {
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: #477083;
    margin-bottom: 30px;
}


/* ==========================================================
   SECTION TITLE
   ========================================================== */

.subtitle-text {
    font-size: 24px;
    font-weight: 800;
    color: #008cff;

    text-shadow:
        0 0 3px rgba(0,140,255,0.25);

    margin-top: 10px;
}


/* ==========================================================
   PRODUCT GRID
   ========================================================== */

.grid-container {
    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(210px, 1fr));

    gap: 25px;

    padding: 15px 5px 10px 5px;
}


/* ==========================================================
   PRODUCT CARD
   ========================================================== */

.product-card {
    padding: 18px;

    border-radius: 22px;

    background: rgba(255,255,255,0.75);

    border: 1px solid rgba(0,140,255,0.12);

    backdrop-filter: blur(10px);

    box-shadow:
        0 8px 25px rgba(0,90,150,0.10);

    text-align: center;

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;

    min-height: 300px;
}


.product-card:hover {
    transform: translateY(-8px) scale(1.02);

    box-shadow:
        0 18px 40px rgba(0,100,180,0.18);
}


/* ==========================================================
   PRODUCT IMAGE
   ========================================================== */

.product-card img {
    border-radius: 15px;
}


/* ==========================================================
   PRODUCT CAPTION
   ========================================================== */

.caption {
    font-size: 23px;
    font-weight: 900;

    margin-top: 15px;

    color: #008cff;

    text-shadow:
        0 0 4px rgba(0,140,255,0.20);
}


/* ==========================================================
   DESCRIPTION
   ========================================================== */

.desc {
    font-size: 14px;

    color: #426474;

    margin-top: 7px;

    line-height: 1.5;
}


/* ==========================================================
   DIVIDER
   ========================================================== */

.cool-divider {
    width: 80%;
    height: 2px;

    margin: 45px auto 25px auto;

    background: linear-gradient(
        90deg,
        transparent,
        #00aaff,
        transparent
    );

    opacity: 0.5;
}


/* ==========================================================
   NEXT PAGE PROMO BOX
   ========================================================== */

.next-box {
    text-align: center;

    margin: 25px auto 10px auto;

    padding: 30px 20px;

    max-width: 800px;

    border-radius: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(0,140,255,0.10),
            rgba(0,200,255,0.06)
        );

    border: 1px solid rgba(0,140,255,0.18);

    box-shadow:
        0 10px 35px rgba(0,120,200,0.10);
}


/* ==========================================================
   NEXT PAGE HEADING
   ========================================================== */

.next-title {
    font-size: 28px;

    font-weight: 900;

    color: #0077dd;

    margin-bottom: 5px;
}


.next-description {
    font-size: 16px;

    color: #527080;

    margin-bottom: 18px;
}


/* ==========================================================
   ANIMATED ARROW
   ========================================================== */

.next-arrow {
    font-size: 42px;

    color: #008cff;

    font-weight: 900;

    display: inline-block;

    animation: arrowMove 1.1s infinite;

    margin-right: 8px;
}


@keyframes arrowMove {

    0%, 100% {
        transform: translateX(0);
    }

    50% {
        transform: translateX(10px);
    }
}


/* ==========================================================
   STREAMLIT NEXT PAGE BUTTON
   ========================================================== */

[data-testid="stPageLink-NavLink"] {

    display: flex !important;

    justify-content: center !important;

    align-items: center !important;

    width: 280px !important;

    margin: 0 auto !important;

    padding: 15px 25px !important;

    border-radius: 35px !important;

    background:
        linear-gradient(
            90deg,
            #007bff,
            #00bfff
        ) !important;

    color: white !important;

    font-size: 18px !important;

    font-weight: 900 !important;

    text-decoration: none !important;

    box-shadow:
        0 8px 25px rgba(0,140,255,0.30) !important;

    transition: all 0.3s ease !important;
}


[data-testid="stPageLink-NavLink"]:hover {

    transform: translateY(-4px) scale(1.03);

    box-shadow:
        0 12px 32px rgba(0,140,255,0.45) !important;
}


/* ==========================================================
   SMALL ATTENTION TEXT
   ========================================================== */

.scroll-hint {

    text-align: center;

    font-size: 13px;

    color: #6d8794;

    margin-top: 12px;
}


/* ==========================================================
   MOBILE
   ========================================================== */

@media (max-width: 600px) {

    .title {
        font-size: 32px;
    }

    .welcome {
        font-size: 15px;
    }

    .subtitle-text {
        font-size: 20px;
    }

    .product-card {
        min-height: 260px;
    }

    .caption {
        font-size: 20px;
    }

    .next-title {
        font-size: 23px;
    }

    .next-description {
        font-size: 14px;
    }

    [data-testid="stPageLink-NavLink"] {
        width: 85% !important;
        font-size: 16px !important;
    }

}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# PAGE TITLE
# ==========================================================

st.markdown(
    "<div class='title'>🛍️ Mina Multi-Purpose Store</div>",
    unsafe_allow_html=True
)


# ==========================================================
# WELCOME MESSAGE
# ==========================================================

st.markdown(
    """
    <div class="welcome">
        Everything you need, all in one place ✨
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# CATEGORY TITLE
# ==========================================================

st.markdown(
    "<div class='subtitle-text'>🛒 Explore Our Categories</div>",
    unsafe_allow_html=True
)


# ==========================================================
# PRODUCT GRID
# ==========================================================

st.markdown(
    "<div class='grid-container'>",
    unsafe_allow_html=True
)


# ==========================================================
# CATEGORIES
# ==========================================================

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


# ==========================================================
# DISPLAY PRODUCTS
# ==========================================================

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


# ==========================================================
# CLOSE GRID
# ==========================================================

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ==========================================================
# NEXT PAGE SECTION
# ==========================================================

st.markdown(
    "<div class='cool-divider'></div>",
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="next-box">

        <div class="next-title">
            ✨ Want to Know More About Us?
        </div>

        <div class="next-description">
            📍 Visit our next page for our location,
            contact details and more information.
        </div>

        <div class="next-arrow">
            ➜
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# NEXT PAGE BUTTON
# ==========================================================

st.page_link(
    "pages/Contact_Location.py",
    label="VISIT OUR NEXT PAGE  ➜",
    icon="🌟"
)


# ==========================================================
# FINAL HINT
# ==========================================================

st.markdown(
    """
    <div class="scroll-hint">
        👆 Click the button above to continue
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <br>

    <div style="
        text-align:center;
        color:#78909c;
        font-size:13px;
        margin-top:25px;
        padding-bottom:15px;
    ">
        🛍️ Mina Multi-Purpose Store
        <br>
        Your one-stop destination for everyday needs
    </div>
    """,
    unsafe_allow_html=True
)
```
