import random
import time
import os
import sys
from tabulate import tabulate

from clases import *
from funciones import *
from variables import *

# Funciones:


def maquina_de_escribir(texto, delay_min=0.02, delay_max=0.06):
    # Es una función que hace que el texto que escribes se vea caracter a caracter, dejando un tiempo aleatorio entre letra y letra, por lo que da la sensación de que lo escribe alguien
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(random.uniform(delay_min, delay_max))
    print()

def imprimir_tablero(tablero):
    # Con esta función se genera un tablero con el índice horizontal y vertical, así como una cuadrícula.
    # Esto permite ser más preciso con tus tiradas y que la pantalla quede más clara. 
    tablero_con_indices = [[f"{i}"] + fila for i, fila in enumerate(tablero)]
    # Crear encabezado de columnas
    encabezado = [" "] + [f"{i}" for i in range(10)]
    # Imprimir el tablero con tabulate
    print(tabulate(tablero_con_indices, headers=encabezado, tablefmt="grid"))
          
def verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
    # Verifica que las celdas que el barco ocupará y sus adyacentes estén libres.

    for i in range(x - 1, x + (l if h == "v" else 1) + 1):
        for j in range(y - 1, y + (y if h == "h" else 1) + 1):
            if 0 <= i < len(tablero_maquina) and 0 <= j < len(tablero_maquina[0]):
                if tablero_maquina[i][j] == "B":
                    return False
    return True

def hundido_tocado(i,j,tablero):
    # Con esta función se verifica si la casilla impactada ha producido que la totalidad del barco está hundida o solo tocada.
    # De esta manera se da una pista al jugador para seguir disparando por esa zona 
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            # Verificar que las coordenadas estén dentro del tablero
            if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]):
                # Ignorar la celda actual (i, j)
                if x == i and y == j:
                    continue
                # Verificar si hay un barco en la celda
                if tablero[x][y] == "B":
                    return True
    return False

def todos_los_barcos_hundidos(tablero):
    # Comprueba si hay B en el tablero
    return all("B" not in _ for _ in tablero)

def colocar_barco_aleatorio(tablero_oculto, x, y, h, l):
    # Función para que la máquina coloque los barcos uno por uno, en orden de mayor a menor.
    barcos_colocar = [portaaviones.num_casillas, acorazado.num_casillas, acorazado.num_casillas, destructor.num_casillas, destructor.num_casillas, destructor.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas]
    for n in range(len(barcos_colocar)):
            l = barcos_colocar[n]
            while True:
                h = random.randint(0,1)
                x = random.randint(0,9)
                y = random.randint(0,9)

                if h == 1:
                #horizontal
                    if y + l <= len(tablero_oculto[0]):
                        colocacion_valida = True
                        for j in range(l):
                            if tablero_oculto[x][y+j] == "B":
                                colocacion_valida = False
                            if not verificar_celdas_circundantes(tablero_oculto, x, y, h, l):
                                colocacion_valida = False
                        if colocacion_valida:
                            for j in range(l):
                                tablero_oculto[x][y+j] = "B"
                            break
                    else:
                        # print("El barco no cabe en el tablero_oculto en esta posición.")
                        False
                else:
                    # vertical
                    if x + l <= len(tablero_oculto):
                        colocacion_valida = True
                        for i in range(l):
                            if tablero_oculto[x+i][y] == "B":
                                colocacion_valida = False
                            if not verificar_celdas_circundantes(tablero_oculto, x, y, h, l):
                                colocacion_valida = False
                        if colocacion_valida:
                            for i in range(l):
                                tablero_oculto[x+i][y] = "B"
                            break
                    else:
                        # print("El barco no cabe en el tablero_oculto en esta posición.")
                        False
    return tablero_oculto


