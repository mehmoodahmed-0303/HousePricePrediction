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

## Setup
1. Clone the repository:
```bash
git clone https://github.com/mehmoodahmed-0303/HousePricePrediction.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
streamlit run app.py
```
4. Access deployed app: https://housepriceprediction1318.streamlit.app

# Results
## Dataset:
- 1460 rows, 81 columns; SalePrice as target (mean: $180,921, max: $755,000).
## Model:
- Random Forest (RMSE: $29,194.74, R2: 0.89).

## Key Features:
- Numerical: OverallQual, GrLivArea, TotalBsmtSF, GarageArea, LotArea.
- Categorical: Neighborhood, BldgType, HouseStyle, MSZoning.

## Feature Importance:
- OverallQual: 0.588257
- GrLivArea: 0.178465
- TotalBsmtSF: 0.091544

## EDA:
- ## Top 5 correlations with SalePrice:
- - SalePrice: 1.000000
- - OverallQual: 0.790982
- - GrLivArea: 0.708624
- - GarageCars: 0.640409
- - GarageArea: 0.623431

## Example Prediction:
- $214,830.41 for OverallQual=7, GrLivArea=2000, TotalBsmtSF=1000, GarageArea=500, LotArea=10000, Neighborhood=CollgCr, BldgType=1Fam, HouseStyle=2Story, MSZoning=RL.

# Deployment
- Streamlit app deployed at https://housepriceprediction1318.streamlit.app.
- Inputs: LotArea, GrLivArea, TotalBsmtSF, GarageArea, OverallQual, Neighborhood, BldgType, HouseStyle, MSZoning.
- Tested locally: Predicted $214,830.41 (see above inputs).
- Deployed app prediction: [Pending confirmation].


# Portfolio
- Added to GitHub profile: mehmoodahmed-0303.
- Status: [Pending confirmation].