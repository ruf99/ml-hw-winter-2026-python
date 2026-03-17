#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.metrics import accuracy_score
import warnings

# Let's suppress unnecessary warnings for very small datasets
warnings.filterwarnings('ignore')

def main():
    try:
        # --- 1. DATA COLLECTION (Numpy) ---
        n = int(input("Enter number of training samples (N): "))
        train_x, train_y = [], []
        for i in range(n):
            train_x.append([float(input(f"  Train x_{i+1}: "))])
            train_y.append(int(input(f"  Train y_{i+1}: ")))

        m = int(input("\nEnter number of test samples (M): "))
        test_x, test_y = [], []
        for i in range(m):
            test_x.append([float(input(f"  Test x_{i+1}: "))])
            test_y.append(int(input(f"  Test y_{i+1}: ")))

        X_train, y_train = np.array(train_x), np.array(train_y)
        X_test, y_test = np.array(test_x), np.array(test_y)

        # --- 2. GRID SEARCH (ML) ---
        # To avoid the "n_neighbors > n_samples" error during cross-validation,
        # we calculate the max k possible for the internal folds.
        # If using LeaveOneOut, max_k can be n-1.
        max_k = min(10, n - 1) if n > 1 else 1
        param_grid = {'n_neighbors': np.arange(1, max_k + 1)}

        # LeaveOneOut is the best CV strategy for very small N
        cv_strategy = LeaveOneOut() if n < 10 else 5
        
        grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=cv_strategy)
        grid.fit(X_train, y_train)

        # --- 3. OUTPUT ---
        best_k = grid.best_params_['n_neighbors']
        # Re-predicting on the actual TestS provided by user
        y_pred = grid.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print("\n" + "="*35)
        print(f"Best k found: {best_k}")
        print(f"Test Accuracy: {acc:.2%}")
        print("="*35)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


# 
