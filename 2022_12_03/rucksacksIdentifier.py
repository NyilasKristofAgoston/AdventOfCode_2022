import os

f = open((os.path.dirname(__file__)+"\input"), "r")

# Settel van megoldva, majd talán később megcsinálom gyakorlásképp
''' def vanEBenne(inpLista1, inpLista2):
    inpSet1 = set(inpLista1)
    inpSet2 = set(inpLista2)

    print(inpSet1 & inpSet2) '''

def kozosEgyezes(inpLista1, inpLista2, inpLista3):
    resultLista = list(set([i for i in inpLista1 if i in inpLista2 if i in inpLista3]))
    return resultLista

def priorityValue(inpLista):
    
    returnOsszeg = 0

    # print(resultLista)

    for i in inpLista:
        if i.isupper():
            returnOsszeg += ord(i)-38
            print(i, ord(i)-38)
        else:
            returnOsszeg += ord(i)-96
            print(i, ord(i)-96)   


    return returnOsszeg

# megszámolja az input sorjait, hogy majd 3-mal oszthassa
num_lines = sum(1 for line in f)
#print(num_lines)

#újra meg kell nyitni
f = open((os.path.dirname(__file__)+"\input"), "r")

outValue = 0
szamlaloSor = 0


part = 1

for i in f:
    
    if part == 1:
        firstPart = i
    elif part == 2:
        secondPart = i
    elif part == 3:
        thirdPart = i
    
    elif part > 3:
        print(kozosEgyezes(firstPart[:-2], secondPart[:-2], thirdPart[:-2]))
        outValue += priorityValue(kozosEgyezes(firstPart[:-2], secondPart[:-2], thirdPart[:-2]))
        firstPart = i
        part = 1

    
    
    part += 1

    

print(outValue)