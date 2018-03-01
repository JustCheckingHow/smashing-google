from OutputParser import OutputParser
from InputParser import InputParser
import numpy as np
import math
import pandas as pd

PATH = ""
FILE = "a_example"


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
        if self.ticksToFree > 0:
            self.ticksToFree -= 1


def get_free_cars():
    result = []
    for car in cars:
        if car.ticksToFree == 0:
            result.append(car)
    return result


possibleRides = []
impossibleRides = []

inputData = InputParser(FILE + ".in")
rows, columns, vehicles, numebrOfRides, bonusOnTime, steps = inputData.readLine()
inputData.close()

rides = pd.read_table(FILE + ".in", sep=' ')

counter = 0
for i in rides.values:
    if (abs(i[2] - i[0]) + abs(i[3] - i[1])) >= abs(i[5] - i[4]):
        impossibleRides.append(np.insert(i, 0, counter))
    else:
        possibleRides.append(np.insert(i, 0, counter))
    counter += 1

# Sorting
possibleRides = pd.DataFrame(possibleRides)
impossibleRides = pd.DataFrame(impossibleRides)
possibleRides = possibleRides.sort_values(by=4)
if len(impossibleRides) > 0:
    impossibleRides = impossibleRides.sort_values(by=4)

cars = []
for i in range(vehicles):
    cars.append(Auto(i + 1))
cars = np.array(cars)

# MAIN LOOP
for i in range(steps):
    freeCars = get_free_cars()
    for car in cars:
        car.tick()

# Save output
outputData = OutputParser(PATH + FILE + ".out")
for i in cars:
    outputData.write([i.id] + i.served)

outputData.close()
