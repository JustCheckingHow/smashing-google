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

PATH = ""
FILE = "d_metropolis"


# ROWS: index, xstart, ystart, xend, yend, start, stop

class Auto:
    def __init__(self, id):
        self.id = id
        self.ticksToFree = 0
        self.x = 0
        self.y = 0
        self.served = []

    def goRide(self, ride, current_tick):
        self.ticksToFree = abs(self.x - ride[1]) + abs(self.y - ride[2])
        if 0 < ride[-2] - abs(self.y - ride[3]) - abs(self.x - ride[2]) - current_tick:
            self.ticksToFree += ride[-2] - abs(self.x - ride[2]) + abs(self.y - ride[3]) - current_tick
        self.ticksToFree += abs(ride[3] - ride[1]) + abs(ride[4] - ride[2])

        self.served.append(ride[0])
        self.x = ride[3]
        self.y = ride[4]

    def tick(self):
        # Decrease ticks of the car
        if self.ticksToFree > 0:
            self.ticksToFree -= 1


def get_free_cars():
    result = []
    for car in cars:
        if car.ticksToFree == 0:
            result.append(car)
    return result

def mult():
    x = []
    for i in possibleRides['0']:
        if i==1:
            x.append('r')
        else:
            x.append('b')
    return x

possibleRides = []
impossibleRides = []

inputData = InputParser(FILE + ".in")
rows, columns, vehicles, numebrOfRides, bonusOnTime, steps = inputData.readLine()
inputData.close()

rides = pd.read_table(FILE + ".in", sep=' ')
color = []

for i in rides.values:
    if (abs(i[2] - i[0]) + abs(i[3] - i[1]) + i[1]+i[0]) >= abs(i[5] - i[4]):
        possibleRides.append(np.insert(i, 0, 1))
        color.append('r')
    else:
        color.append('b')
        possibleRides.append(np.insert(i, 0, 0))

# Sorting
possibleRides = pd.DataFrame(possibleRides, columns=[str(x) for x in range(7)])
impossibleRides = pd.DataFrame(impossibleRides, columns=[str(x) for x in range(7)])


# MAIN LOOP
# plt.figure()
sns.jointplot(possibleRides['3'], possibleRides['4'], kind='hex', xlim=[-0.1*rows, rows*1.1], ylim=[-0.1*rows, columns*1.1])
plt.suptitle(FILE+' destinations')

# plt.figure()
sns.jointplot(possibleRides['1'], possibleRides['2'], kind='hex', xlim=[-0.1*rows, rows*1.1], ylim=[-0.1*rows, columns*1.1])
plt.suptitle(FILE+' origins')

plt.figure()
plt.subplot(211)
plt.scatter(possibleRides['1'], possibleRides['2'], alpha=0.2, c=color)
plt.title('Origins')
plt.xlim([-0.1*rows, rows*1.1])
plt.ylim([-0.1*rows, columns*1.1])

plt.subplot(212)
plt.scatter(possibleRides['3'], possibleRides['4'], alpha=0.2, c=color)
plt.title('Destinations')
plt.xlim([-0.1*rows, rows*1.1])
plt.ylim([-0.1*rows, columns*1.1])
plt.tight_layout()

plt.figure()
plt.plot([possibleRides['1'], possibleRides['3']], [possibleRides['2'], possibleRides['4']], alpha=0.2)
plt.scatter(possibleRides['1'], possibleRides['2'], marker='o', s=.5)
plt.title(FILE+' routes')
plt.show()


# plt.figure()
# sns.kdeplot(possibleRides['6'])