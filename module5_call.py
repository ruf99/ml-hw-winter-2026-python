#!/usr/bin/env python
# coding: utf-8

# In[4]:


from module5_mod import Numbers

def main():
    # Initialize the OOP object - Numbers
    finder = Numbers()

    # Part 1: Ask for 'N' as user input
    try:
        n_input = int(input("Please provide a positive integer (N): "))
        
        # Part 2: Provide 'N' numbers  
        print(f"Please provide your {n_input} input(s): ")
        finder.insert_nums(n_input)

        # Part 3: Ask for 'X' and perform search  
        x_input = int(input("Please provide your input for 'X': "))
        result = finder.search_x(x_input)
        
        # Part 4: Printing final output
        print(result)
        
    except ValueError:
        print("Please ensure you enter integers only.")

if __name__ == "__main__":
    main()


# In[ ]:




