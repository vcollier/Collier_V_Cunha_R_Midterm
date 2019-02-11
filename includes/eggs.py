import numpy as np
import matplotlib.pyplot as plt
import csv

with open('data/traa_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

N = 5
rainbowMeans = (100, 150, 100, 50, 150)
brownMeans = (100, 80, 70, 80, 100)
rainbowStd = (2, 3, 4, 1, 2)
brownStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, rainbowMeans, width, color='skyBlue', yerr=rainbowStd)
p2 = plt.bar(ind, brownMeans, width, color='Green',
             bottom=rainbowMeans, yerr=brownStd)

plt.ylabel('Scores')
plt.title('Scores by number of eggs received by species')
plt.xticks(ind, ('2014', '2015', '2016', '2017', '2018'))
plt.yticks(np.arange(0, 260, 10))
plt.legend((p1[0], p2[0]), ('Rainbow Trout', 'Brown Trout'))

plt.show()