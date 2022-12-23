import os

f = open((os.path.dirname(__file__)+"\input"), "r")

loses_to = {
    "A": "B",
    "B": "C",
    "C": "A",
}

pointsForShape = {
    "A": 1,
    "B": 2,
    "C": 3,
}

def play(localHis, localMine):

    # 6 - win, 3 - draw, 0 - lose
    if loses_to[localHis] == localMine:
        return 6 + pointsForShape[localMine]
    elif loses_to[localMine] == localHis:
        return 0 + pointsForShape[localMine]
    else:
        return 3 + pointsForShape[localMine]

counter = 0

for i in f:
    rawList = i.split()

    #changes the ASCII value, (-23) so the chars can be compared 
    his = chr(ord("".join(rawList[0])))
    mine = chr(ord("".join(rawList[1]))-23)

    counter += play(his, mine)


print(counter)

