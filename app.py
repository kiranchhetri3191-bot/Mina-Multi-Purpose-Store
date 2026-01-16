import streanlit as st
# ---------------- HEADER FIX -------------------

logo_path = "Mina Store Logo.png"

header_html = f"""
<div style='display: flex; align-items: center; gap: 30px; margin-bottom: 40px;'>

    <!-- LEFT : LOGO FRAME -->
    <div style="
        background: linear-gradient(135deg, #1d4e89, #0f2557);
        padding: 18px;
        border-radius: 22px;
        height: 150px;
        width: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.20);
    ">
        <div style="
            background: white;
            padding: 12px;
            border-radius: 16px;
            width: 120px;
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
        ">
            <img src='{logo_path}' width='100' style='border-radius:10px;' />
        </div>
    </div>

    <!-- RIGHT : BLUE HEADER BOX -->
    <div style="
        background: linear-gradient(135deg, #1d4e89, #0f2557);
        padding: 32px 45px;
        border-radius: 22px;
        color: white;
        width: 70%;
        box-shadow: 0px 12px 40px rgba(0,0,0,0.28);
    ">
        <h1 style="margin: 0; font-size: 46px; font-weight: 800;">
            Mina Multi-Purpose Store
        </h1>

        <p style="margin: 0; margin-top: 10px; font-size: 20px; color: #dce3eb;">
            Birpara's Trusted Store for Gifts, Groceries, Hardware & Xerox
        </p>
    </div>

</div>
"""

st.markdown(header_html, unsafe_allow_html=True)
