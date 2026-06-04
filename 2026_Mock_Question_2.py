# %% [markdown]
# # 2026 Mock Question 2: Artificial Neural Networks (ANN)
# This notebook covers how to use an Artificial Neural Network using sklearn.
# We will use the MLPClassifier (Multi-Layer Perceptron) which is a type of ANN.

# %%
# Step 1: Import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Step 2: Let's use the famous XOR logic gate problem. 
# An ANN is great at solving this because it requires non-linear logic.
X = [[0, 0], 
     [0, 1], 
     [1, 0], 
     [1, 1]]
y = [0, 1, 1, 0] # Output is 1 only when inputs are different

# Step 3: Split data (Though dataset is very small, this is the standard flow)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 4: Initialize the Neural Network Model
# hidden_layer_sizes=(4,) means we have ONE hidden layer with 4 neurons inside it.
# max_iter=1000 means the model will loop through the data 1000 times (epochs) to learn.
ann_model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=2000, random_state=42)

# Step 5: Train (Fit) the Model
print("Training the Neural Network... This might take a split second!")
ann_model.fit(X_train, y_train)

# Step 6: Predict on test data
predictions = ann_model.predict(X_test)

# Step 7: Evaluate
print("\n--- ANN Results ---")
print("Predictions:", predictions)
print("Actual:", list(y_test))
print("Accuracy:", accuracy_score(y_test, predictions))

# %% [markdown]
# ### Extra Tip: The Math Behind ANN
# If the lecturer asks what's happening inside those 4 hidden neurons:
# 1. **Forward Propagation**: The inputs (0,1) are multiplied by `weights`, and a `bias` is added.
# 2. **Activation Function**: The result is passed through a function (like `Sigmoid` or `ReLU`) to squash the output between 0 and 1.
# 3. **Backpropagation**: The network checks its error, goes backwards, and updates the weights to be more accurate next time!
