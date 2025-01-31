# Juego Piedra, Papel o Tijeras con lógica de comparación

# Mostrar las opciones al usuario
print("Bienvenido al juego Piedra, Papel o Tijeras")
print("Opciones: ")
print("1. Piedra")
print("2. Papel")
print("3. Tijeras")
print("Reglas: ")
print("1 y 1 = ¡Empate!")
print("1 y 2 = Pierde 1 y Gana 2")
print("1 y 3 = Gana 1 y Pierde 3")
print("2 y 1 = Gana 2 y Pierde 1")
print("2 y 2 = ¡Empate!")
print("2 y 3 = Pierde 2 y Gana 3")
print("3 y 1 = Pierde 3 y Gana 1")
print("3 y 2 = Gana 3 y Pierde 2")
print("3 y 3 = ¡Empate!")


# Pedir la elección del usuario
opcion_usuario = input("Elige una opción (1, 2 o 3): ")

# Convertir la elección en texto
if opcion_usuario == "1":
    jugador = "Piedra"
elif opcion_usuario == "2":
    jugador = "Papel"
elif opcion_usuario == "3":
    jugador = "Tijeras"
else:
    print("El tiempo se acabo, perdiste.")
    exit()  # Finaliza el programa si la entrada no es válida

# Definir la jugada de la computadora de forma fija (más adelante se hará aleatoria)
computadora = "Piedra"  # Por ahora, siempre elige "Piedra"

# Mostrar las elecciones
print("\nTú elegiste:", jugador)
print("La computadora eligió:", computadora)

# Determinar el resultado del juego
if jugador == computadora:
    print("¡Empate!")
elif (jugador == "Piedra" and computadora == "Tijeras") or \
     (jugador == "Papel" and computadora == "Piedra") or \
     (jugador == "Tijeras" and computadora == "Papel"):
    print("¡Ganaste!")
else:
    print("Perdiste")

print("Gracias por jugar.")

