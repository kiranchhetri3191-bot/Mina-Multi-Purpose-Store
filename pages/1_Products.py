# --------------------------
# PRODUCT GRID
# --------------------------
st.markdown(
    "<div class='grid-container'>",
    unsafe_allow_html=True
)

for img, caption, desc in categories:

    # Apply category filter
    if selected_category != "All Categories":

        if caption not in selected_category:
            continue

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

st.markdown("</div>", unsafe_allow_html=True)
