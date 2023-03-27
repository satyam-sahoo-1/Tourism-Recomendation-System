import pandas as pd
import random
import numpy
from scipy import spatial

l_type=['Funny','Travel','Food','Fashion','News','Funny','Sports','Motivational','Music','Dance' ]
l_location=['Odisha', 'Delhi', 'Maharastra', 'Assam', 'Rajastrhan', 'West-Bengal']
types = [random.choice(l_type) for i in range(1000)]
location=[random.choice(l_location) for i in range(1000)]
data = {
    "Location": location,
    "types":types
}
df = pd.DataFrame(data)
df.to_csv('ReelType.csv', mode='w')
# df


df_new = df[df['types'] == 'Travel']
df_new
l_travel = df_new['Location'].tolist()
df_new.groupby('Location').size()
# print(l_travel)



# Load the data
tourist_data = pd.read_csv('TouristSpots.csv')
place = input('enter' )
# Define the user preferences
d = random.choice(l_travel)
destination = d
duration = '5 days'
budget = 50000

# Filter the tourist data based on the destination and preferred activities
filtered_data = tourist_data[(tourist_data['States'] == destination)]

# Sort the filtered data by rating and price
sorted_data = filtered_data.sort_values(by=['rating', 'price'], ascending=False)

# Select the top recommendations based on the budget
#top_recommendations = sorted_data[sorted_data['price'] <= budget].head(3)
def recommend_place(place, data=filtered_data):
  if tourist_data[tourist_data['States']== place].shape[0] == 0:
    print('This placce is either not so popular or you\have entered invalid_name.\n Some songs you may like:\n')

    for place in data.sample(n=5)['States'].values:
      print(place)
    return

  data['similarity_factor']= cosine_similarity(place, data)
  
  data.sort_values(by=['similarity_factor','rating'],ascending=[False, False],inplace=True)
  display(data[['States']])

recommend_place(place)
# # Print the recommendations
# print("Top 3 recommendations for your trip to \"", destination, "\" are:")
# price = 0
# NoOfDays = 0
# for index, row in top_recommendations.iterrows():
#   price = price + row['price']
#   NoOfDays = NoOfDays + row['duration']
#   print(row['places'], "- Rating:", row['rating'], "- Price:",row['price'])

# print("\nThe tour will be of", int(NoOfDays), "days and it will cost around Rs.",price,".")