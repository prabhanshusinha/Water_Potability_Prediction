import streamlit as st
import pandas as pd
import joblib
import base64


model =joblib.load("D:\streamlit\Water_Potability\Water_Potability_prediction.joblib")

st.set_page_config(
    page_title="WATER POTABILITY PREDICTION",
    page_icon="💧",
    layout="wide"
)


st.markdown("""
    <style>
        /* Keep the Streamlit header and Deploy button visible */
        header[data-testid="stHeader"] {
            background: transparent;
        }

        /* Hide the three-dot menu if desired */
        button[data-testid="stMainMenu"] {
            display: none;
        }

        /* Reduce the extra top spacing */
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.image(
    "D:\streamlit\Water_Potability\ChatGPT Image Oct 14, 2026, 09_46_27 AM.png",
    use_container_width=True
)

def set_background(image_path): 
     with open(image_path, "rb") as image: 
        encoded_image = base64.b64encode(image.read()).decode() 
        st.markdown( f""" <style> .stApp {{ background-image: url("data:image/png;base64,{encoded_image}"); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed; }} .block-container {{ padding-top: 2rem; }} [data-testid="stSidebar"] {{ background-color: rgba(230, 245, 255, 0.95); }} h1, h2, h3 {{ color: #075985; }} </style> """, unsafe_allow_html=True ) 
        
set_background("D:\streamlit\Water_Potability\ChatGPT Image Oct 14, 2026, 09_52_46 AM.png")

st.markdown(
    """
    <div style="
        background: rgba(0, 40, 80, 0.80);
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        border: 1px solid rgba(0, 206, 209, 0.6);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        margin-top: 30px;
    ">
        <h2 style="color: #00CED1;">
            🌊 Welcome to Water Quality Analysis
        </h2>
        <p style="
            color: white;
            font-size: 17px;
            line-height: 1.8;
        ">
            Enter your water sample parameters in the sidebar
            and click the prediction button to analyze water potability.
        </p>
        <p style="color: #BAE6FD; font-size: 15px;">
            🤖 Machine Learning &nbsp; | &nbsp;
            🧪 Water Quality Analysis &nbsp; | &nbsp;
            💧 Potability Prediction
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <hr style="
        height: 3px;
        background: linear-gradient(
            90deg,
            transparent,
            #00CED1,
            #38BDF8,
            transparent
        );
        border: none;
        margin: 30px 0;
    ">
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown("""
<style>

/* 🌊 Colorful Sidebar Background */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #FF512F 0%,
        #DD2476 35%,
        #6A11CB 70%,
        #2575FC 100%
    );
}

/* Sidebar Text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #FFFFFF !important;
}

/* Sidebar Headings */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #00FFFF !important;
    font-weight: bold;
}

/* Sidebar Input Fields */
[data-testid="stSidebar"] input {
    color: #FFFFFF !important;
    background-color: rgba(10, 25, 47, 0.9) !important;
    border: 1px solid #00D4FF !important;
    border-radius: 8px;
}

/* Sidebar Button */
[data-testid="stSidebar"] button {
    background: linear-gradient(90deg, #00C9FF, #92FE9D);
    color: #082032 !important;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    transition: 0.3s;
}

/* Sidebar Button Hover */
[data-testid="stSidebar"] button:hover {
    background: linear-gradient(90deg, #92FE9D, #00C9FF);
    box-shadow: 0 0 15px rgba(0, 212, 255, 0.7);
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("🧪 Details About Water Sample ")
st.sidebar.write("🔬 Enter The Water Sample Parameter !!")

st.sidebar.divider()

# Enter All Parameter of Sample

ph=st.sidebar.number_input(
    "🧪 pH Level",
    min_value=0.0,
    max_value=14.0,
    value=7.000000,
    step=0.000001,
    format="%.6f"
)

Hardness=st.sidebar.number_input(
    "💧 Hardness (mg/L as CaCo3)",
    min_value=0.0,
    max_value=500.0,
    value=200.000000,
    step=0.000001,
    format="%.6f"
)


Solids=st.sidebar.number_input(
    "🧂 Total Dissolved Solids",
    min_value=0.0,
    max_value=100000.0,
    value=20000.000000,
    step=0.000001,
    format="%.6f"
)

Chloramines=st.sidebar.number_input(
    "⚗️ Chloramines (mg/L)",
    min_value=0.0,
    max_value=14.0,
    value=7.000000,
    step=0.000001,
    format="%.6f"
)

Sulfate=st.sidebar.number_input(
    "🧪 Sulfate (mg/L)",
    min_value=0.0,
    max_value=1000.0,
    value=250.000000,
    step=0.000001,
    format="%.6f"
)

Conductivity=st.sidebar.number_input(
    "⚡Conductivity (μS/cm)",
    min_value=0.0,
    max_value=1500.0,
    value=60.000000,
    step=0.000001,
    format="%.6f"
)

Organic_carbon=st.sidebar.number_input(
    "🌿Organic_carbon (mg/L)",
    min_value=0.0,
    max_value=30.0,
    value=14.000000,
    step=0.000001,
    format="%.6f"
)

Trihalomethanes=st.sidebar.number_input(
    "🧬Trihalomethanes (µg/L)",
    min_value=0.0,
    max_value=150.0,
    value=66.000000,
    step=0.000001,
    format="%.6f"
)

Turbidity=st.sidebar.number_input(
    "🌊Turbidity (µg/L)",
    min_value=0.0,
    max_value=10.0,
    value=3.000000,
    step=0.000001,
    format="%.6f"
)

st.sidebar.divider()

predict_buttom=st.sidebar.button(
    "🔍 Predict Water Potability",
    use_container_width=True
)

# ============================================================
# MAIN AREA
# ============================================================

if predict_buttom:
    pass

else:
    st.markdown("""
    <div style="
        background: linear-gradient(
            135deg,
            rgba(3, 37, 65, 0.95),
            rgba(8, 80, 110, 0.92)
        );
        padding: 20px 25px;
        border-radius: 15px;
        border: 1px solid #00D4FF;
        box-shadow: 0 0 18px rgba(0, 212, 255, 0.25);
        text-align: center;
        margin-top: 25px;
    ">
        <p style="
            color: #FFFFFF;
            font-size: 17px;
            font-weight: 600;
            margin: 0;
            line-height: 1.8;
        ">
            👈 Enter the water sample parameters in the sidebar
            <br>
            <span style="color: #67E8F9;">
                Click Predict Water Potability to get your prediction.
            </span>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <hr style="
        height: 3px;
        background: linear-gradient(
            90deg,
            transparent,
            #00CED1,
            #38BDF8,
            transparent
        );
        border: none;
        margin: 30px 0;
    ">
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown("""
<div style="
    background: linear-gradient(135deg, #06C2A9, #123F63);
    padding: 5px;
    border-radius: 15px;
    border: 1px solid #00D4FF;
    margin-bottom: 20px;
">
    <h3 style="color:#00D4FF; margin :0;"> 🧠 About the Model</h3>
</div>
""", unsafe_allow_html=True)

# _________________________________About MODEL___________________________________________________________

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #F54927, #123F63);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #00D4FF;
        min-height: 260px;
    ">
    <h3 style="color:#00D4FF;">📊 Dataset</h3>

    <p style="color:#FFFFFF; font-weight:bold;">
        Water Potability Dataset
    </p>

    <p style="color:#FFFFFF; line-height:1.8;">
        Used to predict water potability based on various
        water quality parameters and chemical properties.
    </p>

    <p style="color:#00D4FF;">
        💧 9 Water Quality Features
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""

    <div style="
        background: linear-gradient(135deg, #11D9D6, #123F63);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #00D4FF;
        min-height: 260px;
    ">

    <h3 style="color:#00D4FF;">🌲 Model</h3>
    <p style="color:#FFFFFF; font-weight:bold;">
        Random Forest Classifier
    </p>
    <p style="color:#FFFFFF; line-height:1.8;">
        The trained preprocessing pipeline is stored
        together with the model in the .joblib file.
    </p>
    <p style="color:#00D4FF;">
        🤖 Machine Learning Classification
    </p>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #AC06C2, #123F63);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #00D4FF;
        min-height: 260px;
    ">
    <h3 style="color:#00D4FF;">🎯 Prediction</h3>

    <p style="color:#FFFFFF; line-height:1.8;">
        The model predicts one of the following:
    </p>

    <p style="color:#4ADE80; font-weight:bold;">
        ✅ 1 — Potable (Suitable for Drinking)
    </p>

    <p style="color:#FDA4AF; font-weight:bold;">
        ❌ 0 — Not Potable (Unsuitable for Drinking)
    </p>
    """, unsafe_allow_html=True)