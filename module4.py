#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Part 1
print("Please provide an input of a positive integer (N): ")
userInput_P1 = input('>')
print("Your input is: " + userInput_P1)

arr = [0] * int(userInput_P1)


# In[2]:


#Part 2
loop = 1
print("Please provide your " + userInput_P1 + " input(s) of positive integer(s) (N): ")
for i in range(int(userInput_P1)):
    print("Enter input #", + i+1)
    userInput_P2 = input('>')
    arr[i] = int(userInput_P2)


# In[15]:


#Part 3
print("Please provide your input for 'X': ")
userX = int(input('>'))

if userX in arr:
    print(f"{arr.index(userX) + 1}")
else:
    print("-1")


# In[ ]:




