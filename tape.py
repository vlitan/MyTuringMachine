
class Tape(object):
    """docstring for Tape."""

    rightExpandSize = 1
    leftExpandSize = 1

    def __init__(self, defaultValue = None, size = 10):
        super(Tape, self).__init__()
        self.defaultValue = defaultValue
        self.data = [defaultValue] * size
        self.position = size / 2

    def loadTape(self, tapeToLoad):
        self.data = tapeToLoad

    # TODO: create more flexible input methods
    def directionDecoder(self, direction):
        return {"r": 1, "l": -1, "n": 0}.get(direction, 0)

    def adjustSize(self):
        if (self.position < 0):
            self.position += self.leftExpandSize
            self.data = [self.defaultValue] * self.leftExpandSize + self.data
            self.leftExpandSize *= 2

        if (self.position >= len(self.data)):
            self.data = self.data + [self.defaultValue] * self.rightExpandSize
            self.rightExpandSize *= 2

    def move(self, direction):
        self.position += self.directionDecoder(direction)
        self.adjustSize()

    def write(self, val):
        self.data[self.position] = val

    def read(self):
        return self.data[self.position]
    # TODO: this is not good practice. too much coupling and bad naming etc.
    # NOTE: it surrounds the current element with [] if its on the head position, else just converts it to string
    def braketizerStr(self, index):
        if (index == self.position):
            return "[" + str(self.data[index]) + "]"
        return str(self.data[index])

    # NOTE: debug string
    def statusToString(self):
        tapeString = ', '.join([self.braketizerStr(i) for i in range(len(self.data))])
        return "size {}\nlist: {}\nhead position:{}\n\n".format(len(self.data),tapeString, self.position)
