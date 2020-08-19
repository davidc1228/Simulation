#!/usr/bin/env python
# coding: utf-8

# # Assignament I

# In[17]:


from IPython.display import Image
Image(filename='captura.png')


# In[2]:


n = int(input())
L1=1
L2=3
print(L1)
print(L2)
for i in range(n-2):
  L = L2 + L1
  L1 = L2
  L2 = L
  print(L)


# In[ ]:





# In[ ]:




