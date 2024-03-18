import re

# Convierte la direccion de nombre a grados
def parseDireccion(direccion):
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

# Creado para analizar si hay vueltas a la izquierda, derecha o recto
# Utilizado para parsear inputs de si o no a bools
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

# Parsea el tiempo de los semaforos antes entraban tambien minutos pero se cambio a solo segundos pero no se cambio el regex por tiempo
def parseTiempo(texto):
    match = re.search(r' \d{1,3}s', texto)
    getSeconds = re.search(r'(\d+s|:\d{1,2})', texto)
    getSeconds = re.search(r'\d+', getSeconds.group(0))
    return [int(getSeconds.group(0))]

# Parsea la cantidad cantidad de semaforos
# Busca si hay un "cantidad" (opcional) y un numero de varios digitos 
# Seguido de un "semaforo(s)? para ver cuantos semaforos hay"
def parseCantidad(texto):
    matchCantidad = re.search(r'(cantidad .*?)?(\d+)\s+semaforo(s)?', texto)
    if matchCantidad:
        number = re.search(r'\d+', matchCantidad.group(0))
        if number:
            matchCantidad = int(number.group(0))
    else:
        raise Exception("No se encontro la cantidad de semaforos")
    return matchCantidad


def parseInput(texto):
    try:
        matchTiempo = parseTiempo(texto)
        matchCantidad = parseCantidad(texto)
    except Exception as e:
        print(f"El texto ingresado no es valido {e}")
        return False
    return [matchCantidad, matchTiempo]

