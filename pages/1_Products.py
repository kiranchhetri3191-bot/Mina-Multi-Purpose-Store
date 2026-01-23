st.markdown("""
<style>

body, .main {
    background-color: transparent !important;
}

/* ──────────────────────────────────────────────── */
/*            NEON PREMIUM V2 — TITLE               */
/* ──────────────────────────────────────────────── */
.title {
    font-size: 50px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 5px;
    color: #00f2ff;
    text-shadow:
        0 0 10px #00eaff,
        0 0 25px #00ccff,
        0 0 40px #0099cc,
        0 0 60px #0077aa;
    animation: glowPulse 2.5s infinite ease-in-out;
}

@keyframes glowPulse {
    0% { text-shadow: 0 0 10px #00eaff, 0 0 30px #0099cc; }
    50% { text-shadow: 0 0 25px #00eaff, 0 0 50px #00ccff, 0 0 80px #0088cc; }
    100% { text-shadow: 0 0 10px #00eaff, 0 0 30px #0099cc; }
}

/* SUBTITLE */
.subtitle {
    font-size: 22px;
    text-align: center;
    color: #7fe9ff;
    margin-bottom: 20px;
    text-shadow: 0 0 10px #00ccff;
    animation: fadeIn 1.2s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* NEON DIVIDER */
.neon-divider {
    height: 3px;
    width: 60%;
    margin: 10px auto 25px;
    background: linear-gradient(90deg, transparent, #00eaff, transparent);
    box-shadow: 0 0 15px #00eaff;
    border-radius: 50px;
}

/* GRID */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 22px;
    padding: 10px;
}

/* ──────────────────────────────────────────────── */
/*            NEON CARD PREMIUM V2                  */
/* ──────────────────────────────────────────────── */
.product-card {
    padding: 15px;
    border-radius: 20px;
    background: rgba(255,255,255,0.06);
    border: 2px solid rgba(0, 255, 255, 0.25);
    backdrop-filter: blur(12px);
    position: relative;
    perspective: 1000px;
    transition: transform 0.35s ease, box-shadow 0.35s ease;
}

/* Neon border animation */
.product-card::before {
    content: "";
    position: absolute;
    inset: -2px;
    background: linear-gradient(90deg, #00eaff, #0077ff, #00eaff);
    z-index: -1;
    border-radius: 20px;
    filter: blur(8px);
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
}

/* Hover premium effects */
.product-card:hover {
    transform: scale(1.07) rotateX(6deg) rotateY(-6deg);
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.5),
                0 0 50px rgba(0, 255, 255, 0.3);
}

.product-card:hover::before {
    opacity: 1;
}

/* Caption */
.caption {
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
    color: #adf3ff;
    text-shadow: 0 0 6px #00dfff;
}

/* CLICK RIPPLE EFFECT */
.product-card:active {
    animation: clickRipple 0.4s ease-out;
}

@keyframes clickRipple {
    0% { box-shadow: 0 0 20px #00eaff; }
    100% { box-shadow: 0 0 5px #00eaff; }
}

/* MOBILE */
@media(max-width: 480px) {
    .title { font-size: 36px; }
    .subtitle { font-size: 18px; }
    .caption { font-size: 16px; }
}

</style>
""", unsafe_allow_html=True)
