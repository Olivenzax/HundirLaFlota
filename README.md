# HundirLaFlota

1. Estructura del Proyecto
El proyecto está dividido en varios archivos:
funciones.py: Contiene todas las funciones necesarias para el funcionamiento del juego.
clases.py: Define la clase Barco, que representa los barcos del juego.
variables.py: Contiene variables globales que se utilizan en el juego, como el tamaño del tablero.
main.py: Es el punto de entrada del programa, donde se llama a la función main() para iniciar el juego.

2. Clases
Clase Barco (en clases.py):
Esta clase representa un barco en el juego. Cada barco tiene dos atributos:
    nombre: El nombre del barco (por ejemplo, "Fragata").
    num_casillas: El número de casillas que ocupa el barco en el tablero.
'''
class Barco:
    def __init__(self, nombre: str, num_casillas: int):
        self.nombre = nombre
        self.num_casillas = num_casillas
'''

Se crean instancias de la clase Barco para cada tipo de barco:
    fragata: Barco de 1 casilla.
    destructor: Barco de 2 casillas.
    acorazado: Barco de 3 casillas.
    portaaviones: Barco de 4 casillas.

'''
fragata = Barco("Fragata", 1)
destructor = Barco("Destructor", 2)
acorazado = Barco("Acorazado", 3)
portaaviones = Barco("Portaaviones", 4)
'''

3. Variables Globales (en variables.py):
Estas variables se utilizan en todo el juego para configurar el tamaño del tablero y almacenar información sobre la posición y orientación de los barcos.
    t: Tamaño del tablero (por defecto, 10x10).
    x, y: Coordenadas de fila y columna para colocar los barcos.
    l: Longitud del barco (número de casillas).
    h: Orientación del barco (horizontal o vertical).

4. Funciones (en funciones.py):

4.1. Funciones de Utilidad:

maquina_de_escribir(texto, delay_min, delay_max):
Simula una máquina de escribir, mostrando el texto carácter por carácter con un retardo aleatorio entre letras.
Uso: Para dar un efecto visual al mostrar mensajes en la consola.

imprimir_tablero(tablero):
Imprime el tablero en la consola con índices de filas y columnas, utilizando la librería tabulate.
Uso: Para mostrar el estado actual del tablero durante el juego.

4.2. Funciones de Colocación de Barcos:

verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
Verifica si las celdas adyacentes a la posición donde se colocará el barco están libres.
Uso: Para evitar que los barcos se coloquen demasiado cerca unos de otros.

colocar_barco_aleatorio(tablero_oculto, x, y, h, l):
Coloca los barcos de la máquina en posiciones aleatorias en el tablero.
Uso: Para generar el tablero de la máquina al inicio del juego.

colocar_barco_jugador(tablero_maquina, x, y, h, l):
Permite al jugador colocar sus barcos en el tablero, solicitando las coordenadas y la orientación.
Uso: Para que el jugador configure su tablero al inicio del juego.

colocar_barco_jugador_pr(tablero_maquina, x, y, h, l):
Coloca los barcos del jugador de manera aleatoria (similar a colocar_barco_aleatorio).
Uso: Para partidas rápidas donde los barcos se colocan automáticamente.

4.3. Funciones de Disparo:

disparar_maquina(tablero_maquina):
Simula el disparo de la máquina en posiciones aleatorias.
Uso: Para el turno de la máquina durante el juego.

disparar_maquina_2(tablero_oculto):
Similar a disparar_maquina, pero para la segunda máquina en partidas de exhibición.
Uso: Para partidas donde dos máquinas juegan entre sí.

disparar(tablero_oculto, tablero_visible):
Permite al jugador disparar en coordenadas específicas.
Uso: Para el turno del jugador durante el juego.

4.4. Funciones de Verificación:

hundido_tocado(i, j, tablero):
Verifica si un disparo ha tocado o hundido un barco.
Uso: Para determinar si un disparo ha sido efectivo.

todos_los_barcos_hundidos(tablero):
Verifica si todos los barcos en un tablero han sido hundidos.
Uso: Para determinar si el juego ha terminado.

4.5. Funciones de Flujo del Juego:

turnos(tablero_maquina, tablero_oculto, tablero_visible):
Controla el flujo del juego, alternando turnos entre el jugador y la máquina.
Uso: Para partidas normales.

turnos_prueba(tablero_maquina, tablero_oculto):
Similar a turnos, pero para partidas de exhibición donde dos máquinas juegan entre sí.
Uso: Para partidas de exhibición.

preparados():
Muestra una cuenta atrás antes de comenzar el turno de la máquina.
Uso: Para dar un efecto dramático al inicio del juego.

introducir_apodo():
Solicita al jugador que introduzca su nombre o apodo.
Uso: Para personalizar la experiencia del jugador.

main():
Función principal que muestra el menú del juego y permite al jugador elegir entre diferentes modos de juego.
Uso: Para iniciar el juego.

instrucciones():
Muestra las instrucciones del juego.
Uso: Para que el jugador aprenda a jugar.

partida_normal(), partida_rapida(), partida_exhibicion():
Funciones que configuran y ejecutan los diferentes modos de juego.
Uso: Para iniciar partidas según la elección del jugador.

##############################################################################################################

5. Flujo del Juego

Inicio:

El jugador introduce su apodo.
Se muestra el menú principal con opciones para jugar una partida rápida, normal, de exhibición, ver instrucciones o salir.

Colocación de Barcos:
En partidas normales, el jugador coloca sus barcos manualmente.
En partidas rápidas y de exhibición, los barcos se colocan automáticamente.

Turnos:
El juego alterna turnos entre el jugador y la máquina (o entre dos máquinas en partidas de exhibición).
En cada turno, se dispara a una coordenada y se verifica si se ha hundido un barco.

Fin del Juego:
El juego termina cuando todos los barcos de un jugador han sido hundidos.
Se muestra un mensaje de victoria o derrota y se ofrece la opción de volver al menú principal.