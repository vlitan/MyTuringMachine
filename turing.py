#!/usr/bin/env python2.7
import json
import pprint
import optparse
from tape import Tape
from time import sleep
def parse_args():
    usage = """ Usage: turing.py cardsFilePath [options]
    options:
    -m : maximum number of iterations
    -d : default value of the tape
    -s : initial size of the tape"""

    parser = optparse.OptionParser(usage)
    parser.add_option("-m", "--max_iterations", dest="maxIterations", type = "int", default = 10)
    parser.add_option("-d", "--default_value", dest="defaultValue", type = "string", default = "1")
    parser.add_option("-s", "--tape_size", dest="tapeSize", type = "int", default = 10)
    (options, args) = parser.parse_args()
    if len (args) == 0:
        parser.error("The cards file is manadatory")
    return (options, args)



def main():
    (options, args) = parse_args()
    cardsFilePath = args[0]
    tape = Tape(options.defaultValue, options.tapeSize)
    maxIterations = options.maxIterations
    with open(cardsFilePath, "r") as handle:
        cards = json.load(handle)

    currentState = "start"
    iterationCount = 0
    while (currentState != "halt") and (iterationCount < maxIterations):
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
