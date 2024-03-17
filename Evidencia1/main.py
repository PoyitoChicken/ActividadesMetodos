import re
from parsers import parseDireccion, parseCantidad, parseInput, parseTiempo, parseVueltas
class Semaforo:
    def __init__(self, izq, der, recto, direccion):
        self.izq = izq
        self.der = der
        self.recto = recto
        self.direccion = direccion

def sistemaSemaforos(semaforo):
    print(f"*****       Semaforo {semaforo.direccion}       *****")
    print(f"Vuelta a la izquierda: {semaforo.izq}")
    print(f"Vuelta a la derecha: {semaforo.der}")
    print(f"Va recto: {semaforo.recto}")
    print(f"Direccion: {semaforo.direccion}")


def generaSemaforos(cantidad):
    semaforos = []
    for i in range(1, cantidad + 1):
        print(f"*****       Semaforo {i}       *****")
        izq = parseVueltas("¿Tiene vuelta a la izquierda? ")
        der = parseVueltas("¿Tiene vuelta a la derecha? ")
        recto = parseVueltas("¿Va recto? ")
        direccion = input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): ").lower()
        while direccion in [i.direccion for i in semaforos]:
            print("La dirección ya está ocupada, por favor ingrese otra dirección.")
            direccion = input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): ").lower()
        semaforos.append(Semaforo(izq, der, recto, direccion))
    return semaforos

def main():
    texto = str(input("Ingrese el sistema de semaforos que desea, para funcionar correctamente debe contener tiempo y la información semaforos: "))
    texto = parseInput(texto)
    if texto == False:
        main()
    cantidad = texto[0]
    tiempo = texto[1]
    semaforos = generaSemaforos(cantidad)
main()