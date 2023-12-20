import random

class Tragamonedas:
    def __init__(self):
        # Constructor de la clase Tragamonedas
        # Inicializa las variables cuando se crea una instancia de la clase
        self.creditos = 0  # La cantidad de créditos inicia en 0.
        self.max_creditos = 999  # Establece el límite máximo de créditos en 999.
        self.opciones = {
            "A": {"nombre": "Bar/Bar", "premio": 100, "probabilidad": 5},
            "B": {"nombre": "Bar", "premio": 50, "probabilidad": 5},
            "C": {"nombre": "77", "premio": 40, "probabilidad": 5},
            "D": {"nombre": "Estrellas", "premio": 30, "probabilidad": 5},
            "E": {"nombre": "Sandia", "premio": 25, "probabilidad": 5},
            "F": {"nombre": "Melón", "premio": 20, "probabilidad": 10},
            "G": {"nombre": "Campana", "premio": 15, "probabilidad": 10},
            "H": {"nombre": "Naranja", "premio": 10, "probabilidad": 10},
            "I": {"nombre": "Manzana", "premio": 5, "probabilidad": 20},
            "J": {"nombre": "Cereza", "premio": 2, "probabilidad": 40}
        }
        self.game_over = False  # Indica si el juego ha terminado o no.

    def insertar_monedas(self, monedas):
        # Método para insertar monedas en la máquina
        if self.creditos + monedas <= self.max_creditos:
            # Verifica que no se supere el límite máximo de créditos
            self.creditos += monedas  # Agrega las monedas a la cantidad de créditos

    def jugar(self):
        # Método para jugar en la máquina tragamonedas
        if self.creditos <= 0:
            self.game_over = True
            return  # Si no hay créditos, el juego termina

        opcion_elegida = input("Elige una opción (A-J): ").upper()
        # El jugador ingresa su elección en mayúsculas para evitar problemas de mayúsculas/minúsculas

        if opcion_elegida in self.opciones and self.creditos > 0:
            # Verifica si la opción elegida es válida y si hay créditos disponibles
            creditos_apostados = int(input("Ingresa cuántos créditos deseas apostar:"))
            # El jugador ingresa la cantidad de créditos que quiere apostar
            
            if creditos_apostados > 9:
                print("Solo puedes apostar hasta 9 créditos.")
                creditos_apostados = 9
                # Se establece un límite máximo de 9 créditos para evitar apuestas mayores
            
            self.creditos -= creditos_apostados
            # Se resta la cantidad de créditos apostados de los créditos actuales

            opciones_posibles = []  # Aquí se almacenan las opciones disponibles
            probabilidades = []  # Aquí se almacenan las probabilidades asociadas a cada opción

            for opcion, info in self.opciones.items():
                opciones_posibles.append(opcion)
                probabilidades.append(info["probabilidad"])
                # Se construyen las listas de opciones y probabilidades para la elección aleatoria

            opcion_aleatoria = random.choices(opciones_posibles, weights=probabilidades)[0]
            # Se elige una opción aleatoria en base a las probabilidades
            print(f"Resultado: {self.opciones[opcion_aleatoria]['nombre']}")
            # Se muestra el resultado del giro

            if opcion_elegida == opcion_aleatoria:
                premio = self.opciones[opcion_elegida]["premio"]
                self.creditos *= premio
                print(f"Felicidades, has ganado {premio} créditos.")
                # Si la opción elegida coincide con la aleatoria, se gana un premio
            else:
                print("Lo siento, no has ganado esta vez.")
                print(f"Resultado: {self.opciones[opcion_aleatoria]['nombre']}")
                # Si no coinciden, se muestra un mensaje de no ganar y el resultado

    def retirar_creditos(self):
        # Método para retirar créditos
        creditos_retirar = int(input("Ingresa cuántos créditos deseas retirar:"))
        self.creditos -= creditos_retirar
        if self.creditos <= 0:
            self.creditos = 0
            # Se resta la cantidad de créditos retirados y se evita que los créditos sean negativos

# Creamos una instancia del juego
tragamonedas = Tragamonedas()

while not tragamonedas.game_over:
    print(f"Créditos actuales: {tragamonedas.creditos}")
    print("1. Insertar monedas")
    print("2. Jugar")
    print("3. Retirar créditos")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        monedas = int(input("Inserta monedas: "))
        tragamonedas.insertar_monedas(monedas)
        # El jugador puede agregar monedas a la máquina
    elif opcion == 2:
        tragamonedas.jugar()
        # El jugador puede jugar
    elif opcion == 3:
        tragamonedas.retirar_creditos()
        # El jugador puede retirar créditos
    elif opcion == 4:
        break  # Sale del bucle si se selecciona la opción de salir
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        # Muestra un mensaje de error para opciones incorrectas

print("¡Gracias por jugar!")  # Mensaje de despedida cuando se termina el juego