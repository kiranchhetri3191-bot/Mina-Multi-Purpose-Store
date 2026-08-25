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




# --------------------------
# CUSTOMER REVIEWS
# --------------------------

st.markdown("---")

st.markdown(
    "<div class='title'>⭐ Customer Reviews</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 class='subtitle-text'>What Our Customers Say</h3>",
    unsafe_allow_html=True
)

# Sample reviews
reviews = [
    (
        "Rahul",
        "⭐⭐⭐⭐⭐",
        "Excellent service! Good quality products and very friendly staff."
    ),
    (
        "Priya",
        "⭐⭐⭐⭐⭐",
        "Great experience. I found everything I needed at a reasonable price."
    ),
    (
        "Amit",
        "⭐⭐⭐⭐",
        "Good collection and quick service. Will definitely visit again."
    ),
]

# Display existing reviews
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

for name, rating, review in reviews:

    st.markdown(
        f"""
        <div class='product-card'>
            <div class='caption'>{rating}</div>
            <div class='desc' style='font-size:18px; margin-top:10px;'>
                "{review}"
            </div>
            <div style='margin-top:12px; font-weight:700; color:#1FA8FF;'>
                — {name}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------
# LEAVE A REVIEW
# --------------------------

st.markdown("---")

st.markdown(
    "<h3 class='subtitle-text'>💬 Leave Your Review</h3>",
    unsafe_allow_html=True
)

customer_name = st.text_input(
    "Your Name",
    placeholder="Enter your name"
)

customer_rating = st.selectbox(
    "Your Rating",
    [
        "⭐⭐⭐⭐⭐ Excellent",
        "⭐⭐⭐⭐ Very Good",
        "⭐⭐⭐ Good",
        "⭐⭐ Average",
        "⭐ Poor"
    ]
)

customer_review = st.text_area(
    "Your Review",
    placeholder="Tell us about your experience..."
)

if st.button("⭐ Submit Review"):

    if customer_name and customer_review:

        st.success(
            f"Thank you {customer_name}! ❤️ "
            "Your review has been submitted."
        )

    else:

        st.warning(
            "Please enter your name and review before submitting."
        )
