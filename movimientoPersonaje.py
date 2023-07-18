import pygame
import sys
import time
from Dado import Dado
import tkinter as tk
from newWindow import NewScreen
# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width, height = 600, 610
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moviendo un cuadrado")

# Fondo
fondo = pygame.image.load("imagenes/joaco003.jpg")

# Cargar la imagen del jugador
jugador1_imagen = pygame.image.load("imagenes/p1.png")
jugador2_imagen = pygame.image.load("imagenes/p2.png")

# Escalar la imagen del jugador (opcional)
jugador1_imagen = pygame.transform.scale(jugador1_imagen, (50, 50))
jugador2_imagen = pygame.transform.scale(jugador2_imagen, (50, 50))

# Definir la velocidad de movimiento del cuadrado
speed = 1
casillas_con_pregunta = [1,2,3,4,5,6,7,8]
jugadorActual = 1
# Tupla con posiciones de las casillas
posicionCasillas = (
    (124, 90), (103, 157), (106, 224), (147, 267), (217, 285),
    (383, 284), (467, 284), (514, 215), (502, 135), (446, 94)
)

def mostrarVentanaPregunta():
    root = tk.Tk()
    question_list = ["1", "2", "3"]
    NewScreen(root, question_list)
    root.mainloop()

class Jugador:
    def __init__(self, x, y, speed, imagen):
        self.speed = speed
        self.x = x
        self.y = y
        self.imagen = imagen
        self.imagen_actual = imagen 

    def avanzarCasillas(self, pos):
        target_x, target_y = posicionCasillas[pos]

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed

        if self.y == target_y:
            if self.x < target_x:
                self.x += self.speed
            elif self.x > target_x:
                self.x -= self.speed

        return self.x, self.y

    def dibujarJugador(self, ventana):
        ventana.blit(self.imagen_actual, (self.x, self.y))
            
jugador1 = Jugador(50, 50, speed, jugador1_imagen)  # Imagen del jugador 1
jugador2 = Jugador(100, 100, speed, jugador2_imagen)  # Imagen del jugador 2   

indice_casilla_jugador1 = 0
indice_casilla_jugador2 = 0
def cambiarTurno():
    global jugadorActual
    if jugadorActual == 1:
        jugadorActual = 2
    else:
        jugadorActual = 1

def limpiarVentana():
    window.blit(fondo, (0, 0))

def lanzar_dado():
    dado = Dado()
    resultado = dado.lanzar_dado()
    print("Resultado:", resultado)
    return resultado

resultado_dado = 0

def lanzar_dado_evento():
    resultado_dado = lanzar_dado()
    if jugadorActual == 1:
        mover_jugador_actual(jugador1, resultado_dado)
    else:
        mover_jugador_actual(jugador2, resultado_dado)
    cambiarTurno()



mensaje_mostrado = False
tiempo_mostrar_mensaje = None
mostrando_pregunta = False

def mostrar_mensaje(mensaje):
    font = pygame.font.Font(None, 36)
    texto = font.render(mensaje, True, (255, 255, 255))
    window.blit(texto, (150, 250))
    pygame.display.update()
    time.sleep(3)

# Definir el evento personalizado para lanzar el dado
LANZAR_DADO_EVENT = pygame.USEREVENT + 1


def mover_jugador_actual(jugador, resultado_dado):
    global jugadorActual, indice_casilla_jugador1, indice_casilla_jugador2, mostrando_pregunta


    if jugadorActual == 1:
        casilla_actual = indice_casilla_jugador1
    else:
        casilla_actual = indice_casilla_jugador2

    target_casilla = casilla_actual + resultado_dado

    if target_casilla < len(posicionCasillas):
        target_x, target_y = posicionCasillas[target_casilla]

        while (jugador.x, jugador.y) != (target_x, target_y):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if jugador.x < target_x:
                jugador.x += jugador.speed
            elif jugador.x > target_x:
                jugador.x -= jugador.speed

            if jugador.y < target_y:
                jugador.y += jugador.speed
            elif jugador.y > target_y:
                jugador.y -= jugador.speed
                
        

            #limpiarVentana()
            jugador1.dibujarJugador(window)
            jugador2.dibujarJugador(window)
            pygame.display.update()

            # Pequeño retraso para visualizar el movimiento
            pygame.time.delay(10)

        # Actualizar el índice de la casilla para el jugador correspondiente
        if jugadorActual == 1:
            indice_casilla_jugador1 = target_casilla
        else:
            indice_casilla_jugador2 = target_casilla

    
    if (jugador.x, jugador.y) == posicionCasillas[1]:
            mostrar_mensaje("¡Jugador 1 ha ganado!")      
                 
def manejar_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Presionar la tecla de espacio para lanzar el dado
                lanzar_dado_evento()
    if not pygame.display.get_init():  # Comprobar si la ventana ha sido cerrada
        cambiarTurno()

clock = pygame.time.Clock()

while True:
    tiempo_actual = pygame.time.get_ticks()

    limpiarVentana()
    manejar_eventos()

    if jugador1.x == posicionCasillas[-1][0] or jugador2.x == posicionCasillas[-1][0]:
        mostrar_mensaje("¡Jugador {} ha ganado!".format(jugadorActual))

    for casilla_idx in casillas_con_pregunta:
        if jugador1.x  == posicionCasillas[casilla_idx][0] and not mostrando_pregunta:
            # Mostrar la ventana de pregunta solo una vez cuando llega a la casilla
            mostrarVentanaPregunta()
            mostrando_pregunta = True
            break
        elif jugador2.x == posicionCasillas[casilla_idx][0] and not mostrando_pregunta:
            # Mostrar la ventana de pregunta solo una vez cuando llega a la casilla
            mostrarVentanaPregunta()
            mostrando_pregunta = True
            
            break

    jugador1.dibujarJugador(window)
    jugador2.dibujarJugador(window)
    pygame.display.update()
    clock.tick(60)