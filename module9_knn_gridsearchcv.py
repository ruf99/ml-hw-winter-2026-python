#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    print("--- 1. Training Set Collection ---")
    try:
        n_input = int(input("How many training samples (N)? "))
        
        train_x = []
        train_y = []
        
        for i in range(n_input):
            print(f"  Sample {i+1}:")
            x = float(input("    Enter x (feature): "))
            y = int(input("    Enter y (label): "))
            train_x.append([x]) # Nested list to keep it 2D for sklearn
            train_y.append(y)
            
        # Convert to Numpy arrays for processing
        X_train = np.array(train_x)
        y_train = np.array(train_y)

        print("\n--- 2. Test Set Collection ---")
        m_input = int(input("How many test samples (M)? "))
        
        test_x = []
        test_y = []
        
        for i in range(m_input):
            print(f"  Test Sample {i+1}:")
            x = float(input("    Enter x (feature): "))
            y = int(input("    Enter y (label): "))
            test_x.append([x])
            test_y.append(y)
            
        X_test = np.array(test_x)
        y_test = np.array(test_y)

        # --- 3. Finding the Best k ---
        best_k = 1
        max_accuracy = -1.0
        
        # Range of k: 1 to 10 (limited by training size)
        upper_k = min(10, n_input)
        
        print(f"\nEvaluating k from 1 to {upper_k}...")
        
        for k in range(1, upper_k + 1):
            # Create and train the model
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)
            
            # Get predictions and check accuracy
            predictions = knn.predict(X_test)
            acc = accuracy_score(y_test, predictions)
            
            print(f"  k={k} -> Accuracy: {acc:.4f}")
            
            # Update best k if this one is better
            if acc > max_accuracy:
                max_accuracy = acc
                best_k = k
        
        # --- 4. Final Result ---
        print("-" * 30)
        print(f"Done! The best k is {best_k} with an accuracy of {max_accuracy:.2%}")
        print("-" * 30)

    except ValueError:
        print("Error: Please make sure you enter numbers for features and integers for labels.")

if __name__ == "__main__":
    main()


# 
