import os

f = open((os.path.dirname(__file__)+"\input"), "r")

# Settel van megoldva, majd talán később megcsinálom gyakorlásképp
''' def vanEBenne(inpLista1, inpLista2):
    inpSet1 = set(inpLista1)
    inpSet2 = set(inpLista2)

    print(inpSet1 & inpSet2) '''

def kozosEgyezes(inpLista1, inpLista2):
    resultLista = list(set([i for i in inpLista1 if i in inpLista2]))
    return resultLista

def priorityValue(inpLista):
    
    returnOsszeg = 0

    # print(resultLista)

    for i in inpLista:
        if i.isupper():
            returnOsszeg += ord(i)-38
            # print(i, ord(i)-38)
        else:
            returnOsszeg += ord(i)-96
            # print(i, ord(i)-96)   


    return returnOsszeg

outValue = 0

for i in f:
    i = list(i)
    firstPart = i[:(len(i)) // 2]
    secondPart = i[(len(i)) // 2:]
    #vanEBenne(firstPart, secondPart)
    outValue += priorityValue(kozosEgyezes(firstPart, secondPart))
print(outValue)