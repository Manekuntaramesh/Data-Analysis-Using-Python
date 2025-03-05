#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ### Data Structures
# 
# * Series -- 1D (single line -- row and columns)
# * DataFrame -- 2D (row & columns)
# * Panel -- 3D (image)

# ### Series 
# *creation

# In[2]:


emplty = pd.Series()


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# In[4]:


#series


# In[5]:


type(emplty)


# In[6]:


age = list(range(30,50))


# In[7]:


np.array(age)


# In[8]:


pd.Series(age,dtype = 'int16')


# In[9]:


pd.Series(age,dtype = 'int16')


# In[10]:


age = list(range(30,50))


# In[11]:


age


# In[12]:


age = np.array(age)


# In[13]:


age


# In[14]:


pd.Series(age,dtype = 'int16')


# In[15]:


name = ('Rama','rajesh','radha','krishna')
name


# In[16]:


pd.Series(name,index = list(range(1,5)))


# In[17]:


salary = np.random.randint(30000,60000,20)


# np.random.randint

# In[18]:


de = np.random.randint(50,88,10)


# In[19]:


de


# In[20]:


marks = np.random.randint(40,100,25)


# In[21]:


marks


# In[22]:


salary


# In[23]:


pd.Series(salary,index = list(range(1,21)),dtype = 'int32')


# In[24]:


np.iinfo('int16')


# from dictionary

# In[25]:


students = {'A':'rajesh','B':'Ramesh','c':'Raj','d':'mahesh'}


# In[26]:


name = pd.Series(students)


# In[27]:


name.dtype


# In[28]:


name


# In[29]:


products = ['apple','Kiwi','watermelon',"Dragon Fruit",'Mango','Papaya','Mango','apple','Mango','apple','apple','Mango',]


# In[30]:


prd = pd.Series(products,index =list(range(1,13)))


# In[31]:


prd


# In[32]:


prd[1]


# In[33]:


prd.mode()


# In[34]:


prd.mode()[0]


# In[35]:


sal = np.array([61713, 73524, 66055, 72947, 61400, 71783, 50870, 67821, 70678,
       62569, 73002, 68181,61713, 73758, 74946, 65973, 69861,61713, 68444, 79342,
       78825, 72430])


# In[36]:


salary = pd.Series(sal)


# In[37]:


salary


# In[38]:


### Statstical measures


# In[39]:


salary.mean()


# In[40]:


salary.median()


# In[41]:


salary.std()


# In[42]:


salary.var()


# In[43]:


salary.max()


# In[44]:


salary.min()


# In[45]:


salary.quantile(0.25)


# In[46]:


salary.mean()


# In[47]:


salary.median()


# In[48]:


salary.var()


# In[50]:


salary.std()


# In[51]:


salary.quantile(0.25)


# In[52]:


salary.min(),salary.max()


# In[53]:


##Attributes


# In[54]:


salary.info()


# In[56]:


salary.head(2)


# In[57]:


salary.tail()


# In[59]:


salary.dtype


# In[60]:


salary.describe()


# In[61]:


salary.astype('float32')


# In[62]:


salary.memory_usage()


# In[64]:


salary.where(salary > 70000,0)


# In[66]:


salary.ndim


# In[67]:


salary.size


# In[68]:


salary.info()


# In[69]:


salary.dtype


# In[71]:


salary.astype('float32')


# In[81]:


salary.where(salary > 70000)


# In[82]:


salary.ndim


# In[83]:


salary.size


# In[85]:


salary.memory_usage()


# In[86]:


salary.describe()


# ### DataFrame

# In[87]:


#weather report


# In[88]:


strat = np.datetime64('2023-10-13')
end = np.datetime64('2023-10-19')


# In[92]:


dates = np.arange(strat,end,dtype = 'datetime64[D]')
dates


# In[93]:


temp= np.random.randint(20,40,6)
temp


# In[94]:


condition = ['cool','hot','snow','cool','snow','hot']


# In[95]:


pd.DataFrame({'Day':dates,
             'temp':temp,
             'report':condition})


# In[96]:


# importing the dataset


# In[111]:


get_ipython().system('pip install openpyxl')


# In[113]:


df = pd.read_excel(r"C:\rock\dataset\DA-dataset\Iris_clean.xlsx")


# In[114]:


df


# In[115]:


df.head()


# In[116]:


