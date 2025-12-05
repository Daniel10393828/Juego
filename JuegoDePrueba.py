import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Prueba")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
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


# ============================
#     FUNCIÓN: NUEVO JUEGO
# ============================
def juego_cuadrado():
    x = 400
    y = 300
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

        # Movimiento básico
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_s]: y += vel_y
        if teclas[pygame.K_w]: y -= vel_y
        if teclas[pygame.K_a]: x -= vel_x
        if teclas[pygame.K_d]: x += vel_x

        # Límites
        if y < 0: y = 0
        if y > 600 - tam: y = 600 - tam
        if x < 0: x = 0
        if x > 800 - tam: x = 800 - tam

        rect_blanco = pygame.Rect(x, y, tam, tam)
        rect_rojo  = pygame.Rect(rojo_x, rojo_y, tam, tam)

        # --- COLISIÓN ---
        if rect_blanco.colliderect(rect_rojo):
            pantalla.fill(NEGRO)
            texto = fuente_score.render("GANASTE", True, BLANCO)
            pantalla.blit(texto, (260, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            return  # vuelve al menú

        # Dibujar
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, BLANCO, rect_blanco)
        pygame.draw.rect(pantalla, ROJO, rect_rojo)

        pygame.display.update()

# ============================
#     FUNCIÓN: JUEGO PONG
# ============================
def juego():
    ancho = 25
    largo = 100

    x = 0
    y = (600 - largo) / 2

    x2 = 800 - ancho
    y2 = (600 - largo) / 2

    velocidad = 1

    ball_x = 400
    ball_y = 300
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

        teclas = pygame.key.get_pressed()

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
        if y > 600 - largo: y = 600 - largo

        if y2 < 0: y2 = 0
        if y2 > 600 - largo: y2 = 600 - largo

        # Movimiento de pelota
        ball_x += ball_vel_x
        ball_y += ball_vel_y

        # Rebote arriba / abajo
        if ball_y < 0 or ball_y > 600 - ball_size:
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

        if ball_x > 800 - ball_size:
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
        pantalla.blit(texto, (350, 20))

        pygame.display.update()


# ============================
#   PROGRAMA PRINCIPAL
# ============================
opcion = menu()

if opcion == "pong":
    juego()
elif opcion == "cuadrado":
    juego_cuadrado()

pygame.quit()