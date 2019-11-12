# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:50:56 2019

@author: ravkumar8
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:05:11 2019

@author: ravkumar8
"""

#importing libraries
import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns


#from __future__ import print_function
#%matplotlib inline

import warnings


warnings.filterwarnings("ignore")


# importing the dataset
df=pd.read_csv("personalloan.csv", decimal = ',')

df.head()
df.shape

#finding the correlation between the variable
df.corr()

 
df= pd.get_dummies(df,columns =['Education'], drop_first=True)


df.corr()

df.head()
df.shape
#Changing the datatype of CCAvg from object to float
df["CCAvg"] = df.CCAvg.astype(float)
df.info()

#Checking if there are any null values

df.isnull().values.any()

df.isnull().sum()

df.describe()
df.corr()

def generateHeatMap(x):
    plt.figure(figsize=(16,12))
    sns.heatmap(data=df.corr(),annot=True,fmt='.2f',cmap='coolwarm')
    plt.show()
    
df

generateHeatMap(df)


# choose attributes which shows relation
p= df[['CCAvg','Age','Experience','Income','Family',
       'Mortgage','Personal Loan','CD Account','Education_2','Education_3']]

# show corr of the same
sns.heatmap(p.corr(), annot=True)

# choose attributes which shows relation
d= df[['CCAvg','Income','Family','Mortgage','Personal Loan','Education_2','Education_3']]

sns.pairplot(d)



