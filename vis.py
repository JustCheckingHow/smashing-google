from OutputParser import OutputParser
from InputParser import InputParser
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns
from shared import *
import pandas.tools.plotting

# FILE = 'a_example'
# FILE = 'b_should_be_easy'
# FILE = 'c_no_hurry'
FILE = 'd_metropolis'
# FILE = "e_high_bonus"

inputData = InputParser(FILE + ".in")
rows, columns, vehicles, numebrOfRides, bonusOnTime, steps = inputData.readLine()
inputData.close()

possibleRides = pd.read_table(FILE + ".in", sep=' ')
possibleRides.columns = ['xstart', 'ystart', 'xend', 'yend', 'start', 'stop']

color = []
for i in possibleRides.values:
    if (abs(i[2] - i[0]) + abs(i[3] - i[1]) + i[1]+i[0]) >= abs(i[5] - i[4]) and abs(i[2] - i[0]) + abs(i[3] - i[1]) > i[4]:
        color.append('r')
    else:
        color.append('b')

# MAIN LOOP
# sns.jointplot(possibleRides['xend'], possibleRides['yend'], kind='hex', xlim=[-0.1*rows, rows*1.1], ylim=[-0.1*rows, columns*1.1])
# plt.suptitle(FILE+' destinations')

# sns.jointplot(possibleRides['xstart'], possibleRides['ystart'], kind='hex', xlim=[-0.1*rows, rows*1.1], ylim=[-0.1*rows, columns*1.1])
# plt.suptitle(FILE+' origins')

plt.figure()
plt.subplot(211)
plt.scatter(possibleRides['xstart'], possibleRides['ystart'], alpha=0.2, c=color)
plt.title('Origins')
plt.xlim([-0.1*rows, rows*1.1])
plt.ylim([-0.1*rows, columns*1.1])
plt.subplot(212)
plt.scatter(possibleRides['xend'], possibleRides['yend'], alpha=0.2, c=color)
plt.title('Destinations')
plt.xlim([-0.1*rows, rows*1.1])
plt.ylim([-0.1*rows, columns*1.1])
plt.tight_layout()

# plt.figure()
# plt.plot([possibleRides['xstart'], possibleRides['xend']], [possibleRides['ystart'], possibleRides['yend']], alpha=0.1)
# plt.scatter(possibleRides['xstart'], possibleRides['ystart'], marker='o', s=.5)
# plt.title(FILE+' routes')

# plt.figure()
# plt.subplot(211)
# sns.kdeplot(abs(possibleRides['xend']-possibleRides['xstart']) + abs(possibleRides['yend'] - possibleRides['ystart']))
# plt.title('Route distance distribution')
# plt.subplot(212)
# sns.kdeplot(possibleRides['stop']-possibleRides['start'])
# plt.title('Route maxtime distribution')
# plt.tight_layout()

plt.show()