# --------------------------
# RESPONSIVE CSS
# --------------------------
st.markdown("""
<style>

/* NEON BLUE TITLE */
.title {
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 25px;
    color: #00C8FF !important;
    text-shadow: 
        0 0 8px #00C8FF,
        0 0 12px #00AEDD,
        0 0 20px #0088BB;
}

/* SUBTITLE */
.subtitle {
    font-size: 22px;
    font-weight: 600;
    text-align: center;
    margin-bottom: 20px;
    color: #4FD9FF;
    text-shadow:
        0 0 6px #00C8FF,
        0 0 10px #0095CC;
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

/* Caption */
.caption {
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
}

/* Mobile Responsiveness */
@media (max-width: 480px) {
    .title {
        font-size: 30px;
    }
    .subtitle {
        font-size: 18px;
    }
    .product-card {
        padding: 12px;
        border-radius: 14px;
    }
    .caption {
        font-size: 16px;
    }
}

</style>
""", unsafe_allow_html=True)
