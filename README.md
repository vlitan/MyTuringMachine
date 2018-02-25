# MyTuringMachine
## What is this?
A straight forward implementation of a turing machine. I considered the Tibo Rado model, with cards that containt the "code".
Most of what I know about this subject I learned from this [computerphile video](https://www.youtube.com/watch?v=DILF8usqp7M).
## How to use this?
The cards are represented in json format, making it easier to read as a human and to use as a program. Edit the "cards.json" file and run main.py. The output contains the "tape" and state at each iteration. As a true turing machine, the tape has to be infinite, left and right. In order to achieve this each time the cursor gets to the boundaries of the tape, more memory is allocated (the amount of allocated memory increases exponentially with each allocation). Also, at the moment there are no restrictions on values to be written. 
## Future improvements
- Command line arguments and options
- Meaningful errors
- Refactor
- Maybe add some kind of cards generator from user input
- More friendly cards input
