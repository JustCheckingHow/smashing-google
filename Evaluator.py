import numpy as np

class Evaluator(object):
    def __init__(self, evaluationFunction):
        self.evalFunc = evaluationFunction
        self.objectsWithMarks = []

    def clear(self):
        self.objectsWithMarks = []

    def push(self, objectToEval, sort = False):
        mark = self.evalFunc(objectToEval)
        self.objectsWithMarks.append((mark, object))
        if sort:
            self.sort()

    def sort(self):
        self.objectsWithMarks.sort(key = lambda x: x[0])

    def pop(self):
        """ Return tuple (mark, object)"""
        return self.objectsWithMarks[0]

    def popLast(self):
        """ Return tuple (mark, object)"""
        return self.objectsWithMarks[-1]

    def get(self, index):
        """ Return tuple (mark, object)"""
        return self.objectsWithMarks[index]


