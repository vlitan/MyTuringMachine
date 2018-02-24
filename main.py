import json
import pprint
from tape import Tape

def main():
    cardsFilePath = "cards.json"
    maxIterations = 10
    with open(cardsFilePath, "r") as handle:
        cards = json.load(handle)
    currentState = "start"
    tape = Tape(defaultValue = "1")
    iterationCount = 0
    while currentState != "halt" and iterationCount < maxIterations:
        instructions = cards[currentState][tape.read()]
        tape.write(instructions["write"])
        tape.move(instructions["move"])
        currentState = instructions["next"]
        print currentState
        print tape.statusToString()
        iterationCount += 1
    if currentState != "halt":
        print "maximum iterations exceeded!"


if __name__ == "__main__" :
    main()