df.tail()


# In[117]:


df.describe()


# In[118]:


df.isna().sum()


# In[119]:


df.info()


# In[120]:


df.shape


# In[121]:


df.head()


# In[122]:


df.drop('Id',axis = 1,inplace = True)


# In[123]:


df


# In[125]:


df = df.drop('Species',axis = 1)


# In[126]:


df


# In[127]:


## Accesing row & columns


# In[130]:


df[['SepalLengthCm','SepalWidthCm','PetalLengthCm']]


# In[129]:


df['SepalWidthCm']


# In[131]:


df.head(2)


# In[133]:


df.head(9)


# In[134]:


df.loc[2:6]


# In[137]:


df.loc[6:9,['PetalLengthCm','SepalLengthCm']]


# In[138]:


#df.iloc


# In[139]:


df.head(4)


# In[141]:


df.iloc[3:6,1:3]


# In[142]:


df.iloc[1:10,1:2]


# In[143]:


# partice


# In[144]:


df = pd.read_excel(r"C:\rock\dataset\DA-dataset\Iris_clean.xlsx")


# In[145]:


df


# In[148]:


df.head(6)


# In[147]:


df.tail()


# In[149]:


df.describe()


# In[150]:


df.size


# In[152]:


df.mean()


# In[154]:


df.head()


# In[155]:


df.drop('Id',axis = 1,inplace = True)


# In[156]:


df


# In[157]:


df.drop("Species",axis = 1) 


# In[158]:


df


# In[163]:


df[['SepalLengthCm','SepalWidthCm']]


# In[164]:


df.loc[2:6]


# In[167]:


#df.loc[2:6,[column name]]


# In[168]:


df.iloc[2:6,0:2]


# In[169]:


# at , iat


# In[ ]:


-- single value--


# In[173]:


df.at[5,'SepalWidthCm'] = 3.4


# In[175]:


df.head(6)


# In[179]:


df.iat[1,0] = 2.3


# In[180]:


df


# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\manne\Downloads\loandata.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.info()


# In[8]:


df.describe(include = 'object')


# In[9]:


df.head()


# In[12]:


df.set_index('Loan_ID',inplace = True)


# In[13]:


df


# In[15]:


df['Gender'].value_counts()[1]


# In[17]:


df['Gender'].value_counts()[1]


# In[18]:


df.columns


# In[20]:


df['Married'].value_counts()[1]


# In[23]:


df['Education'].value_counts()[1]


# In[30]:


len(df[(df['Married'] == 'No') & (df['Education']=='Not Graduate')])


# In[33]:


len(df[(df['Married'] == 'No') & (df['Education'] == 'Not Graduate')])


# In[39]:


df[(df['Gender'] == 'Female') & (df['Married'] == 'No')]['ApplicantIncome'].mean()


# In[51]:


len(df[(df['Gender'] == 'Male') & (df['ApplicantIncome'] > df['ApplicantIncome'].mean())])


# In[56]:


df['Gender'].mode()[0]


# In[57]:


df.head(3)


# In[60]:


len(df[df['Loan_Amount_Term'] > 180])


# In[61]:


df.head(3)


# In[71]:


df[(df['Married'] == 'No') &  (df['Education'] == 'No Graduate')]


# In[70]:


df[(df['Married'] == 'Yes') & (df['Education'] == 'Graduate')]


# In[72]:


# cross tab


# In[74]:


pd.crosstab(index = df['Married'],columns=[df['Education'],df['Gender']],values = df['ApplicantIncome'],aggfunc = 'mean')


# In[75]:


df.sort_values('LoanAmount',ascending = False)


# In[76]:


# group by


# In[77]:


df.groupby(by = 'Gender')[['Education','Married']].count()


# In[81]:


df.groupby(by = 'Married')[['Gender','Education','Loan_Status']].count()


# In[82]:


df.groupby('Gender')[['Education','Married']].count()


# In[84]:


df.groupby(by = 'Gender')[['ApplicantIncome','LoanAmount']].agg([np.mean,np.std,np.max,np.min,np.median])


# In[85]:


df.groupby(by = 'Married')['Loan_Amount_Term'].agg([np.mean,np.max])


# In[90]:


df.pivot_table(index = 'Gender',columns = 'Married',aggfunc = 'max')


# In[89]:


import warnings
warnings.filterwarnings('ignore')

