# %% [markdown]
# # 2026 Mock Question 3: Decision Trees
# Decision Trees map out decisions like a flowchart.
# We will use DecisionTreeClassifier to predict whether a customer will buy a product.

# %%
# Step 1: Import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 2: Create dummy data
# Age: 0=Young, 1=Old | Income: 0=Low, 1=High
data = {
    'Age': [0, 0, 1, 1, 0, 1, 0, 1],
    'Income': [0, 1, 0, 1, 0, 1, 1, 0],
    'Will_Buy': [0, 0, 0, 1, 0, 1, 1, 0] # Target variable
}
df = pd.DataFrame(data)

# Step 3: Split into Features (X) and Target (y)
X = df[['Age', 'Income']]
y = df['Will_Buy']

# Step 4: Split data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Initialize the Decision Tree Model
# random_state=42 ensures we get the same result every time we run the code
tree_model = DecisionTreeClassifier(random_state=42)

# Step 6: Train (Fit) the Model
tree_model.fit(X_train, y_train)

# Step 7: Predict
predictions = tree_model.predict(X_test)

# Step 8: Evaluate
print("--- Decision Tree Results ---")
print("Predictions:", predictions)
print("Actual:", list(y_test))
print("Accuracy Score:", accuracy_score(y_test, predictions))

# %% [markdown]
# ### Extra Tip: Why use Decision Trees?
# Decision trees are "White Box" models, meaning they are very easy to explain to a human!
# It literally asks questions: "Is Age > 0?" -> Yes -> "Is Income > 0?" -> Yes -> BUY!
