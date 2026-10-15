import streamlit as st
import pandas as pd
import joblib
import base64
import sklearn
import plotly.express as px


model = joblib.load(
    "Water_Potability_prediction.joblib"
)


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
    r"D:\streamlit\Water_Potability\assets\image3.png",
    use_container_width=True
)

# Function to set the background image
def set_background(image_path):
    with open(image_path, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 2rem;
        }}

        [data-testid="stSidebar"] {{
            background-color: rgba(230, 245, 255, 0.95);
        }}

        h1, h2, h3 {{
            color: #075985;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Select the background image based on the prediction
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

if st.session_state.prediction_result == 1:
    set_background(
        r"D:\streamlit\Water_Potability\assets\image1.png"
    )

elif st.session_state.prediction_result == 0:
    set_background(
        r"D:\streamlit\Water_Potability\assets\image1.png"
    )

else:
    set_background(
        r"D:\streamlit\Water_Potability\assets\image2.png"
    )

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
st.sidebar.write("🔬Enter The Water Sample Parameter")

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
    # Create input DataFrame
    input_data = pd.DataFrame({
        "ph": [ph],
        "Hardness": [Hardness],
        "Solids": [Solids],
        "Chloramines": [Chloramines],
        "Sulfate": [Sulfate],
        "Conductivity": [Conductivity],
        "Organic_carbon": [Organic_carbon],
        "Trihalomethanes": [Trihalomethanes],
        "Turbidity": [Turbidity]
    })
    # Make prediction
    prediction = model.predict(input_data)
    prediction_label = int(prediction[0])
    # Store prediction for background selection
    st.session_state.prediction_result = prediction_label
    # Display result
    if prediction_label == 1:
        st.markdown("""
            <div style="
                background: linear-gradient(135deg, #064E3B, #047857);
                padding: 30px;
                border-radius: 20px;
                border: 2px solid #34D399;
                box-shadow: 0 0 25px rgba(52, 211, 153, 0.45);
                text-align: center;
                margin-top: 25px;
                margin-bottom: 25px;
            ">
                <div style="font-size: 55px;">💧</div>
                <h2 style="color: #FFFFFF; margin-bottom: 10px;">
                    Water is Potable!
                </h2>
                <p style="
                    color: #D1FAE5;
                    font-size: 18px;
                    margin-bottom: 15px;
                ">
                    The model predicts that this water sample is suitable
                    for drinking based on the supplied parameters.
                </p>
                <span style="
                    background: #34D399;
                    color: #064E3B;
                    padding: 8px 20px;
                    border-radius: 20px;
                    font-weight: bold;
                ">
                    PREDICTION: POTABLE
                </span>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #7F1D1D, #991B1B);
            padding: 30px;
            border-radius: 20px;
            border: 2px solid #F87171;
            box-shadow: 0 0 25px rgba(248, 113, 113, 0.4);
            text-align: center;
            margin-top: 25px;
            margin-bottom: 25px;
        ">
            <div style="font-size: 55px;">⚠️</div>
            <h2 style="color: #FFFFFF; margin-bottom: 10px;">
                Water is Not Potable!
            </h2>
            <p style="
                color: #FEE2E2;
                font-size: 18px;
                margin-bottom: 15px;
            ">
                The model predicts that this water sample is unsuitable
                for drinking based on the supplied parameters.
            </p>
            <span style="
                background: #F87171;
                color: #450A0A;
                padding: 8px 20px;
                border-radius: 20px;
                font-weight: bold;
            ">
                PREDICTION: NOT POTABLE
            </span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            background: rgba(5, 35, 60, 0.92);
            color: #FFFFFF;
            padding: 14px 20px;
            border-radius: 12px;
            border-left: 5px solid #00D4FF;
            margin-top: 15px;
            margin-bottom: 25px;
            font-size: 15px;
            line-height: 1.7;
            text-align: center;
        ">
            ⚕️ <b>Safety Disclaimer:</b>
            Machine learning predictions are estimates, not proof of drinking-water safety.
            Laboratory testing is required to verify drinking-water safety.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 📊 Water Quality Analytics")

    quality_data = pd.DataFrame({
        "Parameter": [
            "pH",
            "Hardness",
            "Solids",
            "Chloramines",
            "Sulfate",
            "Conductivity",
            "Organic Carbon",
            "Trihalomethanes",
            "Turbidity"
        ],
        "Value": [
            ph,
            Hardness,
            Solids,
            Chloramines,
            Sulfate,
            Conductivity,
            Organic_carbon,
            Trihalomethanes,
            Turbidity
        ]
    })

    fig = px.bar(
        quality_data,
        x="Parameter",
        y="Value",
        title="Water Sample Parameters",
        text="Value",
        template="plotly_dark"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title="Water Quality Parameters",
        yaxis_title="Entered Value",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)
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
        unsafe_allow_html=True)

    st.subheader("📋 Input Summary")
    st.dataframe(
        quality_data,
        use_container_width=True,
        hide_index=True
    )

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

# ============================================================
# DATASET ANALYSIS DASHBOARD
# ============================================================
st.markdown("## 📊 Dataset Analysis")

# IMPORTANT: Change this path if your training CSV has a different name/location.
DATASET_PATH = r"D:\streamlit\Water_Potability\water_potability.csv"

try:
    @st.cache_data
    def load_dataset(path):
        return pd.read_csv(path)

    df_analysis = load_dataset(DATASET_PATH)

    if "Potability" not in df_analysis.columns:
        st.warning("Dataset analysis needs a 'Potability' column. Check your CSV column names.")
    else:
        total_records = len(df_analysis)
        feature_count = len([c for c in df_analysis.columns if c != "Potability"])
        missing_count = int(df_analysis.isna().sum().sum())
        potable_count = int((df_analysis["Potability"] == 1).sum())
        not_potable_count = int((df_analysis["Potability"] == 0).sum())

        metric1, metric2, metric3, metric4 = st.columns(4)
        metric1.metric("📁 Total Records", f"{total_records:,}")
        metric2.metric("🧪 Water Features", feature_count)
        metric3.metric("💧 Potable Samples", f"{potable_count:,}")
        metric4.metric("🔍 Missing Values", f"{missing_count:,}")

        st.markdown("### 💧 Potability Distribution")
        class_data = pd.DataFrame({
            "Water Quality": ["Not Potable", "Potable"],
            "Samples": [not_potable_count, potable_count]
        })
        class_fig = px.pie(
            class_data,
            names="Water Quality",
            values="Samples",
            hole=0.55,
            color="Water Quality",
            color_discrete_map={"Potable": "#00C9A7", "Not Potable": "#FF4B4B"},
            title="Potable vs. Non-Potable Samples"
        )
        class_fig.update_traces(textposition="inside", textinfo="label+percent+value")
        class_fig.update_layout(template="plotly_dark", title_x=0.5)
        st.plotly_chart(class_fig, width="stretch")

        feature_options = [
            c for c in ["ph", "Hardness", "Solids", "Chloramines", "Sulfate",
                        "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"]
            if c in df_analysis.columns
        ]

        if feature_options:
            st.markdown("### 📈 Explore a Water-Quality Feature")
            selected_feature = st.selectbox(
                "Choose a parameter",
                feature_options,
                key="dataset_feature_select"
            )
            distribution_fig = px.histogram(
                df_analysis,
                x=selected_feature,
                color="Potability",
                nbins=40,
                barmode="overlay",
                opacity=0.7,
                color_discrete_map={0: "#FF4B4B", 1: "#00C9A7"},
                title=f"{selected_feature} Distribution by Potability"
            )
            distribution_fig.update_layout(
                template="plotly_dark", title_x=0.5,
                xaxis_title=selected_feature, yaxis_title="Number of Samples"
            )
            st.plotly_chart(distribution_fig, width="stretch")

        st.markdown("### 🔥 Feature Correlation Heatmap")
        numeric_data = df_analysis.select_dtypes(include="number")
        if numeric_data.shape[1] >= 2:
            corr_fig = px.imshow(
                numeric_data.corr(),
                text_auto=".2f",
                aspect="auto",
                color_continuous_scale="RdBu_r",
                zmin=-1,
                zmax=1,
                title="Correlation Between Numeric Features"
            )
            corr_fig.update_layout(template="plotly_dark", title_x=0.5, height=650)
            st.plotly_chart(corr_fig, width="stretch")
        else:
            st.info("Not enough numeric columns to calculate correlations.")

        st.markdown("### 🔍 Missing Values by Column")
        missing_data = df_analysis.isna().sum().rename_axis("Feature").reset_index(name="Missing Values")
        missing_data = missing_data[missing_data["Missing Values"] > 0].sort_values(
            "Missing Values", ascending=False
        )
        if missing_data.empty:
            st.success("No missing values found in this dataset.")
        else:
            missing_fig = px.bar(
                missing_data,
                x="Feature",
                y="Missing Values",
                text="Missing Values",
                title="Missing Values by Feature",
                color="Missing Values",
                color_continuous_scale=["#00D4FF", "#FF4B4B"]
            )
            missing_fig.update_layout(template="plotly_dark", title_x=0.5)
            st.plotly_chart(missing_fig, width="stretch")

except FileNotFoundError:
    st.warning(
        "Dataset analysis is not loaded. Set DATASET_PATH to the actual location "
        "of your water potability CSV file."
    )
except Exception as exc:
    st.error(f"Could not load dataset analysis: {exc}")

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

st.subheader("📈 Machine Learning Dashboard")

st.image(r"D:\streamlit\Water_Potability\assets\image4.png",caption="Water Sample Poatability Prediction — Data Analytics Dashboard",use_container_width=True)

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

st.markdown("""
<p style="
    color: #7D06C2;
    font-size: 14px;
    text-align: center;
    font-weight: 600;
">
    Built with Python • Pandas • Scikit-learn • Random Forest • Streamlit
</p>
""", unsafe_allow_html=True)