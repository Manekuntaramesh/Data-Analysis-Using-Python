#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ### Stastical Methods

# In[4]:


salaries = np.array([20000,40000,60000,34000,65000,96000,1000000])


# ### Mesaure of central tendency 

# In[5]:


#mean
np.mean(salaries)


# In[6]:


#median
np.median(salaries)


# ### Mesaure of spread

# In[7]:


#range
np.min(salaries)


# In[8]:


np.max(salaries)


# In[9]:


range1 = np.max(salaries) -np.min(salaries)


# In[10]:


range1


# In[11]:


np.var(salaries)


# In[12]:


np.std(salaries)


# ### IQR

# In[13]:


salaries


# In[14]:


q1 = np.percentile(salaries,25)
q1


# In[15]:


q2 = np.percentile(salaries,50)
q2


# In[16]:


q3 = np.percentile(salaries,75)
q3


# In[17]:


IQR = q3 - q1
IQR


# In[18]:


lower = q1 - (1.5 * IQR)
lower


# In[19]:


upper = q3 + (1.5 * IQR)
upper


# In[20]:


salaries


# In[21]:


salaries[salaries > upper]


# In[1]:


import numpy as np


# ### Linear Algebra 

# 2x - 3y + 5z = 13
# 
# 3x + 2y - 6z = 17
# 
# 5x + 4y - 4z = 21

# In[3]:


a = np.array([[2,-3,5],[3,2,-6],[5,4,-4]])
a


# In[5]:


b = np.array([13,17,21])
b


# In[6]:


np.linalg.solve(a,b)


# In[7]:


2 *  5.33333333 - 3* (-2.375) + 5 * (-0.9) 


# In[8]:


a


# In[9]:


np.linalg.inv(a)   # inverse matix


# In[10]:


np.linalg.det(a)


# In[12]:


c = np.array([[100,2,-3,4],[21,20,4,80],[1,-10,-40,1],[0,10,-3,0]])
c


# In[14]:


d = np.array([200,2,120,100])
d


# In[17]:


np.linalg.solve(c,d)


# In[20]:


np.linalg.det(c)


# In[23]:


s,v,d = np.linalg.svd(c)


# In[24]:


s


# In[25]:


v


# In[26]:


d


# In[7]:


l =np.random.randint(1,30,12).reshape(4,3)


# In[3]:


np.random.randint(2,30,10).reshape(5,2)


# In[6]:


np.random.randint(2,30,12).reshape(3,4,1)


# In[8]:


l


# ### stacking and splitting

# In[9]:


arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[30,40,50],[60,70,80],[80,89,99]])


# In[11]:


np.stack((arr1,arr2))   # joined two array


# In[12]:


np.stack((arr1,arr2))


# In[13]:


np.stack((arr1,arr2))


# In[14]:


np.hstack((arr1,arr2))


# In[15]:


np.hstack((arr1,arr2))


# In[16]:


np.hstack((arr1,arr2))


# In[17]:


np.dstack((arr1,arr2))


# In[18]:


np.concatenate((arr1,arr2))


# In[19]:


np.concatenate((arr1,arr2))


# In[20]:


np.vstack((arr1,arr2))


# In[21]:


np.stack((arr1,arr2))


# In[27]:


np.append(arr1,arr2,axis = 1)


# In[28]:


arr1


# In[29]:


arr2


# stacking

# In[30]:


np.stack((arr1,arr2))


# In[31]:


np.vstack((arr1,arr2))


# In[32]:


np.hstack((arr1,arr2))


# In[33]:


np.dstack((arr1,arr2))


# In[34]:


np.concatenate((arr1,arr2))


# In[36]:


np.append(arr1,arr2,axis = 0)


# In[37]:


#splitting


# In[38]:


arr1


# In[41]:


np.split(arr1,3)


# In[43]:


np.split(arr2,3)


# In[45]:


arr4 = np.arange(1,13).reshape(4,3)


# In[46]:


arr4


# In[49]:


np.split(arr4,4)


# In[50]:


arr4


# In[53]:


np.array_split(arr4,3)


# In[55]:


np.array_split(arr4,5)


# ### constants

# In[56]:


np.pi


# In[58]:


np.array([1,2,3]) / 0


# In[59]:


np.inf


# In[60]:


np.nan


# In[61]:


ages = np.random.randint(20,60,30)


# In[62]:


ages


# In[65]:


ages =np.array([51, 27, 35, 30, 55,'nan', 23, 21, 43, 35, 34, 45, 25, 41, 49,'nan', 42, 37, 50, 49, 34, 30, 43, 59, 57, 37,600, 59,'nan',40, 20, 25, 24, 47])


# In[91]:


ages


# In[67]:


# np.where 


# In[71]:


arr1 = np.array([np.where(ages =='nan',50,ages)],dtype='int16')


# In[72]:


arr1


# In[77]:


arr = np.array([np.where(ages=='nan',50,ages)])


