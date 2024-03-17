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
    semaforo = []
    for i in range(cantidad):
        print(f"*****       Semaforo {i+1}       *****")
        izq = parseVueltas("Tiene vuelta a la izquierda? ")
        der = parseVueltas("Tiene vuelta a la derecha? ")
        recto = parseVueltas("Va recto? ")
        direccion = str(input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): "))
        while (direccion in semaforo.direccion):
            print("La direccion ya esta ocupada, por favor ingrese otra direccion")
            direccion = str(input("Ingrese la direccion del semaforo (norte, noroeste, sur, sureste, etc.): "))
        semaforo.append(Semaforo(tipo, izq, der, recto, direccion))
        return semaforo

def main():
    texto = str(input("Ingrese el sistema de semaforos que desea, para funcionar correctamente debe contener tiempo, cantidad de semaforos: "))
    texto = parseInput(texto)
    if texto == False:
        main()
    cantidad = texto[0]
    tiempo = texto[1]
    semaforos = generaSemaforos(cantidad)
main()