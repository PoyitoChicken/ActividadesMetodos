import re
from parsers import parseDireccion, parseCantidad, parseInput, parseTiempo, parseVueltas
from semaforoHandler import semaforoHandler, creaMatrizSemaforos

class Semaforo:
    def __init__(self, izq, der, recto, direccion, flujo, tiempo):
        self.izq = izq
        self.der = der
        self.recto = recto
        self.direccion = direccion
        self.flujo = flujo
        self.tiempo = tiempo
# Genera objeto de semaforos convirtiendo si hay vuelta a la direccion en grados
def generaSemaforos(cantidad):
    semaforos = []
    for i in range(1, cantidad + 1):
        print(f"*****       Semaforo {i}       *****")
        izq = parseVueltas("¿Tiene vuelta a la izquierda? ")
        der = parseVueltas("¿Tiene vuelta a la derecha? ")
        recto = parseVueltas("¿Va recto? ")
        direccion = input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): ").lower()
        direccion = parseDireccion(direccion)
        # si es true se le resta 90 si es a la izq o se le suma 90 si es a la derecha y se queda igual si es recto
        if izq == True:
            if direccion-90 < 0:
                izq = 315
            else:
                izq = direccion-90
        if der == True:
            if direccion+90 >= 360:
                der = (direccion+90)-360
            else:
                der = direccion+90
        if recto == True:
            recto = direccion
        while direccion in [i.direccion for i in semaforos]:
            print("La dirección ya está ocupada, por favor ingrese otra dirección.")
            direccion = input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): ").lower()
        flujo = int(input("De cuantos carros es el flujo vehicular? "))
        
        semaforos.append(Semaforo(izq, der, recto, direccion, flujo, 0))
    return semaforos
# semaforo de (\d{1,3}s) va a ((?:izquierda|derecha|recto)(?: |$))+apunta (hacia el|al)? (norte|noreste|este|sureste|sur|suroeste|oeste|noroeste)
def main():
    # texto = str(input("Ingrese el sistema de semaforos que desea, para funcionar correctamente debe contener tiempo y la información semaforos: "))
    texto = "2 semaforos 1s"
    texto = parseInput(texto)
    if texto == False:
        main()
    cantidad = texto[0]
    tiempo = texto[1]
    semaforos = generaSemaforos(cantidad)
    matrizSemaforos = creaMatrizSemaforos(semaforos)
    semaforoHandler(matrizSemaforos)
main()