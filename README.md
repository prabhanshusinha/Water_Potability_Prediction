💧🌊 Water Potability Prediction 🌊💧

🧪 Smart Water Quality Analysis Powered by Machine Learning 🤖

Predict • Explore • Visualize • Understand

A stylish, interactive web application that uses machine learning to estimate whether a water sample is predicted to be potable based on nine water-quality parameters

🌱 Turning Water Data into Meaningful Insights 💦

🌟 About the Project

Water quality is important to public health and everyday life. This project demonstrates how machine learning and data visualization can be combined to explore water-quality data and estimate a sample's potability.

With an interactive Streamlit dashboard, users can enter water-quality measurements, receive a model prediction, and explore visual summaries of both an individual sample and the dataset.

⚠️ Safety first: This is an educational machine-learning project—not a certified water-testing system. A prediction does not prove that water is safe to drink. Always rely on qualified laboratory testing and applicable public-health guidance to verify drinking-water safety.

✨ Key Features

💡 Feature

🔎 What it does

💧 Potability Prediction

Uses a trained machine-learning pipeline to classify a sample.

🎛️ Interactive Inputs

Enter nine water-quality measurements through the Streamlit sidebar.

📊 Sample Analytics

View a bar chart and summary of the submitted values.

🥧 Potability Distribution

Explore the potable and non-potable sample counts in the dataset.

📈 Feature Explorer

Inspect parameter distributions grouped by the target class.

🔥 Correlation Heatmap

Explore relationships among numeric dataset features.

🕵️ Missing-Value Analysis

Review missing values in the dataset.

🎨 Custom Dashboard UI

Enjoy styled cards, visual sections, and interactive Plotly charts.

🧠 Saved ML Pipeline

Load a serialized .joblib pipeline for predictions.

🧪 Water Quality Parameters

The model uses these nine input features:

🔬 Parameter

📝 Description

ph

⚗️ pH level

Hardness

💎 Water hardness

Solids

🧂 Total dissolved solids

Chloramines

🧪 Chloramines concentration

Sulfate

⚗️ Sulfate concentration

Conductivity

⚡ Electrical conductivity

Organic_carbon

🌿 Organic carbon concentration

Trihalomethanes

🧬 Trihalomethanes concentration

Turbidity

🌫️ Water turbidity

🎯 Prediction Classes

🟢 1 — Potable: The model predicts the sample belongs to the potable class.

🔴 0 — Not Potable: The model predicts the sample belongs to the non-potable class.

These are predictions made by the trained model, not a guarantee of real-world drinking-water safety.

🧠 Machine Learning Workflow

The notebook Water_potability_model.ipynb documents the model-development workflow:

📥 Load the data and inspect its structure.

🔍 Explore the dataset through exploratory data analysis (EDA).

📊 Visualize features and relationships.

🎯 Separate features and target into X and y.

✂️ Split the data into training and testing sets using an 80/20 split and random_state=42.

🤖 Compare classifiers, including Logistic Regression, Decision Tree, K-Nearest Neighbors, Support Vector Machine, Random Forest, Gradient Boosting, and Gaussian Naive Bayes.

🛠️ Tune the Random Forest pipeline using GridSearchCV and 5-fold cross-validation.

💾 Save the best estimator as Water_Potability_prediction.joblib.

🚀 Load the saved pipeline in Streamlit for interactive predictions.

The app loads the saved preprocessing-and-model pipeline so its configured preprocessing steps are applied during prediction.

📌 Model evaluation: Accuracy, F1 score, and other performance values should be reported from the actual notebook results. No unverified metric is claimed in this README.

🗂️ Project Structure

A suggested repository layout:

💧 Water-Potability-Prediction/
│
├── 🐍 app.py
├── 🧠 Water_Potability_prediction.joblib
├── 📓 Water_potability_model.ipynb
├── 📊 water_potability.csv
├── 📦 requirements.txt
├── 📖 README.md
│
└── 🎨 assets/
    ├── image1.png
    ├── image2.png
    ├── image3.png
    └── image4.png

