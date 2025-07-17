# ⚡ Smart Grid Stability Prediction

This project focuses on predicting **smart grid stability** using machine learning models. The goal is to develop intelligent systems that can analyze energy data and predict whether a given grid condition is stable or unstable.

---

## 📊 Dataset

The dataset used is related to **Smart Grid Stability**, containing numerical features such as:
- Relative Compactness
- Surface Area
- Wall Area
- Roof Area
- Overall Height
- Orientation
- Glazing Area
- Glazing Area Distribution

Stored in:
- `smart_grid_stability.xlsx`

---

## 🧠 Machine Learning Models

We trained and evaluated the following models:
- 🌲 **Random Forest**
- 🌳 **Decision Tree**
- 🚀 **XGBoost**

Each model is saved in `.pkl` format for future predictions:
- `random_forest_model.pkl`
- `Decision_tree_model.pkl`
- `xgboost.pkl`

---

## 🛠️ Project Structure

```bash
smart-grid-stability/
│
├── app.py                        # Main application script
├── Smart_grid_stability.ipynb   # Jupyter Notebook (model training, visualization)
├── Decision_tree_model.pkl      # Trained Decision Tree model
├── random_forest_model.pkl      # Trained Random Forest model
├── xgboost.pkl                  # Trained XGBoost model
├── smart_grid_stability.xlsx    # Input dataset
├── README.md                    # Project description
└── .gitignore                   # Ignored files
