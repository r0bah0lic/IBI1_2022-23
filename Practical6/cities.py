import pandas as pd
import matplotlib.pyplot as plt
chart=pd.DataFrame({
    'city':['Edinburgh','Glasgow','Stirling','London','Haining','Hangzhou','Shanghai','Beijing'],
    'country':['UK','UK','UK','UK','China','China','China','China'],
    'population':[0.56,0.62,0.04,9.7,0.58,8.4,29.9,22.2]
})
sorted=chart.sort_values(by='population') #sort by population
China_cities=list(sorted.loc[sorted['country'] == 'China', 'population']) #list populations by country
UK_cities=list(sorted.loc[sorted['country'] == 'UK', 'population'])
print('China cities:',China_cities)
print('UK cities:',UK_cities)
countries = chart['country'].unique() #
fig, ax = plt.subplots() #define x axis
for c in countries:
    country_data = chart[chart['country'] == c] #this sorts datas by countries
    ax.bar(country_data['city'], country_data['population'], label=country) #label the bars
ax.set_xlabel('City') #set names
ax.set_ylabel('Population')
ax.set_title('City Population by Country')
ax.legend()
plt.show()