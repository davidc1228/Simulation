#!/usr/bin/env python
# coding: utf-8

# # Assignament I

# In[17]:


from IPython.display import Image
Image(filename='captura.png')


# In[7]:


import matplotlib.pyplot as plt
import time 
n = int(input())
L1=1
L2=3
x=[]
y=[]
print(L1)
print(L2)
start = time.time()
for i in range(n-2):
  L = L2 + L1
  L1 = L2
  L2 = L
  print(L)
  x.append(i)
  y.append(L) 
end = time.time()
plt.plot(x, y)
plt.show()
print('time: ', end - start)
    
    

