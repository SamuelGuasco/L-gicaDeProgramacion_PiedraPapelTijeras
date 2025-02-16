# Juego Piedra, Papel o Tijeras con lógica de comparación
import random  # Para la elección aleatoria de la computadora
import getpass  # Para ocultar la entrada en modo multijugador
import threading  # Para implementar el temporizador
import time  # Para manejar las pausas del temporizador

# Variables para estadísticas
estadisticas = {
    "total_partidas": 0, # Número total de partidas jugadas
    "jugador_1_ganadas": 0, # Veces que ha ganado el jugador 1
    "jugador_2_ganadas": 0, # Veces que ha ganado el jugador 2
    "computadora_ganadas": 0, # Veces que ha ganado la computadora esto para cuando se juega en modo solo
    "empates": 0, #número de empates
    "historico": []
}

def mostrar_menu(): # Esta función se creó para que el usuario pueda ver la primera interacción y decidir que hacer. Esta sería la función principal.
    """Muestra el menú principal del juego y captura la elección del usuario"""
    while True: # Se mantiene el bucle hasta que el jugador escoja la opción 5 y pueda salir
        print("\n🎮 Bienvenido al Juego: Piedra, Papel o Tijeras 🎮")
        print("1. Jugar solo (contra la computadora)")
        print("2. Modo multijugador (2 jugadores)")
        print("3. Reglas")
        print("4. Ver estadísticas")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ") # Se utilizó input para que el usuario pueda seleccionar una opción.
# Se dirige a la función correspondiente, dependiendo de que opción se escoja
        if opcion == "1":
            mostrar_reglas()
            jugar_contra_pc()
        elif opcion == "2":
            mostrar_reglas()
            jugar_multijugador()
        elif opcion == "3":
            mostrar_reglas()
        elif opcion == "4":
            ver_estadisticas()
        elif opcion == "5":
            print("Gracias por jugar Piedra, Papel y Tijeras. ¡Hasta la próxima! 🎉")
            break #Termina el bucle y finaliza el juego
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_reglas(): # Esta función muestra las reglas. Se creó para que los jugadores puedan ver las reglas antes de jugar o incluso al inicio de la partida.
    """Muestra las reglas del juego antes de empezar"""
    # Print se usa basntante en el código porque es fácil de usar y mayormente la usó para mostrar el texto o lo que se desea mostrar al usuario
    print("\n📜 REGLAS DEL JUEGO 📜") 
    print("1️⃣ Piedra vence a Tijeras, Tijeras vence a Papel, y Papel vence a Piedra.")
    print("2️⃣ Si ambos jugadores eligen la misma opción, es un empate.")
    print("3️⃣ En modo multijugador, cada jugador elige en secreto su opción.")
    print("4️⃣ El juego continúa hasta que decidas salir.\n")

def jugar_contra_pc(): # Esta función es creada para que el jugador 1 pueda jugar solo contra la computadora quien puede escoger una opción aleatoria
    """Modo de juego contra la computadora"""
    opciones = ["Piedra", "Papel", "Tijeras"]

    print("\n🔹 Modo: Jugador vs Computadora")
    nombre_jugador = input("Ingrese su nombre: ")

    while True: # Este es bucle que permite repetir el juego si el jugador lo desea.
        try:
            rondas = int(input(f"{nombre_jugador}, ¿cuántas rondas deseas jugar? (Ingrese un número): "))
            if rondas <= 0:
                print("Debe ingresar un número mayor a 0.")
                continue
            break # Se agrega un bucle si la entrada es válida
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

    while True:  # Este bucle es para mantener el juego activo hasta que el jugador desee salir
        for ronda in range(rondas): #Se usa for para que el jugador pueda decir el número de rondas
            print(f"\n🔄 Ronda {ronda + 1} de {rondas}")
            print("\nOpciones: 1) Piedra  2) Papel  3) Tijeras")