def colocar_barco_jugador(tablero_maquina, x, y, h, l):
    # Función para colocar los barcos uno por uno, en orden de mayor a menor.
    barcos_colocar = [portaaviones.num_casillas, acorazado.num_casillas, acorazado.num_casillas, destructor.num_casillas, destructor.num_casillas, destructor.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas]
    for n in range(len(barcos_colocar)):
            l = barcos_colocar[n]
            while True:
                h = str(input("Introduce la dirección del barco (h/v)"))
                while True:
                    x = int(input("Escoge la fila (Entre 0 y 9)"))
                    if x < 0 or x > 9:
                        print("Entre 0 y 10")
                    else:
                        break
                while True:
                    y = int(input("Escoge la fila (Entre 0 y 9)"))
                    if y < 0 or y > 9:
                        print("Entre 0 y 10")
                    else:
                        break
                print(f"Posición elegida: {x},{y}")
                if h == "h" or "horizontal":
                #horizontal
                    if y + l <= len(tablero_maquina[0]):
                        colocacion_valida = True
                        for j in range(l):
                            if tablero_maquina[x][y+j] == "B":
                                print("Hay un barco en esta posición.")
                                colocacion_valida = False
                                #break
                            if not verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
                                print(f"Barco cercano a posiciones cercanas. Escribe una nueva")
                                colocacion_valida = False
                        if colocacion_valida:
                            for j in range(l):
                                tablero_maquina[x][y+j] = "B"
                            imprimir_tablero(tablero_maquina)
                            break
                    else:
                        print("El barco no cabe en el tablero_maquina en esta posición.")
                        False
                elif h == "v" or "vertical":
                    # vertical
                    if x + l <= len(tablero_maquina):
                        colocacion_valida = True
                        for i in range(l):
                            if tablero_maquina[x+i][y] == "B":
                                print("Barco en esa posición. Escribe una nueva")
                                colocacion_valida = False
                                #break
                            if not verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
                                print(f"Barco cercano a posiciones cercanas. Escribe una nueva")
                                colocacion_valida = False
                        if colocacion_valida:
                            for i in range(l):
                                tablero_maquina[x+i][y] = "B"
                            imprimir_tablero(tablero_maquina) 
                            break
                    else:
                        print("El barco no cabe en el tablero_maquina en esta posición.")
                        False
                else:
                    print("Orientación no válida, elige horizontal o vertical:")
    return tablero_maquina

def colocar_barco_jugador_pr(tablero_maquina, x, y, h, l):
    # Función para colocar los barcos uno por uno, en orden de mayor a menor.
    barcos_colocar = [portaaviones.num_casillas, acorazado.num_casillas, acorazado.num_casillas, destructor.num_casillas, destructor.num_casillas, destructor.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas]
    for n in range(len(barcos_colocar)):
            l = barcos_colocar[n]
            while True:
                h = random.randint(0,1)
                x = random.randint(0,9)
                y = random.randint(0,9)

                if h == 1:
                #horizontal
                    if y + l <= len(tablero_maquina[0]):
                        colocacion_valida = True
                        for j in range(l):
                            if tablero_maquina[x][y+j] == "B":
                                colocacion_valida = False
                            if not verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
                                colocacion_valida = False
                        if colocacion_valida:
                            for j in range(l):
                                tablero_maquina[x][y+j] = "B"
                            break
                    else:
                        # print("El barco no cabe en el tablero_oculto en esta posición.")
                        False
                else:
                    # vertical
                    if x + l <= len(tablero_maquina):
                        colocacion_valida = True
                        for i in range(l):
                            if tablero_maquina[x+i][y] == "B":
                                colocacion_valida = False
                            if not verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
                                colocacion_valida = False
                        if colocacion_valida:
                            for i in range(l):
                                tablero_maquina[x+i][y] = "B"
                            break
                    else:
                        # print("El barco no cabe en el tablero_oculto en esta posición.")
                        False
    return tablero_maquina

