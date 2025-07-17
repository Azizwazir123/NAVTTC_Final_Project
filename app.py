import streamlit as st
import numpy as np
import pandas as pd
import joblib
from xgboost import XGBClassifier

# Title and description
st.title("⚡ Smart Grid Stability Predictor")
st.markdown("""
Predict grid stability using the following features:
- **τ (tau)**: Time delay inputs
- **P (p)**: Power injection values
- **G (g)**: Conductance values
""")

# 1. Model Selection
model_choice = st.selectbox("🔍 Select Model", ["XGBoost", "Random Forest", "Decision Tree"])

# 2. Load selected model
if model_choice == "XGBoost":
    model = XGBClassifier()
    model=joblib.load("xgboost.pkl")  
elif model_choice == "Random Forest":
    model = joblib.load("random_forest_model.pkl")  
elif model_choice == "Decision Tree":
    model = joblib.load("Decision_tree_model.pkl") 

# 3. Input Features
st.header("🧮 Input Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Time Delays (τ)")
    tau1 = st.number_input("τ1", value=0.5)
    tau2 = st.number_input("τ2", value=0.5)
    tau3 = st.number_input("τ3", value=0.5)
    tau4 = st.number_input("τ4", value=0.5)

with col2:
    st.subheader("Power Injections (P)")
    p1 = st.number_input("P1", value=0.0)
    p2 = st.number_input("P2", value=0.0)
    p3 = st.number_input("P3", value=0.0)
    p4 = st.number_input("P4", value=0.0)

with col3:
    st.subheader("Conductances (G)")
    g1 = st.number_input("G1", value=0.0)
    g2 = st.number_input("G2", value=0.0)
    g3 = st.number_input("G3", value=0.0)
    g4 = st.number_input("G4", value=0.0)

# 4. Prediction
if st.button("🚀 Predict Stability"):
    input_data = np.array([[tau1, tau2, tau3, tau4, p1, p2, p3, p4, g1, g2, g3, g4]])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader("📊 Result")
    if prediction == 1:
        st.success("✅ The grid is **Stable**")
    else:
        st.error("❌ The grid is **Unstable**")
    
    st.write(f"🔢 Raw prediction value: `{prediction}`")

    # Optional: Show probability if supported
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_data)[0]
        st.write("📈 Probability of stability:", round(proba[1] * 100, 2), "%")
