#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("p000001.csv")
df


# In[3]:


df.columns


# In[4]:


df[[' HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2',
       'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
       'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine', 'Bilirubin_direct',
       'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
       'Bilirubin_total', 'TroponinI', 'Hct', 'Hgb', 'PTT', 'WBC',
       'Fibrinogen', 'Platelets', 'Age',
       'HospAdmTime', 'ICULOS', 'SepsisLabel']].hist(bins=20,figsize=(15,15))
plt.show()
      


# In[5]:


df.describe()


# In[3]:


import seaborn as sns


# In[5]:


sns.pairplot(df[[' HR', 'O2Sat', 'Temp', 'SBP', 'MAP','SepsisLabel']],hue='SepsisLabel',diag_kind='kde',kind='scatter',palette='husl')
plt.show()


# In[6]:


sns.pairplot(df[['FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
       'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine','SepsisLabel']],hue='SepsisLabel',diag_kind='kde',kind='scatter',palette='husl')
plt.show()


# In[8]:


sns.pairplot(df[['Bilirubin_direct',
       'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
       'Bilirubin_total', 'TroponinI', 'Hct', 'Hgb','SepsisLabel']],hue='SepsisLabel',diag_kind='kde',kind='scatter',palette='husl')
plt.show()


# In[9]:


sns.pairplot(df[['PTT', 'WBC',
       'Fibrinogen', 'Platelets', 'Age',
       'HospAdmTime', 'ICULOS','SepsisLabel']],hue='SepsisLabel',diag_kind='kde',kind='scatter',palette='husl')
plt.show()


# In[ ]:




