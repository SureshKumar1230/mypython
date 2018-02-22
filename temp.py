# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing csv without header
import pandas as pd
import numpy as np
url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url,header=None)
print(df)


#Adding header
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers
print(df.head(4))


#basic insights of dataset
print(df.dtypes)


#
print(df.describe())


#provide full summary statistics
print(df.describe(include="all"))




print(df["symboling"])

#increse value

df["symboling"]=df["symboling"]+1

print(df["symboling"])


#drop  missing value in python

print(df.dropna())
df.dropna(subset=["price"],axis=0,inplace=True)

df=df.dropna(subset=["price"],axis=0)
df=df.dropna(subset=["normalized-losses"],axis=0)

print(df)

#replace missing value

mean=df["normalized-losses"].mean()
print(df["normalized-losses"].replace(np.nan,mean))











