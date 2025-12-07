import pygame
import random
import sys

pygame.init()

pantalla = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Pong Prueba")
ANCHO, ALTO = pantalla.get_size()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
AMARILLO = (255,255,0)
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
    x = 0
    y = 0
    tam = 30
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
        if y > 600 - tam: y = 600 - tam
        if x < 0: x = 0
        if x > 800 - tam: x = 800 - tam

        # Rectángulos del juego
        rect_azul  = pygame.Rect(x, y, tam, tam)
        rect_rojo  = pygame.Rect(rojo_x, rojo_y, tam, tam)

        rect_blanco2 = pygame.Rect(tam, 0, 20, 200)
        rect_blanco3 = pygame.Rect(tam, 210 + tam, 20, 200)
        rect_blanco4 = pygame.Rect(tam, 420 + tam*2, 20, 100 - tam + 12)
        rect_blanco5 = pygame.Rect(tam*3, 0+tam, 20, 100)
        # Lista de paredes (IMPORTANTE)
        paredes = [rect_blanco2, rect_blanco3, rect_blanco4, rect_blanco5]

        # --- COLISIÓN CON PAREDES ---
        for p in paredes:
            if rect_azul.colliderect(p):
                x, y = old_x, old_y   # volver atrás
                rect_azul.x = x
                rect_azul.y = y

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
        pygame.draw.rect(pantalla, BLANCO, rect_blanco2)
        pygame.draw.rect(pantalla, BLANCO, rect_blanco3)
        pygame.draw.rect(pantalla, BLANCO, rect_blanco4)
        pygame.draw.rect(pantalla, BLANCO, rect_blanco5)
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
def juego_esquivar():########################################################3
    xnave = ANCHO / 2
    ynave = ALTO - 80
    x_speed = 1
    ladoNave = 50
    score = 0
    enemy_size = 50
    random.randint(0, ANCHO - enemy_size)
    enemy_pos = [random.randint(0, ANCHO - enemy_size), 0]
    enemy_list = [enemy_pos]
    enemy_speed = 10
    clock = pygame.time.Clock()
    disparo_ancho = 10
    disparo_alto = 25
    disparo_x = xnave+ladoNave/2
    disparo_y = ynave+ladoNave/2
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
        if mov_nave[pygame.K_k]:
            disapro = True
        if disapro:
            disparo_y -= disparo_vel_y

        if disparo_y < 0:       # si sale de la pantalla se desactiva
            disapro = False



        # límites
        if xnave < 0:
            xnave = 0
        if xnave > ANCHO - ladoNave:
            xnave = ANCHO - ladoNave
        if disparo_x < ladoNave/2:
            disparo_x = ladoNave/2
        if disparo_x > ANCHO-ladoNave/2:
            disparo_x = ANCHO-ladoNave/2
        # --- DIBUJAR ---
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, BLANCO, (xnave, ynave, ladoNave, ladoNave))
        pygame.draw.rect(pantalla, AMARILLO, (disparo_x, disparo_y, disparo_ancho, disparo_alto))
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
