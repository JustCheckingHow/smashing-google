class InputParser(object):
    
    def __init__(self, filename):
        self.inputFile = open(filename, 'r')

    def readLine(self):
        line = self.inputFile.readline()

        # Remove next line char
        if line[-1] == '\n':
            line = line[:-1]

        values = line.split(' ')
        for i in range(len(values)):
            if values[i].isdigit():
                values[i] = int(values[i])

        return values

    def close(self):
        self.inputFile.close()