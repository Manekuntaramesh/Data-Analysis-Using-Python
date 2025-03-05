#!/usr/bin/env python
# coding: utf-8

# ### missing value

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_excel(r"C:\rock\dataset\DA-dataset\Iris_clean.xlsx")


# In[5]:


df.head()    # frist 5 values


# #### detecting the missing value 

# In[8]:


df.isna().sum()    # dataset 


# In[11]:


df['SepalLengthCm'].isnull().sum()   # single column


# In[12]:


df['SepalWidthCm'].isnull().sum()


# ### Treatment

# In[15]:


# using fillna 
df['SepalLengthCm'].fillna(5.1,inplace = True)


# In[16]:


df["SepalLengthCm"].isnull().sum()


# In[17]:


df['SepalWidthCm'].fillna(3.3,inplace = True)


# In[18]:


df['SepalWidthCm'].isnull().sum()


# In[20]:


df.columns


# In[21]:


df['PetalLengthCm'].fillna(2.2,inplace = True)


# In[22]:


df.isna().sum()


# In[26]:


#using mode - categorical 
df['Species'].fillna(df['Species'].mode()[0],inplace = True)


# In[27]:


df.isna().sum()


# In[28]:


df.head()


# In[29]:


df.isna().sum()


# ### outliers

# In[73]:


df = pd.read_csv(r"C:\rock\dataset\DA-dataset\titanic.csv")


# In[74]:


df.head()


# ### Using IQR 

# In[75]:


# check the missing value
df.isna().sum()


# In[76]:


df["Age"].fillna(df["Age"].median(),inplace = True)


# In[77]:


df['Embarked'].fillna(df['Embarked'].mode(),inplace = True)


# In[78]:


df.head()


# In[79]:


# using IQR


# In[80]:


df['Age'].isna().sum()


# In[81]:


Q1 = df['Age'].quantile(0.25)
Q2 = df['Age'].quantile(0.50)
Q3 = df['Age'].quantile(0.75)


# In[82]:


IQR = Q3 - Q1
Lower = Q1 - (1.5 * IQR)
Upper = Q3 + (1.5 * IQR)


# In[83]:


Lower 


# In[84]:


Upper


# In[85]:


# this time use your Domain Knowledge ...age 0 to 100 


# In[86]:


sum(df['Age'] < 0)


# In[87]:


sum(df['Age'] > 100)


# np.where(condition , first,same value)

# In[88]:


condition = (df['Age'] < 0)  |  (df['Age'] > 100)


# In[89]:


df['Age'] = np.where(condition,40,df['Age'])


# In[ ]:





# ### Detecting of duplicate values

# In[90]:


df.head()


# In[91]:


df.info()


# In[92]:


df.duplicated().sum()


# In[93]:


df.drop('PassengerId',axis = 1,inplace = True)


# In[95]:


df.drop_duplicates(keep = 'first',inplace = True)


# In[96]:


df.info()


# ### Typecasting

# In[97]:


df.head(4)


# In[98]:


df.info()


# In[99]:


df['Pclass'] = df['Pclass'].astype('object')


# In[100]:


df['Survived'] = df['Survived'].astype('object')


# In[102]:


df['Age'] = df['Age'].astype('float16')


# In[103]:


df.info()


# In[ ]:





# In[104]:


### multiple Dataset 


# In[ ]:


## Dummy variable


# In[2]:


df = pd.read_excel(r"C:\rock\dataset\DA-dataset\Sample_-_Superstore.xls",sheet_name=0)
df1 = pd.read_excel(r"C:\rock\dataset\DA-dataset\Sample_-_Superstore.xls",sheet_name=1)
df2 = pd.read_excel(r"C:\rock\dataset\DA-dataset\Sample_-_Superstore.xls",sheet_name=2)


# In[3]:


df.head()


# In[4]:


df1.head(3)


# In[5]:


df2.head(3)


# In[6]:


# unique
df1['Returned'].unique()


# In[7]:


df2['Region'].unique()


# In[8]:


df1['Returned'].nunique()


# In[9]:


df2['Region'].nunique()


# In[10]:


df['Discount'].var()


# In[11]:


df.describe()


# In[122]:


# onehot encoding--- No order


# In[13]:


pd.get_dummies(df['Region'],dtype = int , drop_first= True)


# In[14]:


df.head()


# In[15]:


# label encoding -- this data is follow order 


# In[16]:


role = ['DS','DA','DS','DS','DA','DE',"DE",'DS']
salaries = [80000,70000,80000,80000,70000,60000,60000,80000]


# In[18]:


sal = pd.DataFrame({'Role':role,
                'Salary':salaries})


# In[19]:


sal


# In[20]:


def ordinal(n):
    if n == 'DS':
        return 3
    elif n == 'DA':
        return 2
    else:
        return 1


# In[22]:


sal['Role'].apply(ordinal)


# In[ ]:




