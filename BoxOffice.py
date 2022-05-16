import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice

df = pd.read_csv("BoxOfficeCollections.csv")
## no dpuplicates! hooray print(df[df.duplicated()])

# changing column title because I want to have the cases in the different IMDB rows matching
df.rename(columns={'Imdb_genre': 'IMDB Genre'}, inplace=True)
my_colors = list(islice(cycle(['blue', 'red', 'green', 'yellow', 'grey', 'purple']), None, len(df)))
"""
print("List of column headers: ", list(df.columns.values))
print("The start year for this dataset is: ", df['Year'].min())
print("The end year for this dataset is: ", df['Year'].max())
print("The average IMDB rating is: ", df['IMDB Rating'].mean())
print("The average movie length in minutes, is: ", df['time_minute'].mean())
print("The most frequently produced genre is: ", df['IMDB Genre'].mode())
"""

'''
#comedy is the most frequently produced type of movie
occur = df.groupby(['IMDB Genre']).size()
occur.plot(kind= 'bar', title='Most frequently made movie', xlabel='Genre', ylabel='Number of Times Produced',
           figsize= (10,5), width= 0.5)
plt.show()
'''
'''
#despite comedy being the most commonly made movie, drama has the highest average critic rating - its very close though
c_ratings = df[['IMDB Genre', 'Score']]
Critics_Rating = c_ratings.groupby(['IMDB Genre'])['Score'].mean()
Critics_Rating.plot(kind='bar', title='Highest Rated Genre(Critic Average)', xlabel='Genre', ylabel='Score out of 100',
                    figsize=(10, 5), width=0.5, color=my_colors)
plt.show()
'''

'''
#drama also has the highest average public rating. Key Insight: the pbulic's opinion seems to match critic ratings. Also very close
p_ratings = df[['IMDB Genre', 'IMDB Rating']]
Public_Rating = p_ratings.groupby(['IMDB Genre'])['IMDB Rating'].mean()
Public_Rating.plot(kind='bar', title='Highest Rated Genre(Public Average)', xlabel='Genre', ylabel='Score out of 10',
                    figsize=(10, 5), width=0.5, color=my_colors)
plt.show()
'''

'''
#Sci Fi is the biggest bread winner on average. Key Insight: Drama is second lowest, despite the highest ratings on average
#Adventure is second highest. Seems like people spend more money on movies they don't have to engage with as critically

revenue = df[['IMDB Genre', 'Box Office Collection']]
pd.set_option('display.float_format', lambda x: f'%.{len(str(x%1))-2}f' % x)
money = revenue.groupby(['IMDB Genre'])['Box Office Collection'].mean()
money.plot(kind='bar', title='Average Revenue of Movie Genre', xlabel='Genre', ylabel='Revenue (in 100M)',
                    figsize=(10, 5), width=0.5, color=my_colors)
plt.show()
'''

dated = df[['Year', 'Box Office Collection']]
year_money_made = dated.groupby(['Year'])['Box Office Collection'].max()
year_money_made.plot(kind='bar', title='Year with the Most Money Made', xlabel='Genre', ylabel='Revenue (in 100M)',
                    figsize=(10, 5), width=0.5, color=my_colors)
#plt.show()

#Avengers: Endgame has earned the most money - but Zooptopia is listed if i use max
movie_gross = df[['Movie', 'Box Office Collection', 'Year']]
#print(movie_gross['Box Office Collection'].nlargest(n=10))

print("The Top 10 Highest Grossing movies are: ", movie_gross.loc[[399]], movie_gross.loc[[388]], movie_gross.loc[[395]],
      movie_gross.loc[[894]], movie_gross.loc[[939]], movie_gross.loc[[930]], movie_gross.loc[[637]], movie_gross.loc[[328]],
      movie_gross.loc[[928]], movie_gross.loc[[915]])