def disparar_maquina(tablero_maquina):
    tocado = True
    # Así la máquina dispara en posiciones aleatorias dentro de un tablero y si acierta repite tirada.
    while tocado == True:
        # Generar dos números de manera aleatoria
        i = random.randint(0,9)
        j = random.randint(0,9)
        # Solicita esas dos coordenadas a la máquina
        print(f"Tu enemigo ha disparado a la posición [{i},{j}] y el resultado es:")
        # Dispara y comprueba dónde ha impactado.
        # Si acierta
        if tablero_maquina[i][j] == "B":
            tablero_maquina[i][j] = "X" 
            # Comprueba si en los alrededores del objetivo impactado hay casillas que contengan B alrededor
            # Si es así, devuelve 'Tocado'
            if hundido_tocado(i,j,tablero_maquina) == True:
                print(f"\nTocado en posición {i},{j}")
            # Si no, devuelve 'hundido', pues si no hay ninguna B alrededor, ya no hay barco.
            else: 
                print(f"\nHundido en posición {i},{j}")
            # Imprime el tablero y devuelve 'Tocado = True' lo que hace que el bucle se repita (se vuelve a tirar)
            print("\n")
            imprimir_tablero(tablero_maquina)
            tocado = True
            # Si no, devuelve agua y pasa el turno
        elif tablero_maquina[i][j] == " ":
            tablero_maquina[i][j] = "A" 
            print("Agua")
            print("\n")
            imprimir_tablero(tablero_maquina)
            tocado = False
            # Si se dispara dos veces en la misma posición se devuelve el siguiente texto y se pasa el turno como si fuera un disparo fallido.
        else:
            print("\nTu contrincante ha vuelto a disparar en la misma posición.")
            print("\n")
            imprimir_tablero(tablero_maquina)
            tocado = False
        print("\n\n")

def disparar_maquina_2(tablero_oculto):
    tocado = True
    # Así la máquina dispara en posiciones aleatorias dentro de un tablero y si acierta repite tirada.
    while tocado == True:
        # Generar dos números de manera aleatoria
        i = random.randint(0,9)
        j = random.randint(0,9)
        # Solicita esas dos coordenadas a la máquina
        print(f"Tu aliado ha disparado a la posición [{i},{j}] y el resultado es:")
        # Dispara y comprueba dónde ha impactado.
        # Si acierta
        if tablero_oculto[i][j] == "B":
            tablero_oculto[i][j] = "X" 
            # Comprueba si en los alrededores del objetivo impactado hay casillas que contengan B alrededor
            # Si es así, devuelve 'Tocado'
            if hundido_tocado(i,j,tablero_oculto) == True:
                print(f"\nTocado en posición {i},{j}")
            # Si no, devuelve 'hundido', pues si no hay ninguna B alrededor, ya no hay barco.
            else: 
                print(f"\nHundido en posición {i},{j}")
            # Imprime el tablero y devuelve 'Tocado = True' lo que hace que el bucle se repita (se vuelve a tirar)
            print("\n")
            imprimir_tablero(tablero_oculto)
            tocado = True
            # Si no, devuelve agua y pasa el turno
        elif tablero_oculto[i][j] == " ":
            tablero_oculto[i][j] = "A" 
            print("Agua")
            print("\n")
            imprimir_tablero(tablero_oculto)
            tocado = False
            # Si se dispara dos veces en la misma posición se devuelve el siguiente texto y se pasa el turno como si fuera un disparo fallido.
        else:
            print("\nTu aliado ha vuelto a disparar en la misma posición.")
            print("\n")
            imprimir_tablero(tablero_oculto)
            tocado = False
        print("\n\n")

