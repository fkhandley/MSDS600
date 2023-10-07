import pandas as pd
import numpy as np
from pycaret.classification import ClassificationExperiment
print("Hello, and welcome to the Churn Predictor.  Please make sure you're running a an environment with pycaret.")
file_path = input("To see into the future of your customers, provide a file path to your churn data in csv format:")
df = pd.read_csv (file_path,index_col='customerID')
df = df[['tenure','PhoneService','Contract','PaymentMethod','MonthlyCharges','TotalCharges']]
new_pycaret = ClassificationExperiment()
loaded_model = new_pycaret.load_model('Churn_model')
y_pred = predictions = loaded_model.predict(df)
print("Our predictions for your churn observations are as follow:", y_pred)