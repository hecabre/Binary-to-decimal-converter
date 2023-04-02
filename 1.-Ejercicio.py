import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
window_size = (800, 600)

# Crear la ventana
screen = pygame.display.set_mode(window_size)

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dibujar un círculo
circle_pos = (400, 300)
circle_radius = 50
pygame.draw.circle(screen, WHITE, circle_pos, circle_radius)

# Actualizar la pantalla
pygame.display.flip()

# Esperar a que se cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.K_w:
            print('hola')