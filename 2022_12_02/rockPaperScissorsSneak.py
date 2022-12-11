import os

f = open((os.path.dirname(__file__)+"\input"), "r")

counter = 0

his = ""
instructionChar = ""
for i in f:
    rawList = i.split()

    his = chr(ord("".join(rawList[0])))
    instructionChar = "".join(rawList[1])


    loses_to = {
        "A": "B",
        "B": "C",
        "C": "A",
    }

    wins_to = {
        "A": "C",
        "B": "A",
        "C": "B",
    }

    draws_to = {
        "A": "A",
        "B": "B",
        "C": "C",
    }

    pointsForShape = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    instruction = {
        # X - lose, Y - draw, Z - win
        "X":0 + pointsForShape[loses_to[his]],
        "Y":3 + pointsForShape[draws_to[his]],
        "Z":6 + pointsForShape[wins_to[his]],

    }

    counter += (instruction[instructionChar])

print(counter)