import pygame

pygame.init()

# Tamaño de la pantalla
ANCHO = 900
ALTO = 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juegos")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Fuentes
fuente_score = pygame.font.Font(None, 60)