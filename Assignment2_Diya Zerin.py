#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


#1
df = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\banking.csv")
#df.info()
pd.set_option('display.max_columns', None)

print("Last 3 rows of every column:")
print("")
print(df.tail(3))


# In[5]:


#2
data = {'name': ['a', 'b', 'c', 'd', 'e'],
        'age': [20, 17, 32, 45, 15]}
df = pd.DataFrame(data)

average_age = df['age'].mean()
max_age = df['age'].max()
min_age = df['age'].min()

print("Average age:", average_age)
print("Maximum age:", max_age)
print("Minimum age:", min_age)
df


# In[8]:


#3
data = {'name': ['a', 'b', 'c', 'd', 'e'],
        'age': [71, 17, 32, 45, 15]}

# data = {'name': ['a', 'b', 'c', 'd', 'e', 'f'],
#         'age': [71, 17, 32, 45, 15, 18]}  

df = pd.DataFrame(data)
df['new_column'] = df['age'].apply(lambda x: 'yes' if x > 18 else 'no')
#df.head()   #shows 1st five values
df     #for whole


# In[9]:


#4
data = {'name': ['a', 'b', 'c', 'd', 'e'],
        'age': [71, 17, 32, 45, 15],
        'new_column': ['yes', 'no', 'yes', 'yes', 'no']}

df = pd.DataFrame(data)
df['new_column'] = df['new_column'].apply(lambda x: 1 if x == 'yes' else 0)
df


# In[14]:


#5
data = pd.DataFrame({'color': ['red', 'blue', 'green', 'blue', 'red']})
#data = pd.DataFrame({'color': ['red', 'blue', 'green', 'blue', 'red','red']})

dm = pd.get_dummies(data['color'])
result = dm.rename(columns=lambda x: 'color_' + x)
print(result)


# In[17]:


#6
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\banking.csv")

married_loans = df.query('marital== "married" and loan== "yes"')
#married_loans = data[(data["marital"]== "married") & (data["loan"] == "yes")]
count = married_loans.shape[0]

print("Number of people who are married and getting their loans:", count)


# In[23]:


#7
data = {'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        'salary': ['10020', None, '15500', None, None, '18200', '25300', '12500']}
df = pd.DataFrame(data)

average_salary = pd.to_numeric(df['salary'], errors='coerce').mean()
df['salary'] = df['salary'].fillna(average_salary)    #replace
df['salary'] = df['salary'].astype(int)

print(df)


# In[25]:


#8
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\banking.csv")

min_age_married = df[df['marital']== 'married']['age'].min()
min_age_loans = df[df['loan']== 'yes']['age'].min()

print("Minimum age when people are getting married:", min_age_married)
print("Minimum age when people are getting loans:", min_age_loans)


# In[28]:


#9
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\banking.csv")

marital_data = df[df['marital'].isin(['single', 'divorced'])]
loan_data = marital_data[marital_data['loan'] == 'yes']
count = loan_data.shape[0]
#total_count1 = marital_data.shape[0]

divorced_count = marital_data[marital_data['marital'] == 'divorced'].shape[0]
total_count = df.shape[0]
divorce_rate = (divorced_count / total_count) * 100

print("Number of people who are single or divorced and getting loans:", count)
print("Divorce rate in the dataset: {:.2f}%".format(divorce_rate))


# In[ ]:




