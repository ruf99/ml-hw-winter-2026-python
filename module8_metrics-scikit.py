#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # ---------------------------------------------------------
    # 1. DATA COLLECTION & INITIALIZATION
    # ---------------------------------------------------------
    try:
        n_str = input("Enter the number of points (N): ")
        N = int(n_str)
        
        if N <= 0:
            print("Please enter a positive integer for N.")
            return

        # We'll store (x, y) pairs where x = ground truth, y = predicted
        data_points = np.zeros((N, 2), dtype=int)

        # ---------------------------------------------------------
        # 2. DATA INSERTION
        # ---------------------------------------------------------
        for i in range(N):
            print(f"\nEntry {i + 1} of {N}:")
            x = int(input("  Enter ground truth class (0 or 1): "))
            y = int(input("  Enter predicted class (0 or 1): "))
            
            if x not in [0, 1] or y not in [0, 1]:
                print("Error: Labels must be binary (0 or 1). Restarting entry...")
                return main()

            data_points[i, 0] = x
            data_points[i, 1] = y

        # ---------------------------------------------------------
        # 3. COMPUTATION
        # ---------------------------------------------------------
        y_true = data_points[:, 0]
        y_pred = data_points[:, 1]

        # Precision: Aims to avoid false positives 
        # Recall: Aims to avoid false negatives
        precision = precision_score(y_true, y_pred, zero_division=0)
        recall = recall_score(y_true, y_pred, zero_division=0)

        # ---------------------------------------------------------
        # 4. OUTPUT RESULTS
        # ---------------------------------------------------------
        print("\n" + "="*30)
        print("   CLASSIFICATION REPORT")
        print("="*30)
        print(f"Precision: {precision:.2f}")
        print(f"Recall:    {recall:.2f}")
        print("="*30)

    except ValueError:
        print("Input error: Please ensure you enter valid integers.")

if __name__ == "__main__":
    main()


# In[ ]:




