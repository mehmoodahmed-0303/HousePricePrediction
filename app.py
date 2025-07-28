import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and preprocessor
model = joblib.load('house_price_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Streamlit app
st.title("House Price Prediction")

# Input fields
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", 500, 5000, 1500)
total_bsmt_sf = st.number_input("Basement Area (sq ft)", 0, 5000, 1000)
garage_area = st.number_input("Garage Area (sq ft)", 0, 2000, 500)
lot_area = st.number_input("Lot Area (sq ft)", 1000, 50000, 10000)
neighborhood = st.selectbox("Neighborhood", ['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst', 'Gilbert', 'NridgHt', 'Sawyer', 'NWAmes', 'SawyerW', 'BrkSide', 'Crawfor', 'Mitchel', 'NoRidge', 'Timber', 'IDOTRR', 'ClearCr', 'StoneBr', 'SWISU', 'MeadowV', 'Blmngtn', 'BrDale', 'Veenker', 'NPkVill', 'Blueste'])
bldg_type = st.selectbox("Building Type", ['1Fam', '2fmCon', 'Duplex', 'Twnhs', 'TwnhsE'])
house_style = st.selectbox("House Style", ['1Story', '2Story', '1.5Fin', 'SLvl', 'SFoyer', '1.5Unf', '2.5Unf', '2.5Fin'])
mszoning = st.selectbox("Zoning", ['RL', 'RM', 'FV', 'RH', 'C (all)'])

# Prepare input data
input_data = pd.DataFrame({
    'LotArea': [lot_area],
    'GrLivArea': [gr_liv_area],
    'TotalBsmtSF': [total_bsmt_sf],
    'GarageArea': [garage_area],
    'OverallQual': [overall_qual],
    'Neighborhood': [neighborhood],
    'BldgType': [bldg_type],
    'HouseStyle': [house_style],
    'MSZoning': [mszoning]
})

# Predict
if st.button("Predict"):
    input_preprocessed = preprocessor.transform(input_data)
    if input_preprocessed.shape[1] != 44:
        feature_names = preprocessor.get_feature_names_out()
        missing_cols = set(feature_names) - set(preprocessor.get_feature_names_out(input_data.columns))
        missing_cols_idx = [list(feature_names).index(col) for col in missing_cols]
        for idx in missing_cols_idx:
            input_preprocessed = np.insert(input_preprocessed, idx, 0, axis=1)
    prediction = model.predict(input_preprocessed)[0]
    st.write(f"Predicted House Price: ${prediction:,.2f}")