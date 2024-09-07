mport pandas as pd
import matplotlib.pyplot as plt

# The task is to find the most frequent movie duration in the 1990s and count the number of short action movies released in the 1990s
netflix_df = pd.read_csv("netflix_data.csv")

subset_movies = netflix_df[netflix_df['type'] == 'Movie']

plt.hist(films_1990s['duration'])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

action_movies = films_1990s[films_1990s['genre'] == 'Action']  

# Count the number of short movies (duration < 90)
short_movie_count = 0

for label, row in action_movies.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1
    else:
         short_movie_count = short_movie_count
        

print(short_movie_count)
