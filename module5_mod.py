#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Numbers:
    def __init__(self):
        self.data = []

    def insert_nums(self, n):
        # This is the data insertion logic: reads n numbers from the user
        for i in range(n):
            val = int(input(f"Enter input #{i + 1}: "))
            self.data.append(val)

    def search_x(self, x):
        # This is the data search logic: returns 1-based index or -1 if n/a
        if x in self.data:
            return self.data.index(x) + 1
        return -1

