# House Price Prediction

## Overview
Machine learning project to predict house prices using the Ames Housing Dataset. Built a Random Forest model and deployed it as a Streamlit web app.

## Files
- `house_price_prediction.ipynb`: Preprocessing, model training, and EDA.
- `app.py`: Streamlit app for predictions.
- `house_price_model.pkl`: Trained Random Forest model.
- `preprocessor.pkl`: Preprocessing pipeline.
- `requirements.txt`: Dependencies.
- `train.csv`: Dataset.

## How to Run
1. Install: `pip install -r requirements.txt`
2. Run locally: `streamlit run app.py`
3. Access deployed app: https://housepriceprediction1318.streamlit.app

## Results
- Model: Random Forest (RMSE: $29,194.74, R2: 0.89).
- Key features: OverallQual (0.59), GrLivArea (0.18), TotalBsmtSF (0.09).
- Example: Predicted $214,830.41 for OverallQual=7, GrLivArea=2000, TotalBsmtSF=1000, GarageArea=500, LotArea=10000, Neighborhood=CollgCr, BldgType=1Fam, HouseStyle=2Story, MSZoning=RL.