def disparar(tablero_oculto, tablero_visible):
    tocado = True
    # Así el jugador es consultado por las coordenadas en las que disparar, comprueba si están dentro del tablero y si acierta repite tirada.
    while tocado == True:
        # Solicitar coordenadas al usuario
        i = int(input("Introduce la coordenada i (fila): "))
        j = int(input("Introduce la coordenada j (columna): "))
        print(f"Has disparado a la posición [{i},{j}] y el resultado es:")
        # Se comprueba si estas coordenadas coinciden con el tablero.
        # Si es así, se procede a disparar y marcar la tirada.
        if 0 <= i < 10 and 0 <= j < 10:
            # Si aciertas
            if tablero_oculto[i][j] == "B":
                # Si la posición elegida en el tablero_oculto contiene una B, se ha impactado. Se marca una X en el tablero_oculto y se copia en el tablero_visible. Dejando así visible solo el tablero vacío con los aciertos/fallos.
                tablero_oculto[i][j] = "X" 
                tablero_visible[i][j] = "X"
                # Comprueba si en los alrededores del objetivo impactado hay casillas que contengan B alrededor
                # Si es así, devuelve 'Tocado'
                if hundido_tocado(i,j,tablero_oculto) == True:
                    print(f"Tocado en posición {i},{j}")
                # Si no, devuelve 'hundido', pues si no hay ninguna B alrededor, ya no hay barco.
                else: 
                    print(f"Hundido en posición {i},{j}")
                # Imprime el tablero y devuelve 'Tocado = True' lo que hace que el bucle se repita (se vuelve a tirar)
                print("\n")
                imprimir_tablero(tablero_visible)
                tocado = True
            # Si no, devuelve agua y pasa el turno
            elif tablero_oculto[i][j] == " ":
                tablero_oculto[i][j] = "A"
                tablero_visible[i][j] = "A"  
                print("Agua")
                print("\n")
                imprimir_tablero(tablero_visible)
                tocado = False
            # Si se dispara dos veces en la misma posición se devuelve el siguiente texto y se pasa el turno como si fuera un disparo fallido.
            else:
                print("Ya has disparado en esta posición.")
                print("\n")
                imprimir_tablero(tablero_visible)
                tocado = False
        else:
            # Si se dispara a una ubicación fuera del tablero, se devuelve el siguiente texto y se pasa el turno como si fuera un disparo fallido. 
            print("Coordenadas fuera del rango del tablero.")
            tocado = False
        print("\n\n")
        
def turnos(tablero_maquina,tablero_oculto,tablero_visible):
    while True:
        print("Turno de la máquina:")
        disparar_maquina(tablero_maquina)
        if todos_los_barcos_hundidos(tablero_maquina) == True:
            print("¡Has perdido!")
            break
        else:
            True
        print("Tu turno:")
        disparar(tablero_oculto, tablero_visible)
        if todos_los_barcos_hundidos(tablero_oculto) == True:
            print("¡Has ganado!")
            break
        else:
            True
        continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Volviendo al menú principal...")
            time.sleep(2)
            break
        time.sleep(2)
        os.system("cls")

def turnos_prueba(tablero_maquina,tablero_oculto):
    rep = 0
    while True:
        rep += 1
        time.sleep(0.05)
        print("Turno máquina 1:")
        disparar_maquina(tablero_maquina)
        if todos_los_barcos_hundidos(tablero_maquina) == True:
            print(f"¡Máquina 1 ha ganado en {rep} turnos!")
            break
        else:
            True
        time.sleep(0.05)
        print("Turno máquina 2:")
        disparar_maquina_2(tablero_oculto)
        if todos_los_barcos_hundidos(tablero_oculto) == True:
            print(f"¡Máquina 2 ha ganado en {rep} turnos!")
            break
        else:
            True
        time.sleep(0.05)
        # os.system("cls")
    continuar = input("¿Deseas volver al menú principal? (s/n): ").strip().lower()
    if continuar != "s":
        print("Volviendo al menú principal...")
        time.sleep(2)
        True

