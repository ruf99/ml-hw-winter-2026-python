#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

class knn_regr:
    def __init__(self):
        self.data = np.empty((0, 2))

    def insert_data(self, n):
        points = []
        for i in range(n):
            print(f"Point {i + 1}:")
            x = float(input("Enter x value: "))
            y = float(input("Enter y value: "))
            points.append([x, y])
        self.data = np.array(points)

    def calculate_knn(self, target_x, k):
        x_val = self.data[:, 0]
        y_val = self.data[:, 1]

        distances = np.abs(x_val - target_x)
        neighbour_indices = np.argsort(distances)[:k]

        prediction = np.mean(y_val[neighbour_indices])
        return prediction

def main():
    try:
        n = int(input("Enter the number of points (N): "))
        k = int(input("Enter the number of neighbours (k): "))

        if k > n:
            print(f"Error: k ({k}) cannot be greater than N ({n}).")
            return

        regressor = knn_regr()
        regressor.insert_data(n)

        target_x = float(input("Enter the X value to predict Y for: "))

        result = regressor.calculate_knn(target_x, k)
        print(f"\nThe predicted Y value for X={target_x} using {k}-NN is: {result}")

    except ValueError:
        print("Invalid input. Please ensure N and k are integers and coordinates are numbers.")

if __name__ == "__main__":
    main()


# In[ ]:




