import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('all_seasons.csv') 
print(data['player_height'].values) 
print(data['player_height'].dtypes) 

heights_list = data['player_height'].values.tolist() 

# FIVE-NUMBER-SUMMARY
height_df = pd.DataFrame(heights_list)
print(height_df.describe())

# BOXPLOT
fig = plt.figure(figsize = (10, 7))
plt.boxplot(heights_list)
plt.show()