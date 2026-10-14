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