# In[82]:


np.array([np.where(ages == "nan",50,ages)])


# In[83]:


np.where(ages == 'nan',50,ages)


# In[85]:


arr = np.array([np.where(ages == 'nan',50,ages)])


# In[86]:


arr


# In[90]:


arr


# In[104]:


ages = np.array([46, 51, 'nan', 3, 49, 44,'nan', 43, 42, 27, 53, 51, 45, 42, 44, 4000, 34,
       57, 43, 53, 42, 41, 48, 49, 51, 151, 53, 55, 50, 45])


# In[105]:


ages


# In[98]:


np.isnan(ages).sum()


# In[99]:


# isnan -- find the missing values


# In[106]:


ages


# In[111]:


arr4 = np.array([np.where(ages == 'nan',50,ages)])


# In[112]:


arr4


# In[117]:


ages = np.array([46, 51, np.nan, 3, 49, 44, np.nan, 43, 42, 27, 53, 51, 45, 42, 44, 4000, 34,
       57, 43, 53, 42, 41, 48, 49, 51, 151, 53, 55, 50, 45])


# In[119]:


np.isnan(ages)


# In[120]:


ages = np.where(np.isnan(ages),50,ages).astype('int16')


# In[121]:


ages


# In[ ]:


ages = np.where(np.isnan(ages),50,ages).astype('int16')


# In[ ]:





# In[113]:


# outlier


# In[122]:


ages


# In[127]:


cond = (ages  > 100) | (ages < 20)
cond


# In[128]:


np.sum(cond)


# In[130]:


np.where(cond,40,ages)


# In[132]:


ages


# In[133]:


out = (ages  > 100) | (ages < 20)


# In[134]:


out


# In[136]:


ages = np.where(out,40,ages)


# In[137]:


ages


# In[138]:


#view & copy


# In[139]:


a = np.array([1,2,3,4,5,6])


# In[140]:


a


# In[142]:


b = a.view()


# In[143]:


b


# In[144]:


b[4] = 9


# In[145]:


b


# In[146]:


a


# In[147]:


a


# In[148]:


b = a.copy()


# In[149]:


b


# In[150]:


b[5] =10


# In[151]:


b


# In[152]:


a


# In[153]:


#ravel & flatten


# In[155]:


arr5 = np.array([[1,2,3],[3,5,7],[9,3,5]]).reshape(3,3)


# In[156]:


arr5


# In[157]:


arr5.ndim


# In[158]:


a = np.ravel(arr5)


# In[159]:


a


# In[160]:


a[4] = 200


# In[161]:


arr5


# In[162]:


b  = arr5.flatten()


# In[163]:


b


# In[164]:


b[4] =8


# In[165]:


b


# In[166]:


arr5


# In[167]:


# csv files using the numpy


# In[172]:


salary = np.genfromtxt(r"C:\Users\manne\Downloads\salary.csv",dtype = 'int32',delimiter =",")


# np.genfromtxt()   # numpy to load the data

# In[178]:


sal = salary[1:,1]


# In[179]:


sal


# In[175]:


salary


# In[180]:


sal = np.where(sal ==-1,np.nan,sal)


# In[181]:


sal


# In[184]:


np.nanmean(sal)


# In[186]:


np.nanmax(sal)


# In[187]:


a = np.where(np.isnan(sal),np.nanmean(sal),sal)


# In[188]:


a


# In[189]:


# isung numpy to load the data 


# In[219]:


a = np.genfromtxt(r"C:\Users\manne\Downloads\salary.csv",dtype ='int16',delimiter=',')


# In[220]:


a


# In[215]:


salary  = data[1:,1]


# In[216]:


salary


# In[198]:


salary = np.where(salary == -1 , np.nan , salary)


# In[199]:


salary


# In[200]:


# if you replace any missing values the trearment is RRR - replace , retain,remove 


# In[212]:


men = np.nanmean(salary)


# In[210]:


salary = np.where(np.isnan(salary) , men,salary)


# In[211]:


salary 


# In[205]:


# sorting


# In[206]:


salary 


# In[221]:


np.sort(salary)


# In[222]:


salary


# In[223]:


np.savetxt('sal.txt',salary)


# In[224]:


# load


# In[226]:


np.loadtxt('sal.txt')


# In[227]:


#Task


# In[228]:


data = np.genfromtxt(r"C:\Users\manne\anaconda3\ds\pkgs\scikit-learn-1.4.2-py311hf62ec03_1\Lib\site-packages\sklearn\datasets\data\iris.csv",dtype = "int16",delimiter = ',')


# In[229]:


data


# In[230]:


sepal_length = data[:3]


# In[231]:


sepal_length


# In[232]:


np.mean(sepal_length)


# In[235]:


np.sort(sepal_length)


# In[236]:


np.savetxt('cleaned_iris.txt',sepal_length)


# In[237]:


np.loadtxt('cleaned_iris.txt')


# In[ ]:




