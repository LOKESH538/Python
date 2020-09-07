'''2.	Draw correlation graph for mobile price with all attributes.'''
import pandas as pd
import matplotlib as plt
plt.rcParams.update({'figure.max_open_warning': 0})
data = pd.read_csv("mobile_cleaned-1549119762886.csv")
for col in data.columns:
    if(col != 'price'):
        data.plot(x='price',y=col)
