#!/usr/bin/env python
# coding: utf-8

# In[25]:


file= open("pull_up.txt" , "w")
file.write("5\n6\n7\n8\n9")
file.close()


# In[34]:


file= open("pull_up.txt" , "r")
lines = file.readlines()
file.close()
n = int(input("type a number"))
for day in range(n+1) :
    pull_ups = lines[day]
    print("day", day , "=" , pull_ups)

