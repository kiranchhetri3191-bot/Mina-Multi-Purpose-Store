st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* Soft Gradient Background (Professional) */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #dde6ff, #cfdaf7, #e5ecff);
    z-index: -2;
}

/* HEADER WRAPPER – DARKER & MORE PREMIUM */
.header-box {
    background: rgba(5, 12, 28, 0.82);  /* darker navy */
    backdrop-filter: blur(14px);
    padding: 42px 55px;
    border-radius: 26px;
    margin-bottom: 40px;

    /* darker, stronger neon outline */
    border: 1px solid rgba(0, 112, 230, 0.55);
    box-shadow:
        0px 0px 18px rgba(0, 112, 230, 0.28),
        0px 10px 26px rgba(0,0,0,0.45);

    animation: fadeDown 0.9s ease;
}

@keyframes fadeDown {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* FLEX */
.header-flex {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 38px;
}

/* LOGO — Slightly darker shadow */
.header-logo img {
    width: 145px;
    border-radius: 14px;
    box-shadow: 
        0px 4px 14px rgba(0,0,0,0.45),
        0px 0px 12px rgba(80,150,255,0.25);
}

/* MAIN TITLE — More visible, brighter */
.header-title {
    font-size: 54px;
    font-weight: 800;
    color: #f3f7ff;   /* brighter white-blue */

    text-shadow:
        0px 0px 8px rgba(100, 170, 255, 0.45),
        0px 0px 16px rgba(80, 150, 255, 0.28);
}

/* SUBTITLE — slightly brighter */
.header-subtitle {
    font-size: 22px;
    font-weight: 400;
    color: #d3e4f4;
    margin-top: 8px;
}

/* SECTION TITLE */
.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: #102a45;
    padding-left: 12px;
    border-left: 6px solid #007bff;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.95);
    padding: 28px;
    border-radius: 20px;
    border-left: 6px solid #0a4ba6;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.10);
    transition: 0.2s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0px 12px 26px rgba(0,0,0,0.18);
}

</style>
""", unsafe_allow_html=True)
