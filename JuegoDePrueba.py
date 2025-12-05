import pygame

# Inicializar
pygame.init()

# Crear ventana negra de 800x600
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pantalla Negra")

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.fill((0, 0, 0))  # Negro
    pygame.display.update()

pygame.quit()