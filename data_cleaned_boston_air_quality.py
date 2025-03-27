import pandas as pd  
import numpy as np 




#load each DF individually 
df1 = pd.read_csv('/Users/michaelyu/Documents/boston_aqi_files/boston 2015-01-01 to 2017-01-01.csv')
df2 = pd.read_csv('/Users/michaelyu/Documents/boston_aqi_files/boston 2017-01-01 to 2019-01-01.csv')
df3 = pd.read_csv('/Users/michaelyu/Documents/boston_aqi_files/boston 2019-01-01 to 2021-01-01.csv')
df4 = pd.read_csv('/Users/michaelyu/Documents/boston_aqi_files/boston 2021-01-01 to 2023-01-01.csv')
df5 = pd.read_csv('/Users/michaelyu/Documents/boston_aqi_files/boston 2023-01-01 to 2025-01-01.csv')

# concat all DFs into one 
df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

print(df.head()) 

# make sure 'datetime' col is there before cleaning starts
if 'datetime' not in df.columns:
    raise KeyError("there is no 'datetime' column in the dataset!")


# Convert datetime and sort the DF
df['datetime'] = pd.to_datetime(df.get('datetime'), errors='coerce')  # Using .get() for safety
df = df.sort_values('datetime')


#which columns to data clean in files
cols_to_clean = ['windspeed', 'temp', 'cloudcover', 'snow', 'tempmax', 'windgust'] 


# check for missing vals in cols before smoothing 
print(df[cols_to_clean].isnull().sum())

# use coerce to any non-empty strings or special chars will be converted to NaN to prevent errors
df[cols_to_clean] = df[cols_to_clean].apply(pd.to_numeric, errors='coerce') 

# fill missing vals by carrying the last valid val to missing placeholders
df[cols_to_clean] = df[cols_to_clean].ffill()

print(df.head())

# rolling average to smooth fluctuations over 10 day average
# use 10 data points for more volatile data, feel free to use bigger number since bigger window is better for filtering  
for col in cols_to_clean:
    df[f'{col}_Smoothed'] = df[col].rolling(window=10, min_periods=1).mean()

#save newly cleaned dataset
df.to_csv('/Users/michaelyu/Documents/boston_aqi_files/newly_cleaned_boston_aqi_files.csv',index=False) 

# print last few rows of cleaned data 
print(df.tail())
