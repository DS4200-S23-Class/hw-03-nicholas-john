import pandas as pd 
import matplotlib.pyplot as plt 
import datetime
from matplotlib import cm

if __name__ == "__main__":

    netflix_data = pd.read_csv(r"/Users/bongo/Documents/DS_4200/Hw3/hw-03-nicholas-john/NetFlix.csv")
    netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'])

    netflix_data = netflix_data.loc[netflix_data['type'] == 'Movie']
    netflix_data = netflix_data.loc[netflix_data['date_added'] > datetime.datetime(2021, 1, 1)]
    netflix_data.reset_index(inplace=True)

    date = netflix_data['date_added']
    run_time = netflix_data['duration']
    ratings = netflix_data['rating']
    color_dict = {'R': 'Magenta', 'TV-14': 'yellow', 'PG-13': 'orange', 'TV-MA': 'red', 'TV-G': 'Green',
              'TV-Y': 'blue', 'TV-PG': 'purple', 'G': 'brown', 'TV-Y7': 'Teal', 'PG': 'maroon'}
    color_lst = [color_dict[rating] for rating in ratings]


    fig, ax = plt.subplots()

    scatter = ax.scatter(data=netflix_data, x='date_added', y='duration', color=color_lst)
    markers = [plt.Line2D([0, 0], [0, 0], color=color, marker='o', linestyle='') for color in color_dict.values()]
    plt.legend(markers, color_dict.keys(), numpoints=1, title='Movie Rating', loc='upper left')
    plt.xticks(rotation='45')
    plt.title('Has Netflix started adding longer movies to its Collection in the last few Years?')
    plt.xlabel('Date Movie was Added')
    plt.ylabel('Duration of the Movie in Minutes')
    plt.show()










