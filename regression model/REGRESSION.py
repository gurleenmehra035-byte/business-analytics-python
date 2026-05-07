#GURLEEN 12514824
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# Load dataset and remove missing values
df = pd.read_csv(r"C:\Users\DELL\Downloads\Punjab&SindbankBS4.csv").dropna()

# Define target variable
y = df["TotalLiabilities"]

# Select only numeric predictor variables (excluding target)
X = df.drop(columns=["TotalLiabilities"]).select_dtypes(include="number")

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree Regressor model
model = DecisionTreeRegressor(max_depth=4, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict values
y_pred = model.predict(X_test)

# Evaluate model
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("R2:", r2)
print("RMSE:", rmse)

# Plot Decision Tree
plt.figure(figsize=(8, 6))

plot_tree(
    model,
    feature_names=X.columns,
    filled=True,
    rounded=True,
    fontsize=7
)

plt.title("Decision Tree Regressor")
plt.show()