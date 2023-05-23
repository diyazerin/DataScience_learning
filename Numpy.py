#!/usr/bin/env python
# coding: utf-8

# # importing library

# In[1]:


import numpy as np


# # Array creation

# In[2]:


#1
a= np.array([1, 2, 3, 4, 5]) #creating a numpy array


# In[3]:


a


# In[16]:


type(a)


# In[7]:


#2
#a2= np.array([[1,2,3,4],[4,5,6,7]]) 
#2D array with arrange function and additional tools
a= np.arange(10)
a2= a.reshape(2,5)


# In[8]:


a2


# In[9]:


a2.ndim


# In[17]:


#3 creating 3D array with all ones
c= np.ones((3,4,3), dtype='int')


# In[18]:


c


# In[22]:


#4 
arr= np.arange(24) #arr= np.arange(0,24,1) (start,end(inclusive),step)

# Reshape the array into a 3D array with shape (2, 3, 4)
arr_3D = arr.reshape((2, 3, 4))


# In[23]:


arr_3D


# In[28]:


#5
arr= np.linspace(0, 1, 50, dtype='int')
arr2= np.linspace(0, 1, 50)    #float


# In[29]:


arr


# In[30]:


arr2


# In[33]:


#6
arr = np.arange(30).reshape(3,2,5)


# In[34]:


arr


# In[35]:


#7
arr = np.arange(1,41).reshape(5, 2, 4)
arr[2][0][1:3] = 0       #indexing+slicing
arr[2][1][1:3]= 0


# In[36]:


arr


# In[37]:


#8
# arr= np.arange(100).reshape(5, 2, 2, 5)
# new= array % 10 == 0
# arr[new] = 0           #arr[arr % 10 == 0]=0

arr1= np.arange(100).reshape(5, 2, 2, 5)
arr= np.where(arr1 % 10==0,0,arr1)
print(arr)


# In[39]:


#9
arr= np.arange(24).reshape(3, 2, 4)
print(arr)

odd= arr[arr % 2!= 0]
print("New array containing all odd numbers:")
print(odd)


# In[ ]:


#10
1.NumPy arrays are mostly used in scientific computing, especially in numerical simulations, data analysis 
  and machine learning algorithms.
2.NumPy arrays can have multiple dimensions, making it easy to manipulate multi-dimensional data structures.
3.NumPy arrays are more memory-efficient than Python's built-in arrays, which is good for handling large data.
4. NumPy provides numerous functions for array manipulation, such as slicing, indexing, sorting, and filtering. 
  These functions make it easy to manipulate arrays and extract the data required for analysis.

