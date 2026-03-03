#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def get_input():
    
    try:
        n = int(input("Enter number of points (N): "))
        k = int(input("Enter number of neighbours (k): "))

        if k > n:
            print(f"Error: k ({k}) cannot be greater than N ({n}).")
            return None, None, None

        data = np.zeros((n, 2))

        for i in range(n):
            print(f"Point {i + 1}:")
            data[i, 0] = float(input("  x: "))
            data[i, 1] = float(input("  y: "))

        return data, n, k
    except ValueError:
        print("Invalid input. Please use numbers.")
        return None, None, None

def run_analysis():
    # Step 1. Collect data
    train_data, n, k = get_input()
    if train_data is None:
        return

    # Step 2. Extract x & y
    X_train = train_data[:, 0].reshape(-1, 1)
    y_train = train_data[:, 1]

    # Step 3. Calculate Variance
    label_variance = np.var(y_train)
    print(f"\n--- Training Stats ---")
    print(f"Label Variance: {label_variance:.4f}")

    # Step 4. Prediction!
    target_x = float(input("\nEnter the X value to predict Y for: "))
    
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)
    
    prediction = model.predict([[target_x]])[0]
    
    print(f"The {k}-NN predicted 'Y' for X = {target_x} is: {prediction:.4f}")

if __name__ == "__main__":
    run_analysis()


# In[ ]:




