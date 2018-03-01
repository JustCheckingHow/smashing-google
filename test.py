from OutputParser import OutputParser
from InputParser import InputParser
from CellularAutomaton import *

PATH = "E:\\GoogleHashCode2018\\"
FILE = "big"

global pizza
global lastGroupNumber
global groups

pizza = None
groups = {}
lastGroupNumber = 0

class Group:
    HORIZONTAL = 0 # set
    VERTICAL = 1 # set
    def __init__(self, autosInGroup, state, set):
        self.autos = autosInGroup
        self.state = state
        self.number = len(self.autos)
        self.set = set

class PizzaAuto(Auto):
    T = -2
    M = -1
    ING = {'T': T, 'M': M}

    def __init__(self, x, y, state):
        return super().__init__(x, y, state)

    def firstStep(self, autos, stepCounter, stepInfo):
        global pizza
        global lastGroupNumber
        global groups

        p = stepInfo[0]
        q = stepInfo[1]
        mNumber = 0
        tNumber = 0
        if self.state == PizzaAuto.M: 
            mNumber += 1
        elif self.state == PizzaAuto.T: 
            tNumber += 1
        else:
            return

        # Left
        x = self.x - 1
        y = self.y
        i = 0
        autos = [self]
        while (x >= 0) and (pizza.autosMatrix[y][x] != None):
            if (pizza.autosMatrix[y][x].state == PizzaAuto.M):
                mNumber += 1
            elif (pizza.autosMatrix[y][x].state == PizzaAuto.T):
                tNumber += 1
            else:
                break
            autos.append(pizza.autosMatrix[y][x])

            if (mNumber + tNumber) > q:
                break
            if (mNumber >= p) and (tNumber >= p):
                lastGroupNumber += 1
                g = Group(autos, lastGroupNumber, Group.HORIZONTAL)
                for a in autos: 
                    groups[a] = g
                    a.state = lastGroupNumber
                return

            x -= 1

        # Right
        mNumber = 0
        tNumber = 0
        if self.state == PizzaAuto.M: 
            mNumber += 1
        else:
            tNumber += 1
        x = self.x + 1
        y = self.y
        i = 0
        maxX = len(pizza.autosMatrix[y])
        autos = [self]
        while (x < maxX) and (pizza.autosMatrix[y][x] != None):
            if (pizza.autosMatrix[y][x].state == PizzaAuto.M):
                mNumber += 1
            elif (pizza.autosMatrix[y][x].state == PizzaAuto.T):
                tNumber += 1
            else:
                break
            autos.append(pizza.autosMatrix[y][x])

            if (mNumber + tNumber) > q:
                break
            if (mNumber >= p) and (tNumber >= p):
                lastGroupNumber += 1
                g = Group(autos, lastGroupNumber, Group.HORIZONTAL)
                for a in autos: 
                    groups[a] = g
                    a.state = lastGroupNumber
                return

            x += 1

        # Up
        mNumber = 0
        tNumber = 0
        if self.state == PizzaAuto.M: 
            mNumber += 1
        else:
            tNumber += 1
        x = self.x
        y = self.y - 1
        i = 0
        autos = [self]
        while (y >= 0) and (pizza.autosMatrix[y][x] != None):
            if (pizza.autosMatrix[y][x].state == PizzaAuto.M):
                mNumber += 1
            elif (pizza.autosMatrix[y][x].state == PizzaAuto.T):
                tNumber += 1
            else:
                break
            autos.append(pizza.autosMatrix[y][x])

            if (mNumber + tNumber) > q:
                break
            if (mNumber >= p) and (tNumber >= p):
                lastGroupNumber += 1
                g = Group(autos, lastGroupNumber, Group.VERTICAL)
                for a in autos: 
                    groups[a] = g
                    a.state = lastGroupNumber
                return

            y -= 1

        # Down
        mNumber = 0
        tNumber = 0
        if self.state == PizzaAuto.M: 
            mNumber += 1
        else:
            tNumber += 1
        x = self.x
        y = self.y + 1
        i = 0
        autos = [self]
        maxY = len(pizza.autosMatrix)
        while (y < maxY) and (pizza.autosMatrix[y][x] != None):
            if (pizza.autosMatrix[y][x].state == PizzaAuto.M):
                mNumber += 1
            elif (pizza.autosMatrix[y][x].state == PizzaAuto.T):
                tNumber += 1
            else:
                break
            autos.append(pizza.autosMatrix[y][x])

            if (mNumber + tNumber) > q:
                break
            if (mNumber >= p) and (tNumber >= p):
                lastGroupNumber += 1
                g = Group(autos, lastGroupNumber, Group.VERTICAL)
                for a in autos: 
                    groups[a] = g
                    a.state = lastGroupNumber
                return

            y += 1

    def secondStep(self, autos, stepCounter, stepInfo):
        global groups

        p = stepInfo[0]
        q = stepInfo[1]
        if self.state == PizzaAuto.M or self.state == PizzaAuto.T:
            g = None
            try:
                g = groups[autos[3]]
            except:
                pass
            else:
                if groups[autos[3]].set == Group.HORIZONTAL and groups[autos[3]].number < q:
                    groups[autos[3]].number += 1
                    self.state = groups[autos[3]].state
                    groups[autos[3]].autos.append(self)
                    return
            try:
                g = groups[autos[4]]
            except:
                pass
            else:
                if groups[autos[4]].set == Group.HORIZONTAL and groups[autos[4]].number < q:
                    groups[autos[4]].number += 1
                    self.state = groups[autos[4]].state
                    groups[autos[4]].autos.append(self)
                    return
            try:
                g = groups[autos[1]]
            except:
                pass
            else:
                if groups[autos[1]].set == Group.VERTICAL and groups[autos[1]].number < q:
                    groups[autos[1]].number += 1
                    self.state = groups[autos[1]].state
                    groups[autos[1]].autos.append(self)
                    return 
            try:
                g = groups[autos[6]]
            except:
                pass
            else:
                if groups[autos[6]].set == Group.VERTICAL and groups[autos[6]].number < q:
                    groups[autos[6]].number += 1
                    self.state = groups[autos[6]].state
                    groups[autos[6]].autos.append(self)
                    return

    def changeState(self, autos, stepCounter, stepInfo):

        if stepCounter == 0:
            self.firstStep(autos, stepCounter, stepInfo)
        else:
            self.secondStep(autos, stepCounter, stepInfo)

inputData = InputParser(PATH + FILE + ".in")

rows, columns, p, q = inputData.readLine()
autos = []
for i in range(rows):
    autos_row = []
    row = inputData.readLine()[0]
    x = 0
    for ing in row:
        autos_row.append(PizzaAuto(x, i, PizzaAuto.ING[ing]))
        x += 1
    autos.append(autos_row)
inputData.close()

pizza = CellularAutomaton(autos)
pizza.doStep(stepInfo=(p, q))
for i in range(q - 2):
    pizza.doStep(stepInfo=(p, q))

# Third step
for i in range(lastGroupNumber):
    group = None
    for g in groups.values(): 
        if g.state == (i + 1): 
            group = g
    
    connect = False
    autosToAdd = []
    for a in group.autos:
        if group.set == Group.VERTICAL:
            if (a.x - 1) >= 0:
                if pizza.autosMatrix[a.y][a.x - 1].state == PizzaAuto.M or pizza.autosMatrix[a.y][a.x - 1].state == PizzaAuto.T:
                    connect = True
                    autosToAdd.append((a.y, a.x - 1))
                else:
                    connect = False
                    break
    if connect:
        if (group.number + len(autosToAdd)) <= q:
            group.number += len(autosToAdd)
            for auto in autosToAdd:
                pizza.autosMatrix[auto[0]][auto[1]].state = group.state
                group.autos.append(pizza.autosMatrix[auto[0]][auto[1]])

    connect = False
    autosToAdd = []
    for a in group.autos:
        if group.set == Group.VERTICAL:
            if (a.x + 1) < len(pizza.autosMatrix[a.y]):
                if pizza.autosMatrix[a.y][a.x + 1].state == PizzaAuto.M or pizza.autosMatrix[a.y][a.x + 1].state == PizzaAuto.T:
                    connect = True
                    autosToAdd.append((a.y, a.x + 1))
                else:
                    connect = False
                    break
    if connect:
        if (group.number + len(autosToAdd)) <= q:
            group.number += len(autosToAdd)
            for auto in autosToAdd:
                pizza.autosMatrix[auto[0]][auto[1]].state = group.state
                group.autos.append(pizza.autosMatrix[auto[0]][auto[1]])

    connect = False
    autosToAdd = []
    for a in group.autos:
        if group.set == Group.HORIZONTAL:
            if (a.y - 1) >= 0:
                if pizza.autosMatrix[a.y - 1][a.x].state == PizzaAuto.M or pizza.autosMatrix[a.y - 1][a.x].state == PizzaAuto.T:
                    connect = True
                    autosToAdd.append((a.y - 1, a.x))
                else:
                    connect = False
                    break
    if connect:
        if (group.number + len(autosToAdd)) <= q:
            group.number += len(autosToAdd)
            for auto in autosToAdd:
                pizza.autosMatrix[auto[0]][auto[1]].state = group.state
                group.autos.append(pizza.autosMatrix[auto[0]][auto[1]])

    connect = False
    autosToAdd = []
    for a in group.autos:
        if group.set == Group.HORIZONTAL:
            if (a.y + 1) < len(pizza.autosMatrix):
                if pizza.autosMatrix[a.y + 1][a.x].state == PizzaAuto.M or pizza.autosMatrix[a.y + 1][a.x].state == PizzaAuto.T:
                    connect = True
                    autosToAdd.append((a.y + 1, a.x))
                else:
                    connect = False
                    break
    if connect:
        if (group.number + len(autosToAdd)) <= q:
            group.number += len(autosToAdd)
            for auto in autosToAdd:
                pizza.autosMatrix[auto[0]][auto[1]].state = group.state
                group.autos.append(pizza.autosMatrix[auto[0]][auto[1]])

outputData = OutputParser(PATH + FILE + ".out")
outputData.write([lastGroupNumber])
for i in range(lastGroupNumber):
    xs = []
    ys = []
    group = None
    for g in groups.values(): 
        if g.state == (i + 1): 
            group = g
    for a in group.autos:
        xs.append(a.x)
        ys.append(a.y)
    outputData.write([min(ys), min(xs), max(ys), max(xs)])
outputData.close()