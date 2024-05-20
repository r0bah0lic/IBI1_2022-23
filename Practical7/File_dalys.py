import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/20815/Desktop/IBI1_2023-24/Practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
task1=dalys_data.iloc[0:100:10, 3] #Show the fourth column from every 10th row for the first 100 rows
print(task1)
boo = dalys_data['Entity'] == 'Afghanistan' #Used a Boolean to show DALYs for all rows corresponding to Afghanistan
task2 = dalys_data.loc[boo,"DALYs"]
print(task2)
china_data = dalys_data.loc[dalys_data['Entity']=='China'] #Computed the mean DALYs in China
print(china_data)
mean = int(china_data['DALYs'].mean())
the19 = int(china_data[china_data['Year'] == 2019]['DALYs'])
if mean >= the19: #Stating is the mean or the daly of 2019 higher
    print('mean is higher')
if mean <= the19:
    print('mean is lower')
plt.plot(china_data['Year'], china_data['DALYs'],'b+') #Draw plot figure
plt.xticks(china_data.Year,rotation=-90)
plt.show()