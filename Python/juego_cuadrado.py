import pygame
from setting import *

def juego_cuadrado(pantalla):
    maze = [
    "011111111111111111111111111111",
    "000000000000000000000000000001",
    "111101010011000000000011111101",
    "011001010010100000001110000001",
    "000001010010100000110010110001",
    "111101010010100001100001010011",
    "100001010010100010000011100101",
    "101111010010111100000000000001",
    "000000010010000000001111111101",
    "100101110011110000000000000001",
    "100100000000010001111110001111",
    "100111111111110000000001000001",
    "100100000000000000000000100001",
    "100000111111100000000000100001",
    "100001000000000000000000010001",
    "100110000000100100000000010001",
    "100011111000101111110000010001",
    "100011010011101000001000010001",
    "111110010010001111100100010001",
    "100000010010000000100010000001",
    "101111110011111110111001000001",
    "100000000000000010000000000001",
    "111111111111111011111111111111"
    ]
    x = 0
    y = 0
    tam = 30
    tam2 = 50
    vel_x = 1/3
    vel_y = 1/3
    rojo_x = 800 - tam
    rojo_y = 600 - tam

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

        # Guardar posición anterior (necesario para la colisión)
        old_x, old_y = x, y

        # Movimiento básico
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_s]: y += vel_y
        if teclas[pygame.K_w]: y -= vel_y
        if teclas[pygame.K_a]: x -= vel_x
        if teclas[pygame.K_d]: x += vel_x

        # Límites de la pantalla
        if y < 0: y = 0
        if y > ALTO - tam: y = ALTO - tam
        if x < 0: x = 0
        if x > ANCHO - tam: x = ANCHO - tam

        # Rectángulos del juego
        rect_azul  = pygame.Rect(x, y, tam, tam)
        rect_rojo  = pygame.Rect(rojo_x, rojo_y, tam, tam)

        # Lista de paredes (IMPORTANTE)

        # --- COLISIÓN CON PAREDES

        # --- COLISIÓN CON META ---
        if rect_azul.colliderect(rect_rojo):
            pantalla.fill(NEGRO)
            texto = fuente_score.render("GANASTE", True, BLANCO)
            pantalla.blit(texto, (260, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            return

        # Dibujar
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, AZUL, rect_azul)
        pygame.draw.rect(pantalla, ROJO, rect_rojo)
        for fila in range(len(maze)):
            for col in range(len(maze[fila])):
                if maze[fila][col] == "1":
                    rect_verde  = pygame.Rect(col * tam, fila * tam, tam, tam)
                    pygame.draw.rect(pantalla,(0,255,0), rect_verde)
                    if rect_azul.colliderect(rect_verde):
                        x = old_x
                        y = old_y

        pygame.display.update()