import sys

class Auto:

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def setState(self, newState):
        self.state = newState

    def getState(self):
        return self.state

    def changeState(self, autos, stepCounter, stepInfo):
        """ 
        autos: list of neighbourhood: 
        | 0 | 1 | 2 |
        | 3 | X | 4 |
        | 5 | 6 | 7 |
        """

        pass

class CellularAutomaton(object):

    def __init__(self, autosMatrix):
        self.stepCounter = 0
        self.autosMatrix = autosMatrix
        self._autos = [[None for x in range(len(autosMatrix[0]) + 2)]]
        for i in autosMatrix:
            self._autos.append([None] + i + [None])
        self._autos.append([None for x in range(len(autosMatrix[0]) + 2)])

    def doStep(self, stepInfo = None):
        for i in range(1, len(self._autos) - 1):
            for j in range(1, len(self._autos[i]) - 1):
                self._autos[i][j].changeState([self._autos[i-1][j-1], self._autos[i-1][j], self._autos[i-1][j+1],
                    self._autos[i][j-1], self._autos[i][j+1],
                    self._autos[i+1][j-1], self._autos[i+1][j], self._autos[i+1][j+1]], 
                    self.stepCounter, stepInfo)

        self.stepCounter += 1
