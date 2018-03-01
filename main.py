from OutputParser import OutputParser
from InputParser import InputParser
import math
import pandas as pd

PATH = ""
FILE = "a_example"

class Auto:
    def __init__(self):
        self.ticksToFree = 0
        self.x = 0
        self.y = 0

    def goRide(self, ride):
        self.x = ride[2]
        self.y = ride[3]

    def tick(self):
        if self.ticksToFree > 0:
            self.ticksToFree -= 1

possibleRides = []
impossibleRides = []

inputData = InputParser(FILE + ".in")
rows, columns, vehicles, numebrOfRides, bonusOnTime, steps = inputData.readLine()
inputData.close()

rides = pd.read_table(FILE + ".in", sep=' ')

for i in rides.values:
    if (abs(i[2] - i[0]) + abs(i[3] - i[1])) >= abs(i[5] - i[4]):
        impossibleRides.append(i)
    else:
        possibleRides.append(i)

# Sorting
possibleRides = pd.DataFrame(possibleRides)
impossibleRides = pd.DataFrame(impossibleRides)
possibleRides = possibleRides.sort_values(by=4)
if len(impossibleRides)>0:
    impossibleRides = impossibleRides.sort_values(by=4)

cars = []
for i in range(vehicles):
    cars.append(Auto())

# MAIN LOOP
for i in range(steps):
    for car in cars:
        car.tick()

outputData = OutputParser(PATH + FILE + ".out")
outputData.close()