# Se obtiene la elección del jugador con tiempo
            eleccion_usuario = obtener_eleccion_tiempo(f"{nombre_jugador}, elija una opción (1-3): ") 

            if not eleccion_usuario:
                print(f"⏳ Se acabó el tiempo, {nombre_jugador} pierde esta ronda automáticamente.")
                estadisticas["computadora_ganadas"] += 1
                estadisticas["total_partidas"] += 1

                estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {nombre_jugador} perdió - Computadora ganó")

                continue # Pasa a la siguiente ronda

            eleccion_usuario = opciones[int(eleccion_usuario) - 1]
            eleccion_pc = random.choice(opciones) #En esta parte utilizamos la biblioteca de random para que la computadora escoja una opción aleatoriamente

            print(f"\n{nombre_jugador} eligió: {eleccion_usuario}")
            print(f"Computadora eligió: {eleccion_pc}")

            resultado = determinar_ganador(eleccion_usuario, eleccion_pc)
# Se imprime quién gana la ronda
            if resultado == "jugador1":
                print(f"\n🏆 ¡{nombre_jugador} gana esta ronda! 🎉")
                estadisticas["jugador_1_ganadas"] += 1
            elif resultado == "empate":
                print("\n🤝 ¡Empate!")
                estadisticas["empates"] += 1
            else:
                print("\n💻 ¡La computadora gana esta ronda! 😞")
                estadisticas["computadora_ganadas"] += 1

            estadisticas["total_partidas"] += 1 # Se incrementa el total de partidas después de registrar la partida
            #Esta parte utilizamos las condicionales para registrar el historial además se usó append para poder guardar los registros de las rondas anteriores.
            if resultado == "jugador1":
                estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {nombre_jugador} ganó - Computadora perdió")
            elif resultado == "empate":
                estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {nombre_jugador} empató - Computadora empató")
            else:
                estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {nombre_jugador} perdió - Computadora ganó")
            
        if not jugar_otra_vez():
            break  # Si el jugador no quiere jugar de nuevo, sale del bucle y vuelve al menú principal

def jugar_multijugador(): # Esta función es creada para que se pueda jugar con 2 personas en una misma partida. Ademas sus elecciones no son visibles. Esto gracias a la biblioteca getpass importada en este código
    """Modo de juego entre dos jugadores"""
    opciones = ["Piedra", "Papel", "Tijeras"]

    print("\n🔹 Modo: Jugador 1 vs Jugador 2")
    jugador_1 = input("Nombre del Jugador 1: ")
    jugador_2 = input("Nombre del Jugador 2: ")

    while True: # Se mantiene el bucle para que los jugadores puedan repetir el juego si así lo desean.
        try:
            rondas = int(input(f"{jugador_1} y {jugador_2}, ¿cuántas rondas desean jugar? (Ingrese un número): ")) #En esta aprte se utilizó int para que ingresen números enteres e input para que el jugador pueda poner el número
            if rondas <= 0:
                print("Debe ingresar un número mayor a 0.")
                continue
            break
        except ValueError: #Esta fue para cuando registran un valor no valido
            print("Entrada inválida. Ingrese un número válido.")

    while True:  # Se agrega un bucle para repetir el juego
        for ronda in range(rondas):
            print(f"\n🔄 Ronda {ronda + 1} de {rondas}")
            print("\nOpciones: 1) Piedra  2) Papel  3) Tijeras")
# Se ejecuta el temproizador y si el jugador no escoge una opción se marca como perdida y se suma a las estadísticas a favor del otro jugador.
            eleccion_1 = obtener_eleccion_tiempo(f"{jugador_1}, elija una opción (1-3) en secreto: ", ocultar=True)
            if not eleccion_1:
                print(f"⏳ Se acabó el tiempo, {jugador_1} pierde esta ronda automáticamente.")
                actualizar_estadisticas("jugador2", jugador_1, jugador_2)
                continue

            eleccion_2 = obtener_eleccion_tiempo(f"{jugador_2}, elija una opción (1-3) en secreto: ", ocultar=True)
            if not eleccion_2:
                print(f"⏳ Se acabó el tiempo, {jugador_2} pierde esta ronda automáticamente.")
                actualizar_estadisticas("jugador1", jugador_1, jugador_2)
                continue

            eleccion_1 = opciones[int(eleccion_1) - 1]
            eleccion_2 = opciones[int(eleccion_2) - 1]

            print(f"\n{jugador_1} eligió: {eleccion_1}")
            print(f"{jugador_2} eligió: {eleccion_2}")