📝 Note: Use the actual filenames in your repository. The app currently contains some Windows-specific absolute paths for the dataset and images. Update these paths before sharing or deploying the project.

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone <GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>

Replace the placeholders with your actual GitHub repository URL and folder name.

2️⃣ Create a Virtual Environment

🪟 Windows PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1

🐧 macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies

If the project includes requirements.txt:

pip install -r requirements.txt

Otherwise, install the packages used by the application and notebook:

pip install streamlit pandas scikit-learn joblib plotly numpy matplotlib seaborn jupyter

💡 Tip: Record the tested package versions in requirements.txt to make the environment easier to reproduce.

4️⃣ Check the Required Files

Before running the app, make sure the following files are available:

🧠 Water_Potability_prediction.joblib — trained model pipeline

📊 water_potability.csv — dataset used by the analytics dashboard

🎨 assets/image1.png, assets/image2.png, assets/image3.png, assets/image4.png — dashboard images

The dataset path currently configured in the app is:

DATASET_PATH = r"D:\streamlit\Water_Potability\water_potability.csv"

🔧 Update DATASET_PATH to match your own CSV location. For a portable setup, consider using a relative path such as data/water_potability.csv if the CSV is stored in a data/ folder. Update the image paths in the same way.

5️⃣ Launch the Application 🚀

streamlit run app.py

If your app file has a different name, replace app.py with that filename.

🌐 Streamlit will print a local address in the terminal. Open it in your browser to use the dashboard.

📊 Dataset Analytics Dashboard

The dataset analytics section expects a CSV containing the nine input features and a target column named Potability.

It provides:

🧾 Record, feature, and missing-value counts

🥧 Potable versus non-potable class distribution

📈 Interactive feature histograms grouped by potability

🔥 Numeric-feature correlation heatmap

🕵️ Missing values by column

If the analytics section cannot load, verify the CSV path and confirm that the target column is named exactly Potability.

🧰 Tech Stack

🛠️ Technology

🚀 Role

🐍 Python

Core programming language

🧮 Pandas & NumPy

Data manipulation and numerical operations

🤖 Scikit-learn

Preprocessing, classification, evaluation, and hyperparameter tuning

💾 Joblib

Saving and loading the trained pipeline

📊 Plotly

Interactive data visualizations

🎈 Streamlit

Web app and dashboard interface

📉 Matplotlib & Seaborn

Exploratory visualizations in the notebook

📓 Jupyter Notebook

Model experimentation and analysis

🛠️ Troubleshooting

❌ Model file not found

Check that Water_Potability_prediction.joblib exists in the app's working directory, or update the path passed to joblib.load().

📂 Dataset analysis does not load

Verify DATASET_PATH, the CSV filename, and the presence of the Potability column.

🐍 Scikit-learn version compatibility error

Serialized Scikit-learn estimators may not load reliably across different library versions. Use the compatible version from the training environment where possible, or retrain and resave the pipeline in the target environment. Only load model files from trusted sources.
🖼️ Dashboard image not found

Confirm that the assets/ folder and image filenames match the paths used in app.py. Replace machine-specific absolute paths with project-relative paths for portability.

🚀 Future Improvements

🧪 Add automated tests for the preprocessing pipeline and predictions.

📉 Display verified model evaluation metrics and a confusion matrix.

☁️ Prepare a portable configuration for cloud deployment.

🧭 Improve input validation and explain the model's predictions.

📚 Add links to dataset documentation and trusted water-quality guidance.

👨‍💻 Author

Prabhanshu Kumar 💻

🔗 GitHub: https://github.com/prabhanshusinha
📦 Project Repository: https://github.com/prabhanshusinha/Water_Potability_Prediction.git

💧 Clean Water Matters • 📊 Data Drives Discovery • 🤖 ML Enables Exploration

Built with ❤️ using Python, Scikit-learn, Plotly, and Streamlit

📜 Disclaimer

This project is intended for learning, experimentation, and data exploration. It is not a certified water-testing system and should not be used as the sole basis for deciding whether water is safe to drink. Actual water safety must be verified through appropriate laboratory testing and qualified public-health guidance.
