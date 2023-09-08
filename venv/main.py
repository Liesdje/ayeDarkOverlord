import random
from cartasExcusa import cartasExcusa
from cartasAccion import cartasAccion
from Utils import barajarCartas

# Barajar las cartas
barajarCartas(cartasExcusa)
barajarCartas(cartasAccion)

# Definir los jugadores
jugadores = ["Jugador 1", "Jugador 2", "Jugador 3"]

# Iniciar el juego
señor_oscuro = random.choice(jugadores)
print(f"El Señor Oscuro es {señor_oscuro}")

while True:
    for jugador in jugadores:
        print(f"Turno de {jugador}:")
        input("Presiona Enter para continuar...")


        #Anadir logica para saber si es necesario robar o no (Hay que llevar la mano)
        # Simular robar una carta de Excusa
        cartasExcusa = cartasExcusa.pop(0)
        print(f"{jugador} roba una carta de Excusa: {cartasExcusa}")

        # Simular robar una carta de Acción
        cartasAccion = cartasAccion.pop(0)
        print(f"{jugador} roba una carta de Acción: {cartasAccion}")

        # Logica para contar la historia (un boton de done?)

        # Simular al Señor Oscuro respondiendo o asignando Miradas Fulminantes
        respuesta_señor = random.choice(["Mirada Fulminante", "Sigue la historia"])
        if respuesta_señor == "Mirada Fulminante":
            print(f"El Señor Oscuro lanza una Mirada Fulminante a {jugador} por su explicación insatisfactoria.")
            # Registro miradas fulminantes

    # Logica de verificacion para alguien que ha perdido
