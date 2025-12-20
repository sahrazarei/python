#!/usr/bin/env python
# coding: utf-8

# In[43]:


names = ["John","Oscar","Jacob"]
file= open("names.txt","w+")
file.write("John\nOscar\nJacob")
file.close()
    
file= open("names.txt","r")
content = file.read()
print(content)
file.close()

