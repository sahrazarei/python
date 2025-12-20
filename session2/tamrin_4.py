#!/usr/bin/env python
# coding: utf-8

# In[9]:


coffee = ["cafe latte" , "caffe americano" , "espresso" , "cappuccino" , "macchiato"]
choice = int(input("please enter a number"))
try :
    if 0 <= choice < 5 :
        print("your type of caffee:" , coffee[choice])
    else : 
        print("invalid number")
except :
    print("invalid number")
finally :
    print("Have a good day")

