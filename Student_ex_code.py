#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("stu_ex.csv")
print(df.head())


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# **drop unnamed column**

# In[8]:


df = df.drop("Unnamed: 0", axis = 1)
print(df.head())


# **change weekly study hrs**

# In[10]:


df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-oct","5-10")
df.head()


# In[11]:


#gender distrubtion


# In[21]:


plt.figure(figsize = (4,3))
ax =  sns.countplot(data = df, x = "Gender" )
ax.bar_label(ax.containers[0])
plt.title("Gender Distrubution")
plt.show()


# In[16]:


#from the above we have analysed that: 
#the numbers of females in the data is more than the numbers of males


# In[17]:


gb = df.groupby("ParentEduc").agg({"MathScore": 'mean', "ReadingScore": 'mean', "WritingScore":'mean'})
print(gb)


# In[22]:


plt.figure(figsize= (5,5))
sns.heatmap(gb, annot = True)
plt.title("Parent Education")
plt.show()


# In[19]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": 'mean', "ReadingScore": 'mean', "WritingScore":'mean'})
print(gb1)


# In[23]:


plt.figure(figsize= (5,5))
sns.heatmap(gb1, annot = True)
plt.title("Parent Marital Status")
plt.show()


# In[24]:


#from the above chart there is no / negligible empact on the 
#students score due to their parants marital status on the students score cards 


# In[25]:


sns.boxplot(data = df, x = "MathScore")
plt.show()


# In[26]:


sns.boxplot(data = df, x = "ReadingScore")
plt.show()


# In[27]:


sns.boxplot(data = df, x = "WritingScore")
plt.show()


# In[28]:


print(df["EthnicGroup"].unique())


# In[29]:


#Distribution of Ethnic Grups


# In[36]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count();
print(groupA)


# In[37]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count
print(groupA)


# In[39]:


groupB = df.loc[(df['EthnicGroup'] == "group B")].count();E
print(groupB)


# In[45]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count();
groupB = df.loc[(df['EthnicGroup'] == "group B")].count();
groupC = df.loc[(df['EthnicGroup'] == "group C")].count();
groupD = df.loc[(df['EthnicGroup'] == "group D")].count();
groupE = df.loc[(df['EthnicGroup'] == "group E")].count();

l = ["group A", "group B", "group C", "group D", "group E"] 
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist , labels = l, autopct = "%1.2f%%" )
plt.title("Distribution of Ethnic Group")
plt.show()


# In[46]:


ax = sns.countplot(data = df, x= 'EthnicGroup')
ax.bar_label(ax.containers[0])


# In[ ]:




