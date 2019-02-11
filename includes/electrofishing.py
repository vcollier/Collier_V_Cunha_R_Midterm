import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import csv
import tkinter

with open('data/traa_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

hfont = {'fontname':'Lato'}

years = [2016, 2017, 2018]

labels = ["Komoka", "Oxbow", "Dingman"]

k_fishes = [15.0, 14.0, 23.0]
o_fishes = [10.0, 18.0, 12.0]
d_fishes = [13.0, 15.0, 14.0]

plt.legend(loc='upper left')
plt.plot(years, k_fishes, color='firebrick', linewidth=6.0, label='komoka')
plt.plot(years, o_fishes, color=('dimgrey'), linewidth=6.0, label='oxbow')
plt.plot(years, d_fishes, color=('olive'), linewidth=6.0, label='dingman')
plt.ylabel("years")
plt.xlabel("number of fish caught")
plt.xticks(years)
plt.title('How many fishes caught in the last three years in the rivers?')

k_fishes = mpatches.Patch(color='firebrick', label='Komoka')
o_fishes = mpatches.Patch(color='dimgrey', label='Oxbow')
d_fishes = mpatches.Patch(color='olive', label='Dingman')
plt.legend(handles=[k_fishes, o_fishes, d_fishes])

plt.show()