def preparados():
    # Es una función que escribe que la máquina empezará su turno y hace una cuenta atrás que se puede ver en pantalla.
    maquina_de_escribir("\n¿Estás preparado? La máquina diparará primero...\n")
    maquina_de_escribir("Su turno comenzará en 5...")
    time.sleep(1)
    maquina_de_escribir("4...")
    time.sleep(1)
    maquina_de_escribir("3...")
    time.sleep(1)
    maquina_de_escribir("2...")
    time.sleep(1)
    maquina_de_escribir("1...")
    time.sleep(1)

def introducir_apodo():
    # Es la función introductoria. Hay que perfilarla para que sea un main y se pueda volver a ella al final de la partida.
    maquina_de_escribir("\n¡Bienvenido a Hundir la flota!\n")
    maquina_de_escribir("\nDinos tu nombre\n")
    apodo = str(input("\nIntroduce tu apodo aquí: "))
    maquina_de_escribir(f"\n¡Hola, {apodo}!")
    return

def main():
    introducir_apodo()
    print("\n--- Menú principal ---")
    while True:  
        maquina_de_escribir("\nElige una opción: \n")
        maquina_de_escribir("1. Partida rápida\n2. Partida normal\n3. Partida de exhibición\n4. Instrucciones\n5. Salir\n")
        opcion = int(input("Introduce el número de la opción (1-5): "))
        if opcion == 1:
            partida_rapida()
        elif opcion == 2:
            partida_normal()
        elif opcion == 3:
            partida_exhibicion()
        elif opcion == 4:
            instrucciones()
        elif opcion == 5:
            maquina_de_escribir("\n\n¡Muchas gracias por jugar a Hundir la Flota!\n\n¡Hasta pronto!")
            time.sleep(5)
            break
        else:
            maquina_de_escribir("Opcion no contemplada, elija de la lista de opciones del menú.")


def instrucciones():
    # Al elegir la opción 3 del menú 
    maquina_de_escribir("\nInstrucciones del juego:\n")
    maquina_de_escribir("Hay dos jugadores: tú y la máquina.\nUn tablero cuadrado de 10x10 cuyo tamaño puedes cambiar desde el archivo variables.py\n\nAl entrar al menú principal del juego habrás podido comprobar que hay tres opciones de juego:\n1. Partida rápida.\n2. Partida normal.\n3. Partida de exhibición.\nLas dos primeras son similares en su funcionamiento por turnos, pero la segunda es una partida clásica en la que tendrás que colocar los barcos en la posición que desees evitando colisiones y colocaciones cercanas.\nEn la primera, los barcos se colocarán aleatoriamente (siguiendo el mismo proceso que realiza la máquina) en tu tablero, podrás ver su configuración y la partida comenzará.\nEn la opción llamada partida de exhibición la máquina ocupa el papel de los dos jugadores, generando dos tableros y disparándose en cada turno hasta que uno de los dos se quede sin B y gane. Devolviendo el número de turnos que le ha costado vencer. Va a toda velocidad.\n\nTipos de barcos:\nPara comenzar a jugar tendrán que estar colocados sobre los tableros (horizontal o verticalmente) los siguientes barcos, que se marcarán con una B en el tablero.\n- 1 portaaviones de 4 casillas de eslora.\n- 2 acorazados de 3 casillas de eslora.\n- 3 destructores de 2 casillas de eslora.\n- 4 fragatas de 1 casilla de eslora.\n\n Se irán colocando en ese orden, así que tienes que tener en cuenta que primero colocarás las de mayor tamaño. Tienes que calcular bien los espacios. \n Tras la colocación, comenzará el juego. La máquina siempre realizará el primer disparo sobre tu tablero. Tiene dos opciones que se comparten con tu disparo, acertar o fallar.\n- Acertar se produce cuando el disparo impacta sobre una B, que pasa a convertirse en una X en el tablero. Siempre que la máquina o tú acertéis se marcará si se ha hundido o tocado el barco y se podrá repetir el disparo.\n- Fallar se produce cuando el disparo no impacta sobre una B, existiendo para este caso más casuística.\n  Si se impacta contra una casilla en la que no haya nada, se marcará como Agua.\n  Si impactas en una posición en la que ya habías impactado.\n  Si impactas fuera del tablero (opción que la máquina tiene deshabilitada).\n En todos los casos se perderá el turno y será el del rival.\n\nLa partida finaliza cuando no quede ninguna B en alguno de los tableros. En el caso de ser el tuyo, habrás perdido, y de lo contrario, habrás ganado.")
    continuar = input("¿Deseas volver al menú principal? (s/n): ").strip().lower()
    if continuar != "s":
        print("Volviendo al menú principal...")
        time.sleep(2)
        True

