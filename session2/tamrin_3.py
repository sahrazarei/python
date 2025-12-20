#!/usr/bin/env python
# coding: utf-8

# In[3]:


pin = input("please type your code.")
try :
    number = int(pin)
    print(number , "its valueable")
    
except ValueError :
    print("please enter a number.")

