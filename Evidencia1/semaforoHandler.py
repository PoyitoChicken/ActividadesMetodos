import time 
from parsers import parseVueltas
import math as m
import sys

## Crea una matriz con los semaforos y sus direcciones donde 
def creaMatrizSemaforos(semaforos):
    sistemaSemaforos = []
    index = 0
    direcciones = {
        0: 0,
        45: 1,
        90: 2,
        135: 3,
        180: 4,
        225: 5,
        270: 6,
        315: 7
    }
    semaforos = sorted(semaforos, key=lambda x: x.flujo, reverse=True)
    semaforos = asignarTiempos(semaforos)
    for semaforo in semaforos: 
        sistemaSemaforos.append([0, 0, 0, 0, 0, 0, 0, 0])
        if semaforo.izq is not False:
            sistemaSemaforos[index][direcciones[semaforo.izq]] = "Verde"
        if semaforo.der is not False:
            sistemaSemaforos[index][direcciones[semaforo.der]] = "Verde"
        if semaforo.recto is not False:
            sistemaSemaforos[index][direcciones[semaforo.recto]] = "Verde"
        for i in range(0, len(sistemaSemaforos[index])):
            if sistemaSemaforos[index][i] == 0:
                sistemaSemaforos[index][i] = "Verde Peatonal"
        index += 1
        sistemaSemaforos.append([0, 0, 0, 0, 0, 0, 0, 0])
        if semaforo.izq is not False:
            sistemaSemaforos[index][direcciones[semaforo.izq]] = "Amarillo"
        if semaforo.der is not False:
            sistemaSemaforos[index][direcciones[semaforo.der]] = "Amarillo"
        if semaforo.recto is not False:
            sistemaSemaforos[index][direcciones[semaforo.recto]] = "Amarillo"
        for i in range(0, len(sistemaSemaforos[index])):
            if sistemaSemaforos[index][i] == 0:
                sistemaSemaforos[index][i] = "Verde Peatonal"
        index += 1
        sistemaSemaforos.append(["Verde Peatonal"*8])
        index += 1
    semaforoHandler(sistemaSemaforos, semaforos)
    return sistemaSemaforos

# Maneja el semaforo
def semaforoHandler(sistemaSemaforos, semaforos):
    index = 0
    i = 0
    botonPeatonal = False
    peatonalIndex = len(sistemaSemaforos) - 1
    print(f"{'Norte':<16}{'Noreste':<16}{'Este':<16}{'Sureste':<16}{'Sur':<16}{'Suroeste':<16}{'Oeste':<16}{'Noroeste':<16}")
    while i < 20:
        if botonPeatonal == False:
            print('\t'.join(map(lambda x: str(x).ljust(8), sistemaSemaforos[i])))
            time.sleep(semaforos[index].tiempo) 
        else:
            print('\t'.join(map(lambda x: str(x).ljust(8), sistemaSemaforos[peatonalIndex])))
            time.sleep(2)
            botonPeatonal = False
        # botonPeatonal = parseVueltas("Desea activar el cruce peatonal? ")
        if index+1 >= len(semaforos):
            index = 0
        if (i % 2 == 0 and i > 0):
            index += 1
        if i + 1 >= len(sistemaSemaforos):
            i = 0   
        # sys.stdout.write('\033[F')
        # sys.stdout.write('\033[K')
        i += 1
    return "Semaforo Handler"
# Asigna tiempos random para evitar errores del usuario
def asignarTiempos(semaforos):
    cap = 1
    for i in range(len(semaforos) - 1, -1, -1):
        semaforos[i].tiempo = cap
        cap += 2
    return semaforos

# Listar las direcciones de los semaforos
# Obtener los destinos dependiendo de si es izquierda o derecha o si es vuelta o giro o recto