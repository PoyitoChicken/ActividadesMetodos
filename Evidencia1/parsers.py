import re

def parseDireccion(direccion):
    # Parsear la orientacion en grados
    direccion = direccion.lower()
    if direccion == "norte":
        direccion = 0
    elif direccion == "noreste":
        direccion = 45
    elif direccion == "este":
        direccion = 90
    elif direccion == "sureste":
        direccion = 135
    elif direccion == "sur":
        direccion = 180
    elif direccion == "suroeste":
        direccion = 225
    elif direccion == "oeste":
        direccion = 270
    elif direccion == "noroeste":
        direccion = 315
    else:
        print("La direccion ingresada no es valida, intenta de nuevo")
        direccion = str(input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): "))
        parseDireccion(direccion)
    return direccion

def parseVueltas(pregunta):
    texto = str(input(pregunta))
    si = re.search(r'(^s[ií]?|^y(es)?.?)', texto.lower())
    no = re.search(r'^n[oó]?.?', texto.lower())
    try: 
        if si:
            return True
        elif no:
            return False
    except:
        print("El texto ingresado no es valido, intenta de nuevo")
        parseVueltas(pregunta)

def parseTiempo(texto):
    match = re.search(r'(\d{1,2}:\d{1,2}|(\d+m)? ?(\d+s)?)', texto)
    getMinutes = re.search(r'(\d+m|\d{1,2}:)', texto)
    getSeconds = re.search(r'(\d+s|:\d{1,2})', texto)
    getMinutes = re.search(r'\d+', getMinutes.group(0))
    getSeconds = re.search(r'\d+', getSeconds.group(0))
    print(f"Minutos: {getMinutes.group(0)} con {getSeconds.group(0)} segundos")
    return [int(getMinutes.group(0)), int(getSeconds.group(0))]

def parseCantidad(texto):
    matchCantidad = re.search(r'(cantidad .*)? ?\d+ semaforos?', texto)
    if matchCantidad:
        number = re.search(r'\d+', matchCantidad.group(0))
        if number:
            matchCantidad = int(number.group(0))
    print(matchCantidad)
    return matchCantidad


def parseInput(texto):
    try:
        matchTiempo = parseTiempo(texto)
        matchCantidad = parseCantidad(texto)
    except:
        print("El texto ingresado no es valido")
        return False
    return [matchCantidad, matchTiempo]
