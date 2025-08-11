import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# loading dataset
df = pd.read_csv('/home/ibrahim/jupyter/datasets/housePrice.csv')

# cleaning data
df['Area'] = df['Area'].str.replace(',', '')
df['Area'] = df['Area'].astype(int)

df['Price(USD)'] = df['Price(USD)'].astype(int)
df['Price'] = df['Price'].astype(int)

# removing outliers in Area column
Q1 = df['Area'].quantile(0.25)
Q3 = df['Area'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Area'] >= lower_bound) & (df['Area'] <= upper_bound)]

# removing outliers in Price column
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

# removing outliers in Price(USD) column
Q1 = df['Price(USD)'].quantile(0.25)
Q3 = df['Price(USD)'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Price(USD)'] >= lower_bound) & (df['Price(USD)'] <= upper_bound)]

# retrieving bool columns
df_bools = df.select_dtypes('bool')
df_bool_cols = df_bools.columns

# converting bool columns to integer
for col in df_bool_cols:
    df[col] = df[col].astype(int)

# dropping non-feature columns and loading it into x
x = df.drop(columns=['Address', 'Price', 'Price(USD)'])

# loading label column into y
y = df['Price(USD)']

# splitting features and label data for training and testing model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# creating model
model = RandomForestRegressor(criterion='absolute_error', max_depth=10, n_estimators=150, random_state=44)

# training the model
model.fit(x_train, y_train)

# exporting model
filename = 'house_price_model_v4'
joblib.dump(model, f'app/{filename}.joblib')
print(f'success created joblib file: app/{filename}.joblib')
