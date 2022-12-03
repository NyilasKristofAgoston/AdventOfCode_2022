import os

f = open((os.path.dirname(__file__)+"\input.txt"), "r")

index = 0

osszegLista = []
szamlalo = 0

for i in f:

    if i == "\n":
        osszegLista.append(szamlalo)
        index += 1
        szamlalo = 0
    else:
        szamlalo += int(i)

print(max(osszegLista))