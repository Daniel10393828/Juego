import pygame
from ..setting import *

def juego(pantalla):
    ancho = 25
    largo = 100

    x = 0
    y = (600 - largo) / 2

    x2 = ANCHO - ancho
    y2 = (ALTO - largo) / 2

    velocidad = 1

    ball_x = ANCHO/2
    ball_y = ALTO/2
    ball_size = 20

    ball_vel_x = 1/3
    ball_vel_y = 1/3

    score1 = 0
    score2 = 0

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

        teclas = pygame.key.get_pressed() ######################################################

        # Movimiento jugador 1
        if teclas[pygame.K_w]:
            y -= velocidad
        if teclas[pygame.K_s]:
            y += velocidad

        # Movimiento jugador 2
        if teclas[pygame.K_UP]:
            y2 -= velocidad
        if teclas[pygame.K_DOWN]:
            y2 += velocidad

        # Límites
        if y < 0: y = 0
        if y > ALTO - largo: y = ALTO - largo

        if y2 < 0: y2 = 0
        if y2 > ALTO - largo: y2 = ALTO - largo

        # Movimiento de pelota
        ball_x += ball_vel_x
        ball_y += ball_vel_y

        # Rebote arriba / abajo
        if ball_y < 0 or ball_y > ALTO - ball_size:
            ball_vel_y *= -1

        # Rebote paleta izquierda
        if (ball_x <= x + ancho and
            ball_y + ball_size >= y and
            ball_y <= y + largo):
            ball_vel_x *= -1

        # Rebote paleta derecha
        if (ball_x + ball_size >= x2 and
            ball_y + ball_size >= y2 and
            ball_y <= y2 + largo):
            ball_vel_x *= -1

        # Puntos
        if ball_x < 0:
            score2 += 1
            ball_x = 400
            ball_y = 300
            ball_vel_x *= -1

        if ball_x > ANCHO - ball_size:
            score1 += 1
            ball_x = 400
            ball_y = 300
            ball_vel_x *= -1

        if score1 == 10 or score2 == 10:
            score1 = 0
            score2 = 0

        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, BLANCO, (x, y, ancho, largo))
        pygame.draw.rect(pantalla, BLANCO, (x2, y2, ancho, largo))
        pygame.draw.rect(pantalla, BLANCO, (ball_x, ball_y, ball_size, ball_size))

        texto = fuente_score.render(f"{score1}   {score2}", True, BLANCO)
        pantalla.blit(texto, (400, 20))

        pygame.display.update()
        pygame.display.update()