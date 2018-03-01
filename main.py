from OutputParser import OutputParser
from InputParser import InputParser
import math

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

inputData = InputParser(PATH + FILE + ".in")
rows, columns, vehicles, numebrOfRides, bonusOnTime, steps = inputData.readLine()
rides = []
impossibleRides = []
for i in range(steps):
    ride = inputData.readLine()
    if (abs(ride[2] - ride[0]) + abs(ride[3] - ride[1])) >= abs(ride[5] - ride[4]): 
        rides.append(ride)
    else:
        impossibleRides.append(ride)

inputData.close()

outputData = OutputParser(PATH + FILE + ".out")
outputData.close()

