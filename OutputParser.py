class OutputParser(object):

    def __init__(self, filename):
        self.outputFile = open(filename, 'w')

    def write(self, listOfData):

        s = ""
        for x in listOfData:
            s += str(x) + ' '

        s = s[:-1] # Remove last 
        s += '\n'
        self.outputFile.write(s)

    def close(self):
        self.outputFile.close()


