def CalcularArea(x1, y1, x2, y2):
    lado1: int = 0
    lado2: int = 0
    if x1 > x2:
        lado1 = x1-x2
    else:
        lado1 = x2-x1
    if y1 > y2:
        lado2 = y1-y2
    else:
        lado2 = y2-y1
    return lado1*lado2

def Separar(linea):
    coordenadas: list = []
    coordenada: dict = {"x": "", "y": ""}
    coordenada2: dict = {"x": "", "y": ""}
    valor = ""
    contador: int = 0
    for i in range(len(linea)):
        actual = linea[i]
        if actual != ",":
            valor = valor + actual
            if len(linea)-1 == i:
                nuevoValor = ""
                for j in range (len(valor)):
                    if j != len(valor)-1:
                        nuevoValor = nuevoValor + valor[j]
                coordenada2["y"] = int(nuevoValor)
                coordenadas.append(coordenada2)
                valor = ""
                contador += 1
        elif actual == ",":
            if contador == 0:
                coordenada["x"] = int(valor)
                contador += 1
                valor = ""
            elif contador == 1:
                coordenada["y"] = int(valor)
                coordenadas.append(coordenada)
                valor = ""
                contador += 1
            elif contador == 2:
                coordenada2["x"] = int(valor)
                contador += 1
                valor = ""
    return coordenadas


def Ordenar(lista):
    for i in range(len(lista)):
        if i < len(lista)-1:
            if lista[i][0]["x"] > lista[i+1][0]["x"]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista

def CalcularIguales(lista):
    nuevasAreas: list = []
    for i in range(len(lista)):
        lado1 = 0
        lado2 = 0
        if i < len(lista) - 1:
            if lista[i][0]["x"] < lista[i+1][1]["x"] and lista[i+1][0]["x"] < lista[i][1]["x"]:
                lado1 = lista[i][1]["x"] - lista[i+1][0]["x"]
                if lista[i + 1][1]["y"] > lista[i][1]["y"] > lista[i + 1][0]["y"]:
                    print(lista[i][1]["y"], lista[i + 1][0]["y"])
                    lado2 = lista[i][1]["y"] - lista[i + 1][0]["y"]
                else:
                    lado2 = lista[i][1]["y"] - lista[i+1][1]["y"]
                print(lado1, lado2)
                area: int = lado1*lado2
                nuevasAreas.append(area)
    return nuevasAreas

archive = open("data.txt", "r")
lineas = archive.readlines()
areas = []
nuevaLista = []
for linea in lineas:
    valores = Separar(linea)
    nuevaLista.append(valores)
nuevaLista = Ordenar(nuevaLista)
print("nv", nuevaLista)
for nv in nuevaLista:
    areas.append(CalcularArea(nv[0]["x"], nv[0]["y"], nv[1]["x"], nv[1]["y"]))
print("nv", nuevaLista)
restar = CalcularIguales(nuevaLista)
respuesta: int = 0
for area in areas:
    respuesta = respuesta+ area
for resta in restar:
    respuesta = respuesta - resta
print("Respuesta: ", respuesta)
archive.close()