def partida_normal():
    # Al elegir la opción 2 del menú, te hace colocar los barcos en el tablero y después procedéis a jugar
    maquina_de_escribir("Has elegido partida normal, la máquina ya ha colocado sus barcos en el tablero y estaría impaciente, si pudiera estarlo.\nColoca los barcos siguiendo este orden: orientación, fila y columna.\nEl tamaño de los barcos va de mayor a menor, tendrás que colocar 1 de 4 casillas, 2 de 3, 3 de 2 y 4 de 1.\n\n¡Buena suerte!\n")
    # Se generan los tableros
    tablero_oculto = [[" " for _ in range(t)] for _ in range(t)]
    tablero_visible = [[" " for _ in range(t)] for _ in range(t)]
    tablero_maquina = [[" " for _ in range(t)] for _ in range(t)]
    # Se colocan los barcos
    colocar_barco_aleatorio(tablero_oculto, x, y, h, l)
    colocar_barco_jugador(tablero_maquina, x, y, h, l)
    time.sleep(5)
    preparados()
    # Se juega por turnos hasta que uno gane
    turnos(tablero_maquina,tablero_oculto,tablero_visible)

def partida_rapida():
    # Se muestra el mensaje de bienvenida al juego.
    maquina_de_escribir("Has elegido partida rápida, los tableros se generarán aleatoriamente... Solo te tienes que preocupar de jugar bien.\n¡Buena suerte!\n")
    # Al elegir la opción 1 del menú, los barcos se colocan aleatoriamente, como los de la máquina y después procedéis a jugar
    # Se generan los tableros
    tablero_oculto = [[" " for _ in range(t)] for _ in range(t)]
    tablero_visible = [[" " for _ in range(t)] for _ in range(t)]
    tablero_maquina = [[" " for _ in range(t)] for _ in range(t)]
    # Se colocan los barcos
    colocar_barco_aleatorio(tablero_oculto, x, y, h, l)
    colocar_barco_jugador_pr(tablero_maquina, x, y, h, l)
    maquina_de_escribir("Este es tu tablero:\n")
    imprimir_tablero(tablero_maquina)
    time.sleep(5)
    preparados()
    # Se juega por turnos hasta que uno gane
    turnos(tablero_maquina,tablero_oculto,tablero_visible)

def partida_exhibicion():
    # Se muestra el mensaje de bienvenida al juego.
    maquina_de_escribir("Has elegido partida de exhibición, los tableros se generarán aleatoriamente, la máquina combatirá contra sí misma hasta acabar con todos los barcos.\nTú solo tienes que coger las palomitas y distrutar de su autodestrucción...\n")
    # Al elegir la opción 1 del menú, los barcos se colocan aleatoriamente, como los de la máquina y después procedéis a jugar
    # Se generan los tableros
    tablero_oculto = [[" " for _ in range(t)] for _ in range(t)]
    tablero_maquina = [[" " for _ in range(t)] for _ in range(t)]
    # Se colocan los barcos
    colocar_barco_aleatorio(tablero_oculto, x, y, h, l)
    colocar_barco_jugador_pr(tablero_maquina, x, y, h, l)
    maquina_de_escribir("\nEmpezamos\n")
    time.sleep(4)
    # Se juega por turnos hasta que uno gane
    turnos_prueba(tablero_maquina,tablero_oculto)
