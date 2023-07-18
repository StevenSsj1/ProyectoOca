import pygame
import sys
import time
import numpy as np
import random

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width, height = 600, 610
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moviendo un cuadrado")

# Fondo
fondo = pygame.image.load("./imagenes/joaco003.jpg")

import pygame
import random

class Dado:
    def __init__(self):
        self.caras = [
            pygame.image.load("imagenes/Dice1.png"),
            pygame.image.load("imagenes/Dice2.png"),
            pygame.image.load("imagenes/Dice3.png"),
            pygame.image.load("imagenes/Dice4.png"),
            pygame.image.load("imagenes/Dice5.png"),
            pygame.image.load("imagenes/Dice6.png")
        ]
        self.dado_x = 250
        self.dado_y = 250
        self.dado_height = 100
        self.dado_width = 100
        for i in range(6):
            self.caras[i] = pygame.transform.scale(self.caras[i], (self.dado_height, self.dado_height))

    def lanzar_dado(self):
        pygame.time.set_timer(pygame.USEREVENT, 200)
        lanzada_actual = 0
        tiempo_lanzamiento = time.time()
        stop = False

        while not stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.USEREVENT:
                    lanzada_actual = random.randint(0, 5)
                    tiempo_actual = time.time()
                    if tiempo_actual - tiempo_lanzamiento >= 2.0:  # Cambiar el 2.0 a la cantidad de segundos que desees que dure el lanzamiento
                        stop = True

            window.blit(fondo, (0, 0))  # Dibujar el fondo primero
            window.blit(self.caras[lanzada_actual], (250 - self.dado_width // 2, 250 - self.dado_height // 2))  # Superponer el dado sobre el tablero
            pygame.display.update()

        pygame.time.set_timer(pygame.USEREVENT, 0)  # Detener el temporizador
        return lanzada_actual + 1
