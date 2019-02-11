import numpy as np
import matplotlib.pyplot as plt
import csv

with open('data/traa_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
years = ('2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018')
y_pos = np.arange(len(years))
membership = ('52', '48', '67', '45', '45', '50', '55', '67', '65', '70', '60', '60', '55', '60', '65', '75', '80')
x_pos = np.arange(len(membership))
error = np.random.rand(len(years))

ax.barh(y_pos, membership, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(years)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Membership Numbers')
ax.set_title('How many members we got by year?')

plt.show()