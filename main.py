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

inputData = InputParser(FILE + ".in")
rows, columns, vehicles, numebrOfRides, bonusOnTime, steps = inputData.readLine()
inputData.close()

rides = pd.read_table(FILE + ".in", sep=' ')

outputData = OutputParser(PATH + FILE + ".out")
outputData.close()