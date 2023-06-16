archive = open("data.txt", "r")
pieza = archive.readlines()
print(type(pieza))
actual = ""
imagenes = []
for i in range(len(pieza)):
    actual = actual + pieza[i]
    for j in range(len(pieza[i])):
        if i>0:
            if pieza[i - 1][j] == "|" and pieza[i][j] == "+":
                imagenes.append(actual)
                actual = ""

for img in imagenes:
    print(img)
    print("inicia otra")
archive.close()
