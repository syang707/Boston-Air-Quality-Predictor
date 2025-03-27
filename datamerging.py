#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 19:52:17 2025

@author: sarah
"""
#panda dict
import pandas as pd

#path
path= ["/Users/sarah/Desktop/CS506 project/boston_2015-01-01_to_2017-01-01.csv","/Users/sarah/Desktop/CS506 project/boston_2017-01-01_to_2019-01-01.csv",
    "/Users/sarah/Desktop/CS506 project/boston_2019-01-01_to_2021-01-01.csv",
    "/Users/sarah/Desktop/CS506 project/boston_2021-01-01_to_2023-01-01.csv",
    "/Users/sarah/Desktop/CS506 project/boston_2023-01-01_to_2025-01-01.csv",]

#col to keep
column_keep= ['datetime','precip','preciptype','precipcover','windspeed','tempmin','temp','humidity','cloudcover','snow','tempmax','windgust']

#read and merging csv
read=[]
for file in path :
    r= pd.read_csv(file, usecols=column_keep, parse_dates=["datetime"])
    read.append(r)
  
merge= pd.concat(read,ignore_index=True)
#sort in correct order
merge=merge.sort_values(by="datetime").reset_index(drop=True)
    
#uniquw years
merge["year"]=merge["datetime"].dt.year
unique=sorted(merge["year"].unique())


#split data into 8 year->training 
#split 2 year-> testing
eight=unique[:8]
two=unique[-2:]

#spliting data into training and testing
train=merge[merge["year"].isin(eight)]
test=merge[merge["year"].isin(two)]

#saving data for training and testing
train.to_csv("train.csv",index=False)
test.to_csv("test.csv",index=False)

#merging of train and testing
combine= pd.concat([train,test],ignore_index=True)
#all in one csv
combine.to_csv("combiningtrainandtest.csv", index=False)



print(train["year"].unique()) 
print(test["year"].unique())   








