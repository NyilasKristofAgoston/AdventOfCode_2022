import os

f = open((os.path.dirname(__file__)+"\input"), "r")

def priorityValue(inpChar):

    if inpChar.isupper():
        return ord(inpChar)-38
    else:
        return ord(inpChar)-96

part = 1
outValue = 0


for i in f:
    if part == 1:
        a = i.strip()
        part += 1

    elif part == 2:
        b = i
        part += 1

    elif part == 3:
        c = i
        
        outValue += priorityValue(((set(a) & set(b) & set(c)).pop()))
        
        
        
        
        part = 1
print(outValue)