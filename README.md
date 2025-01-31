"# Lógica de Programación - Piedra, Papel o Tijeras"

Este repositorio forma parte del desarrollo del juego "Piedra, Papel o Tijeras" en el contexto del aprendizaje de programación. En este documento se detalla el proceso seguido para configurar el entorno de desarrollo, trabajar con Git, Github y documentar los avances.

# Cración de cuenta en GitHub

Esta fue la primera vez que realizó un proceso como este. Primero investigue sobre que es GitHub y como era beneficioso para los desarrolladores. Vi videos en youtube para tener más claro todo y no cometer errores en la configuración. También investigue en los motores de busqueda para ver pasos y guiarme de los comandos que necesitaría para configurar mi repositorio. Este proceso se puede hacer con la terminal de la computadora.

# Configuración del Repositorio en GitHub

1. Se creó un repositorio en GitHub llamado **"LógicaDeProgramacion_PiedraPapelTijeras"**.
2. No se marcó la opción "Add a README file", por lo que este archivo se creó manualmente después. En este punto no sabía si eso me iba a traer problemas a futuro pero luego si pude igual subir el README.md sin ningun problema
3. Se configuró **Git** en la computadora para poder trabajar con el repositorio. Esto lo configuramos en la terminal, esto nos permitio crear la carpeta que tendría los archivos para subirlos al respositorio.


# Clonación del Repositorio y Creación de Archivos Iniciales

1. Se clonó el repositorio en la computadora utilizando el siguiente comando:

   git clone https://github.com/SamuelGuasco/L-gicaDeProgramacion_PiedraPapelTijeras.git

   Se utilizó este comando en vez de git init que sirve para crear un repositorio desde cero porque al crear mi cuenta en github pensé que solo había que crear el repositorio y subir los archivos de manera manual al repositorio creado y no sabia que se podía hacer desde la terminal. Despúes de seguir investigando me di cuenta de ello, pero lo que era más recomendale era clonar ese repositorio a pesar de que esta sin nada de archivos para configurar mi respositorio en mi computadora.
   
2. luego se utilizo el siguiente comando:

   cd L-gicaDeProgramacion_PiedraPapelTijeras


4. Luego en la terminal se creo el archivo README.md dentro de la carpeta L-gicaDeProgramacion_PiedraPapelTijeras y una vez creado utilizamos el siguiente comando para subirlo a github:

git add README.md
git commit -m "Archivo Agregado README.md"
git push origin main

Esto me permitió subirlo a GitHub y hacer mis primero commits. Una vez subido a la plataforma el documento se puede editar directo desde el Repositorio. Sin embargo, este es un trabajo práctico y de investigación por esta razón se realizo todo en Visual Studio Code y para subir un nuevo documento o actualizar el README.md se uso la terminal de la computadora. 

Se creo un documento llamado juego.py y lo subí al repositorio usando el siguiente comando dentro de la terminal. 

git add juego.py
git commit -m "Añadido archivo juego.py"
git push origin main

Después de realizar este tema solo se hacen actualizaciones al documento usando los mismos comandos anteriormente mencionados.

# Desarrollo del código para el juego Piedra, Papel, tijeras

Avanazamos hasta la siguiente parte en la generación del código para el programa esocogido en el Trabajo Autónomo 1. En este se avanzo con lo siguiente que se ha aprendido en clase. Además con un poco de investigación y ejemplos encontrados en el buscador se pudo desarrollar lo siguiente:


```python
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

