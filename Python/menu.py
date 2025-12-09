import pygame

ANCHO = 900
ALTO = 700

NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
NARANJA = (255,165,0)
AMARILLO = (255,255,0)
VERDE = (0,255,0)

pygame.font.init()
FUENTE_TITULO = pygame.font.Font(None, 100)
FUENTE_BOTON = pygame.font.Font(None, 60)
FUENTE_SCORE = pygame.font.Font(None, 60)


# ============================
#        FUNCIÓN MENU
# ============================
def menu(pantalla):
    while True:
        pantalla.fill(NEGRO)

        # Título
        titulo = FUENTE_TITULO.render("MENU", True, BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - 150, 80))

        # Botón Pong
        boton1 = pygame.Rect(250, 250, 300, 90)
        pygame.draw.rect(pantalla, BLANCO, boton1, 3)
        texto1 = FUENTE_BOTON.render("JUGAR PONG", True, BLANCO)
        pantalla.blit(texto1, (300, 270))

        # Botón Cuadrado
        boton2 = pygame.Rect(250, 380, 300, 90)
        pygame.draw.rect(pantalla, BLANCO, boton2, 3)
        texto2 = FUENTE_BOTON.render("CUADRADO", True, BLANCO)
        pantalla.blit(texto2, (310, 400))

        #Boton Esquivar
        boton3 = pygame.Rect(250, 510, 300, 90)
        pygame.draw.rect(pantalla,BLANCO,boton3,3)
        texto3 = FUENTE_BOTON.render("NAVE",True,BLANCO)
        pantalla.blit(texto3, (320,530))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton1.collidepoint(event.pos):
                    return "pong"
                if boton2.collidepoint(event.pos):
                    return "cuadrado"
                if boton3.collidepoint(event.pos):
                    return "nave"