import pygame
import menu
import pong
import juego_cuadrado
import nave1
from setting import *

# Inicializar pygame
pygame.init()

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juegos")

# Pasar pantalla a los módulos (si la necesitan)
import builtins
builtins.pantalla = pantalla

# Ejecutar menú UNA SOLA VEZ
opcion = menu.menu(pantalla)

# Ejecutar la opción elegida
if opcion == "pong":
    pong.juego(pantalla)
elif opcion == "cuadrado":
    juego_cuadrado.juego_cuadrado(pantalla)
elif opcion == "nave":
    nave1.esquivar(pantalla)
pygame.quit()
