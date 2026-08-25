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
