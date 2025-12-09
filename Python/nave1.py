import pygame
from setting import *
import random
from menu import *
def esquivar(pantalla):##############################################
    xnave = ANCHO / 2
    ynave = ALTO - 80
    x_speed = 1
    ladoNave = 50
    score = 0

    #Enemigos
    xenemigo = ladoNave/2
    yenemigo = 0

    enemy_size = 50
    y2enemigo = yenemigo+80
    y3enemigo = yenemigo+160
    y4enemigo = yenemigo+240
    random.randint(0, ANCHO - enemy_size)
    enemy_pos = [random.randint(0, ANCHO - enemy_size), 0]
    enemy_list = [enemy_pos]
    enemy_speed_x = 1
    enemy_speed_y = 5
    enemy_existencia = True
    clock = pygame.time.Clock()
    #Lista de enemigos
    enemigos = []

    enemy_size = 50

    for i in range(0,35,5):
        for j in range (0,320,80):

            x = xenemigo * i  # separación entre enemigos
            y =+ j                      # todos en la fila superior
            enemigo = pygame.Rect(x, y, enemy_size, enemy_size)
            enemigo2 = pygame.Rect(x, y, enemy_size, enemy_size)
            enemigo3 = pygame.Rect(x,y+160,enemy_size, enemy_size)
            enemigos.append(enemigo)

    #Disparo
    disparo_ancho = 10
    disparo_alto = 25
    disparo_x = xnave+ladoNave/2-5
    disparo_y = ynave+ladoNave/2
    old_disparo_x = 0
    disparo_vel_x = x_speed
    disparo_vel_y = 3/2
    disapro = False
    ejecutando = True
    while ejecutando:


        # --- EVENTOS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

        # --- MOVIMIENTO y DISPARO (SIEMPRE FUERA DEL FOR EVENT) ---
        mov_nave = pygame.key.get_pressed()
        if mov_nave[pygame.K_a]:
            xnave -= x_speed
            disparo_x -=x_speed
        if mov_nave[pygame.K_d]:
            xnave += x_speed
            disparo_x += disparo_vel_x
        if disapro == False:
            old_disparo_x = disparo_x
        if mov_nave[pygame.K_k]:
            disapro = True
        if disapro:
            disparo_y -= disparo_vel_y
            disparo_x = old_disparo_x
        if disparo_y < 0:       # si sale de la pantalla se desactiva
            disapro = False
            disparo_y = ynave+ladoNave/2
            disparo_x = xnave+ladoNave/2-5
        ###########
        #Movimiento del enemigo#
        ###########
        for enemigo in enemigos:
            enemigo.x += enemy_speed_x

        # Detectar bordes (solo mirar el más a la derecha o izquierda)
        hitting_left = any(e.x <= 0 for e in enemigos)
        hitting_right = any(e.x + e.width >= ANCHO for e in enemigos)

        if hitting_left or hitting_right:
            enemy_speed_x *= -1   # cambio dirección
            for e in enemigos:
                e.y += enemy_speed_y
        # límites
        if xnave < 0:
            xnave = 0
        if xnave > ANCHO - ladoNave:
            xnave = ANCHO - ladoNave
        if disparo_x < ladoNave/2:
            disparo_x = ladoNave/2
        if disparo_x > ANCHO-ladoNave/2:
            disparo_x = ANCHO-ladoNave/2
        rect_enemigo  = pygame.Rect(xenemigo, yenemigo, enemy_size, enemy_size)
        rect_disparo  = pygame.Rect(disparo_x, disparo_y, disparo_ancho, disparo_alto)
        rect_nave = pygame.Rect(xnave, ynave, ladoNave, ladoNave)
        if rect_disparo.colliderect(rect_enemigo):#####################################################################################3
            disparo_y = ynave+ladoNave/2
            disparo_x = xnave+ladoNave/2-5
            disapro = False
        for enemigo in enemigos:
            if enemigo.colliderect(rect_nave) or enemigo.bottom > ALTO:
                pantalla.fill(NEGRO)
                texto = fuente_score.render("PERDISTE", True, ROJO)
                pantalla.blit(texto, (ANCHO/2, ALTO/2))
                pygame.display.update()
                pygame.time.delay(2000)
                return






        for enemigo in enemigos[:]:
            if rect_disparo.colliderect(enemigo):
                enemigos.remove(enemigo)
                disapro = False
                disparo_x = xnave + ladoNave/2-5
                disparo_y = ynave + ladoNave/2
                break



        # --- DIBUJAR ---
        pantalla.fill(NEGRO)

        pygame.draw.rect(pantalla, BLANCO, rect_nave)
        pygame.draw.rect(pantalla, AMARILLO, (disparo_x, disparo_y, disparo_ancho, disparo_alto))
        if len(enemigos) <= 10 and len(enemigos)>1:
            color_enemigo = NARANJA
        else:
            color_enemigo = VERDE
        if len(enemigos) == 1:
            color_enemigo = ROJO
        if len(enemigos) == 0:
            pantalla.fill(NEGRO)
            texto = fuente_score.render("GANASTE", True, BLANCO)
            pantalla.blit(texto, (ANCHO/2, ALTO/2))
            pygame.display.update()
            pygame.time.delay(2000)
            return
        for i in range(0, 35, 5):
            for enemigo in enemigos:
                pygame.draw.rect(pantalla, color_enemigo, enemigo)
        pygame.display.update()


    return