# Se imprime quién gana la partida, en esta parte se imprime el nombre que coloca cad jugador
            resultado = determinar_ganador(eleccion_1, eleccion_2)
            if resultado == "empate":
                print("\n🤝 ¡Empate!")
            elif resultado == "jugador1":
                print(f"\n🏆 ¡{jugador_1} gana esta ronda! 🎉")
            else:
                print(f"\n🏆 ¡{jugador_2} gana esta ronda! 🎉")

            actualizar_estadisticas(resultado, jugador_1, jugador_2)

        if not jugar_otra_vez():
            break  # Si no quiere repetir, se sale del bucle y vuelve al menú principal


def obtener_eleccion_tiempo(mensaje, ocultar=False): # Esta función nos permite añadir el temporizador, si el jugador se tarda mucho pierde y el otro gana.
    """Función que permite ingresar una opción con un tiempo límite"""
    eleccion = [None] #Se usa una Lista para poder modificar su valor dentro del temporizador

    def temporizador(): #Esta se define como una función que actúa como el temporizador.
        time.sleep(10) #La función espera 10 segundo antes continuar.
        if eleccion[0] is None: #Esto verifica si el usuario no ha escogido la opción durante los 10 segundos. En caso de no insertar nada se imprime que se acabo el tiempo.
            print("\n⏳ Se acabó el tiempo, perdiste esta ronda automáticamente.")

    thread = threading.Thread(target=temporizador) # En esta parte se utilizó la biblioteca de Threading para que se pueda crear el temproizador
    thread.start() # Esto para que la cuenta regresiva comience

    if ocultar: #Esto es para que se pueda ocultar las opciones en el modo multijugador
        eleccion[0] = getpass.getpass(mensaje) # Se usó la biblioteca de getpass para ocultar las entradas de las opciones en el modo multijugador
    else:
        eleccion[0] = input(mensaje) #input en esta parte nos permite capturar la entrada normalmente a pesar de que no pueda verse

    return eleccion[0] # Se devuelve a la elección

def determinar_ganador(jugador1, jugador2): # Esta función es para definir la lógica para comparar las elecciones y definir un ganador
    """Determina el resultado de la partida"""
    if jugador1 == jugador2:
        return "empate"
    
    condiciones_ganadoras = {
        "Piedra": "Tijeras",
        "Papel": "Piedra",
        "Tijeras": "Papel"
    }

    return "jugador1" if condiciones_ganadoras[jugador1] == jugador2 else "jugador2"
# Se actualizan los contadores de victorias, empates y partidas jugadas.
def actualizar_estadisticas(resultado, jugador1, jugador2): # Esta función permite llevar un registro de las partidas jugadas de los jugadores
    """Actualiza las estadísticas del juego y almacena el historial de cada partida"""
    estadisticas["total_partidas"] += 1
# El historial almacena cada partida con su número y el resultado correspondiente.
    if resultado == "jugador1":
        estadisticas["jugador_1_ganadas"] += 1
        estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {jugador1} ganó - {jugador2} perdió")
    elif resultado == "jugador2":
        estadisticas["jugador_2_ganadas"] += 1
        estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {jugador1} perdió - {jugador2} ganó")
    else:
        estadisticas["empates"] += 1
        estadisticas["historico"].append(f"Partida {estadisticas['total_partidas']}: {jugador1} empató - {jugador2} empató")

def ver_estadisticas(): #Esta función se creó para ver el historial de partidas jugadas.
    """Muestra el historial de partidas jugadas"""
    print("\n📊 Estadísticas del juego:")
    print(f"Total de partidas jugadas: {estadisticas['total_partidas']}")
    print(f"Jugador 1 ganó: {estadisticas['jugador_1_ganadas']} veces")
    print(f"Jugador 2 ganó: {estadisticas['jugador_2_ganadas']} veces")
    print(f"Computador ganó:{estadisticas['computadora_ganadas']} veces")
    print(f"Empates: {estadisticas['empates']} veces")

    print("\n📜 Historial de partidas:")
    if estadisticas["historico"]:
        for partida in estadisticas["historico"]:
            print(partida)
    else:
        print("Aún no se han jugado partidas.")


def jugar_otra_vez(): # Esta función se creó para que el jugador decida si jugar nuevamente con el mismo número de rondas si no regresa al menu principal.
    """Pregunta si los jugadores quieren jugar con el mismo número de rondas"""
    return input("\n¿Quieres jugar con el mismo número de rondas otra vez? (si/no): ").lower() == "si"

if __name__ == "__main__":
    mostrar_menu()

