#!/usr/bin/env python
# coding: utf-8

# In[47]:


file = open("books.txt" , "w")
file.write("some book\nAnother book")
file.close()

file = open("books.txt" , "r")
lines = file.readlines()
file.close()

for line in lines :
    line = line.strip()
    if line :
        code = line[0] + str(len(line))
        print(code)

