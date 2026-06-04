# %% [markdown]
# # 2026 Mock Question 1: Regression Modelling
# In this notebook, we'll cover both Linear Regression (predicting a number)
# and Logistic Regression (predicting a category like Yes/No).
# We are using VS Code's Interactive Window. Click "Run Cell" above each code block!

# %% [markdown]
# ### Part A: Linear Regression (Predicting House Prices)
# Imagine you are given a dataset of houses and you need to predict the price based on their size.

# %%
# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 2: Create some dummy data (In the exam, you'll use pd.read_csv('filename.csv'))
data = {
    'Size_sqft': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Price': [200000, 300000, 400000, 500000, 600000]
}
df = pd.DataFrame(data)

# Step 3: Split into Features (X) and Target (y)
X = df[['Size_sqft', 'Bedrooms']] # The things we use to predict
y = df['Price']                   # The thing we want to predict

# Step 4: Split data into Training and Testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize the Model
model = LinearRegression()

# Step 6: Train (Fit) the Model
model.fit(X_train, y_train)

# Step 7: Predict on the test set
predictions = model.predict(X_test)

# Step 8: Evaluate the model
print("--- Linear Regression Results ---")
print("Predictions:", predictions)
print("Actual Prices:", list(y_test))
print("MAE (Mean Absolute Error):", mean_absolute_error(y_test, predictions))
print("R^2 Score:", r2_score(y_test, predictions))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# %% [markdown]
# ### Part B: Logistic Regression (Predicting Pass/Fail)
# Now let's predict if a student Passes (1) or Fails (0) based on hours studied.

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1 & 2: Create dummy data
data_classification = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'Passed': [0, 0, 0, 0, 1, 1, 1, 1] # 0 = Fail, 1 = Pass
}
df_class = pd.DataFrame(data_classification)

X = df_class[['Hours_Studied']]
y = df_class['Passed']

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 4: Initialize the Logistic Regression Model
logistic_model = LogisticRegression()

# Step 5: Train the model
logistic_model.fit(X_train, y_train)

# Step 6: Predict
log_predictions = logistic_model.predict(X_test)

# Step 7: Evaluate
print("\n--- Logistic Regression Results ---")
print("Predictions (Pass/Fail):", log_predictions)
print("Actual (Pass/Fail):", list(y_test))
print("Accuracy Score:", accuracy_score(y_test, log_predictions))
print("Confusion Matrix:\n", confusion_matrix(y_test, log_predictions))
