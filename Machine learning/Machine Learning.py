#GURLEEN 12514824
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeRegressor, plot_tree

from sklearn.metrics import r2_score, mean_squared_error

import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\DELL\Downloads\Punjab&SindbankBS4.csv").dropna()

y = df['TAD']

X = df.drop(columns=['TAD']).select_dtypes(include='number')

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeRegressor(max_depth=4, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2:", r2_score(y_test, y_pred))

print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)

plt.figure(figsize=(6,4))

plot_tree(
    model,
    feature_names=X.columns,
    filled=True,
    fontsize=6
)

plt.tight_layout()

plt.show()