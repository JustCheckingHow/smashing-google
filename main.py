from OutputParser import OutputParser
from InputParser import InputParser

PATH = "E:\\GoogleHashCode2018\\"
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
for i in range(steps):
    rides.append(inputData.readLine())

inputData.close()

outputData = OutputParser(PATH + FILE + ".out")
outputData.close()

