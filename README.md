"# Lógica de Programación - Piedra, Papel o Tijeras"

# Descripción del juego
Este proyecto implementa el clásico juego Piedra, Papel o Tijeras en Python. Permite jugar en dos modos:

Modo individual: El jugador compite contra la computadora, la cual elige una opción de forma aleatoria.
Modo multijugador: Dos jugadores pueden enfrentarse, ingresando sus elecciones en secreto.
El juego incluye un sistema de estadísticas y historial de partidas, además de un temporizador que limita el tiempo de respuesta de los jugadores. Este temporizador dura 10 segundos.

# ¿Cómo se juega?
Al ejecutar el programa, se muestra un menú principal con cinco opciones:

    - Jugar solo (contra la computadora)
    - Modo multijugador (2 jugadores)
    - Ver reglas
    - Ver estadísticas
    - Salir

Si se elige cualquiera de las 2 primeras opciones para jugar, el usuario o los usuarios deben seleccionar cuántas rondas desean jugar.
Cada jugador debe ingresar su opción (1: Piedra, 2: Papel, 3: Tijeras) dentro del tiempo permitido. Las Reglas son las siguientes:

    - Piedra vence a tijeras
    - Tijeras vence a Papel
    - Papel vence a Piedra
    - Si los usuarios sacan la misma opción es un empate

Se determina el ganador de la ronda según las reglas del juego.
Al finalizar, se muestran las estadísticas de las partidas jugadas.

# Ambiente de Desarrollo
IDE utilizado: Visual Studio Code
Lenguaje de programación: Python
Versión del lenguaje: Python 3.11.0


# Cración de cuenta en GitHub

Esta fue la primera vez que realizó un proceso como este. Primero investigue sobre que es GitHub y como era beneficioso para los desarrolladores. Vi videos en youtube para tener más claro todo y no cometer errores en la configuración. También investigue en los motores de busqueda para ver pasos y guiarme de los comandos que necesitaría para configurar mi repositorio. Este proceso se puede hacer con la terminal de la computadora o en la terminal de Visual Studio Code

# Configuración del Repositorio en GitHub

1. Se creó un repositorio en GitHub llamado **"L-gicaDeProgramacion_PiedraPapelTijeras"**.
2. No se marcó la opción "Add a README file", por lo que este archivo se creó manualmente después. En este punto no sabía si eso me iba a traer problemas a futuro pero luego si pude igual subir el README.md sin ningun problema
3. Se configuró **Git** en la computadora para poder trabajar con el repositorio. Esto lo configuramos en la terminal, esto nos permitio crear la carpeta que tendría los archivos para subirlos al respositorio.


# Clonación del Repositorio y Creación de Archivos Iniciales
   
   Se clonó el repositorio en la computadora utilizando el siguiente comando:

   git clone https://github.com/SamuelGuasco/L-gicaDeProgramacion_PiedraPapelTijeras.git

   Se utilizó este comando en vez de git init que sirve para crear un repositorio desde cero porque al crear mi cuenta en github pensé que solo había que crear el repositorio y subir los archivos de manera manual al repositorio creado y no sabia que se podía hacer desde la terminal. Despúes de seguir investigando me di cuenta de ello, pero lo que era más recomendable era clonar ese repositorio a pesar de que esta sin nada de archivos para configurar mi respositorio en mi computadora.

# Liberías utilizadas
    
    - Random: Esta se uso para generar la elección aleatoria de la computadora
    - Getpass: Esta permite que en el modo multijugador las opciones que escoge cada usuario sea secreta
    - Threading: Implementa un temporizador para limitar el tiempo de respuesta
    - Time: Controla el tiempo de espera y pausa dentro del juego. En este caso trabaja en conjunto con la librería de threading.

    Todas estas librerías estan incluidas en python, por lo que no se tuvo que hacer ninguna instalación fuera del entorno ya implementado. Solo se importó directamente.

# Estructura del Repositorio

```L-gicaDeProgramación_PiedraPapelTijeras```
    ```DiagramaDe_Flujo/``` 
            ```DiagramaDeFlujoTA2/ (Diagramas de flujo anteriores)```
            ```DiagramaDeFlujoTA3/ (Diagramas de flujo actualizados)```
                ```DiagramaDeFlujoParte1.png```
                ```DiagramaDeFlujoParte2.png```

La estructura del repositorio está organizada en carpetas que agrupan los diferentes elementos del proyecto de manera clara y estructurada. Dentro del repositorio principal, se encuentran dos carpetas principales: DiagramaDeFlujo y DiagramasUML. En DiagramaDeFlujo, hay subcarpetas correspondientes a cada tarea, permitiendo conservar versiones anteriores y la versión más reciente de los diagramas en archivos de imagen bien identificados. De la misma, en DiagramasUML, se almacenan diagramas relevantes, como el de casos de uso, arquitectura del software y diagrama de clases, organizados pora la la tarea anterior y el que se actualizó para esta tarea fue el diagrama de casos de uso. Además, el archivo principal del código, juego.py, está ubicado en el repositorio para que se fácil de encontrar, junto con el archivo README.md, que contiene información esencial sobre el proyecto, su instalación y uso. Esta organización permite una fácil navegación asegurando que toda la información relevante esté disponible para su revisión y actualización.


