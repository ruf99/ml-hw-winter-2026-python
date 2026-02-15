#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Numbers:
    def __init__(self):
        self.numbers = []

    def insert_data(self, n):
        print(f"Please provide your {n} input(s) of positive integer(s): ")
        for i in range(n):
            val = int(input(f"Enter input #{i + 1}: "))
            self.numbers.append(val)

    def search_data(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1

def main():
    # Part 1 - Asking for user input
    n_str = input("Please provide an input of a positive integer (N): ")
    n = int(n_str)
    
    # Part 2 - Initializing the class itself
    finder = Numbers()
    
    # Part 3 - Updating list with inputs
    finder.insert_data(n)
    
    # Part 4 - Let's find 'X'
    x_input = int(input("Please provide your input for 'X': "))
    result = finder.search_data(x_input)
    
    # Part 5 - Printing the result
    print(result)

if __name__ == "__main__":
    main()


# In[ ]:




