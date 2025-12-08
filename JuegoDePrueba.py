import pygame
import random
import sys
import turtle

pygame.init()

pantalla = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Pong Prueba")
ANCHO, ALTO = pantalla.get_size()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
NARANJA = (255,165,0)
AMARILLO = (255,255,0)
VERDE = (0,255,0)
fuente_titulo = pygame.font.Font(None, 100)
fuente_boton = pygame.font.Font(None, 60)
fuente_score = pygame.font.Font(None, 60)


# ============================
#     FUNCIÓN: MENÚ
# ============================
def menu():
    while True:
        pantalla.fill(NEGRO)

        # Texto PONG
        titulo = fuente_titulo.render("MENU", True, BLANCO)
        pantalla.blit(titulo, (280, 80))

        # Botón PONG
        boton1 = pygame.Rect(250, 250, 300, 90)
        pygame.draw.rect(pantalla, BLANCO, boton1, 3)
        texto1 = fuente_boton.render("JUGAR PONG", True, BLANCO)
        pantalla.blit(texto1, (265, 270))

        # Botón NUEVO JUEGO
        boton2 = pygame.Rect(250, 380, 300, 90)
        pygame.draw.rect(pantalla, BLANCO, boton2, 3)
        texto2 = fuente_boton.render("CUADRADO", True, BLANCO)
        pantalla.blit(texto2, (300, 400))
        # Boton Esquivar
        boton3 = pygame.Rect( 250, 510,300,90)
        pygame.draw.rect(pantalla, BLANCO, boton3, 3)
        texto3 = fuente_boton.render("ESQUIVAR", True, BLANCO)
        pantalla.blit(texto3, (335,530))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton1.collidepoint(event.pos):
                    return "pong"
                if boton2.collidepoint(event.pos):
                    return "cuadrado"
                if boton3.collidepoint(event.pos):
                    return "esquivar"

# ============================
#     FUNCIÓN: NUEVO JUEGO
# ============================
def juego_cuadrado():
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
# ============================
#     FUNCIÓN: JUEGO PONG
# ============================
def juego():
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
def juego_esquivar():########################################################3
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
                pantalla.blit(texto, (260, 250))
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
            pantalla.blit(texto, (260, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            return
        for i in range(0, 35, 5):
            for enemigo in enemigos:
                pygame.draw.rect(pantalla, color_enemigo, enemigo)
        pygame.display.update()


    return
# ============================
#   PROGRAMA PRINCIPAL
# ============================
opcion = menu()

if opcion == "pong":
    juego()
elif opcion == "cuadrado":
    juego_cuadrado()
elif opcion == "esquivar":
    juego_esquivar()
pygame.quit()
