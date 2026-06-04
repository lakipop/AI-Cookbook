# %% [markdown]
# # 2025 Past Paper: Question 2
# This paper focused on Machine Learning Models: Linear Regression and K-Means Clustering.

# %% [markdown]
# ### Part A: Linear Regression (Predicting Prices)
# Using historical data to predict house prices.

# %%
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. Load Data
# In the exam, they used: df = pd.read_csv('housing.csv')
# We will create dummy data here so you can run the code and see it work!
data = {
    'SquareFeet': [1500, 2000, 2500, 3000, 3500],
    'Bedrooms': [3, 3, 4, 4, 5],
    'Age': [10, 15, 5, 20, 2],
    'Price': [300000, 350000, 500000, 450000, 650000]
}
df = pd.DataFrame(data)

# 2. Split into Features (X) and Target (y)
X = df[['SquareFeet', 'Bedrooms', 'Age']]
y = df['Price']

# 3. Split into Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train (Fit) the Model
model = LinearRegression()
model.fit(X_train, y_train)

print("--- Linear Regression Results ---")
print('Coefficients (Weight of each feature):', model.coef_)
print('Intercept (Base price):', model.intercept_)
# .score() is a shortcut to get the R^2 accuracy score
print('R^2 Score (Accuracy):', model.score(X, y))

# 5. Predict and check error
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print('MAE (Mean Absolute Error):', mae)


# %% [markdown]
# ### Part B: K-Means Clustering
# Grouping customers based on Income and Spending habits. This is "Unsupervised" learning, meaning there is no 'Target' variable!

# %%
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Load Data
# In the exam, they used: df = pd.read_csv('customers.csv')
# Creating dummy data
customer_data = {
    'CustomerID': [1, 2, 3, 4, 5, 6],
    'AnnualIncome': [15000, 16000, 85000, 87000, 120000, 130000],
    'SpendingScore': [39, 41, 80, 85, 10, 15]
}
df_customers = pd.DataFrame(customer_data)

# 2. Select the features we want to group by (Income and Spending)
X = df_customers[['AnnualIncome', 'SpendingScore']]
# Notice there is no 'y' train! We don't have the answers, the model has to group them itself.

# 3. Initialize Model
# n_clusters=3 means we want the AI to group shoppers into 3 distinct categories
kmeans = KMeans(n_clusters=3, random_state=42)

# 4. Train the Model
kmeans.fit(X)

# 5. Attach the AI's predicted cluster (0, 1, or 2) back to our original dataset
df_customers['Cluster'] = kmeans.labels_

print("\n--- Clustering Results ---")
print(df_customers)

# 6. Plot the results on a graph
plt.scatter(df_customers['AnnualIncome'], df_customers['SpendingScore'], c=df_customers['Cluster'], cmap='viridis', s=100)
plt.title("Customer Segments")
plt.xlabel('Annual Income ($)')
plt.ylabel('Spending Score (1-100)')
plt.show()
