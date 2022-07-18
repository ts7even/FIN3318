import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Qt5Agg')

df1 = pd.read_csv('The_Basics/olympics.csv')


# Question 2: List the Edition, City, Athlete Name, and Medal columns. What type is this object?
df2 = df1[['City', 'Edition', 'Athlete', 'Medal']]
print('The dataframe consits of a "String Object" Exept for Edition which is a Interger...')


# Question 3: 
print(df2.head(5), '\n\n')

# Question 4: In which events did Micheal Phelps win a Medal> 
phelps_medal = df2[(df2['Athlete']=='PHELPS, Michael')]
print(phelps_medal, '\n\n')
print(f'The amount of medals that Micheal Phelps won: {phelps_medal.shape[0]}')


# Question 5: Display the female gold medal winners for the 100m track and field sprint event over the years.
female_track = df1[(df1['Sport']=='Athletics') & (df1['Gender']=='Women') & (df1['Event']=='100m')]
print(female_track, '\n\n')


# Question 6: Plot the number of medals achieved by the U.S. team (men and women) in Beijing 2008 using both Matplotlib and Seaborn.
us_medals = df1[(df1['City']=='Beijing') & (df1['Edition']==2008) & (df1['NOC']=='USA')]
female_us_medals = us_medals[(us_medals['Gender']=='Women')]
femaleMedals = female_us_medals.shape[0]
male_us_medals = us_medals[(us_medals['Gender']=='Men')]
maleMedals = male_us_medals.shape[0]

# Ploting With Matplotlib
height = (femaleMedals, maleMedals)
bars = ('Female', 'Male')
ypos = np.arange(len(bars))

plt.bar(ypos, height)
plt.title("Male and Female Medal Winners in the 2008 Beijing Olympics")
plt.xticks(ypos, bars)
plt.show()
plt.close()


# Ploting With Seaborn
sns.countplot(
    x='Medal',
    data=us_medals,
    hue='Gender'
)
plt.title('Male and Female Medal Winners in the 2008 Beijing Olympics')
plt.show()


# Question 7: Find 10 individual names who won the most medals. Do not discriminate between gold, silver, versus bronze
top10 = df1['Athlete'].value_counts().nlargest(10)
print(top10,'\n\n')



# Question 8: Find the names of 5 countries that won the most medals
top5countries = df1['NOC'].value_counts().nlargest(5)
print(top5countries, '\n\n')


# Question 9: Using groupby(), plot the total number of medals awarded at each of the Olympic games throughout history.
df1.groupby('Edition').size().plot()
plt.title('Total Number of Medals Awarded at each Olympic Games')
plt.show()


# Question 10: Creat a list showing the total number of Gold medals won for U.S., China, Mexico, Japan, France, and Canada. 
# For each country, include the year of the first and most recent Olympic medal wins.
gold_medal = df1[(df1['Medal']=='Gold')]
country = ['USA','CHN','MEX', 'JPN', 'FRA', 'CAN']

df3 = pd.DataFrame()
for c in country:
    medals = gold_medal[(gold_medal['NOC']==f'{c}')] 
    medal_count = medals.shape[0]
    first_medal = medals['Edition'].min()
    recent_medal = medals['Edition'].max()

    df2 = pd.DataFrame({
        "Country": [f'{c}'],
        "Total Gold Medals": [medal_count],
        "First Gold Medal": [first_medal],
        "Recent Gold Medal": [recent_medal]
    }, index=None)
    df3 = pd.concat([df3,df2],axis=0)
df3.reset_index(drop=True, inplace=True)        
print(df3, '\n\n')
