# paquetes
import pygame
import sys

# inicialización pygame
pygame.init()

# pantalla
ANCHO, ALTO = 800, 590
ventana = pygame.display.set_mode((ANCHO, ALTO))
FPS = 20
RELOJ = pygame.time.Clock()

# título
pygame.display.set_caption('Perritos wuiwui')

# fondo 
fondo = pygame.image.load("img/fondo_mov.gif").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# perrito
perrito = pygame.image.load("img/perrito.png").convert_alpha()
perrito = pygame.transform.scale(perrito,(290, 300))
perrito_rect = perrito.get_rect()  # dimensiones del perrito

# Posiciones iniciales de los perritos
x_perrito1 = 0
y_perrito1 = 0

x_perrito2 = ANCHO - perrito_rect.width
y_perrito2 = 0

x_perrito3 = ANCHO - perrito_rect.width
y_perrito3 = ALTO - perrito_rect.height

x_perrito4 = 0
y_perrito4 = ALTO - perrito_rect.height

# velocidad perrito
velocidad_perrito = 5

# bucle de ejecución
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # perrito 1
    x_perrito1 += velocidad_perrito  # movimiento izq -> der
    if x_perrito1 > ANCHO:
        x_perrito1 = -perrito_rect.width  # para reaparecer

    # perrito 2
    y_perrito2 += velocidad_perrito  # movimiento arr -> aba
    if y_perrito2 > ALTO:
        y_perrito2 = -perrito_rect.height

    # perrito 3
    x_perrito3 -= velocidad_perrito  # movimiento der -> izq
    if x_perrito3 < -perrito_rect.width:
        x_perrito3 = ANCHO

    # perrito 4 
    y_perrito4 -= velocidad_perrito  # movimiento aba -> arr
    if y_perrito4 < -perrito_rect.height:
        y_perrito4 = ALTO

    # llenar fondo
    ventana.blit(fondo, (0, 0))

    # perritos en las posiciones finales
    ventana.blit(perrito, (x_perrito1, y_perrito1))  # perrito 1
    ventana.blit(perrito, (x_perrito2, y_perrito2))  # perrito 2
    ventana.blit(perrito, (x_perrito3, y_perrito3))  # perrito 3
    ventana.blit(perrito, (x_perrito4, y_perrito4))  # perrito 4

    # actualiza la ejecución de la ventana
    pygame.display.update()

    # control de FPS- Llamado al metodo clock del objeto reloj
    RELOJ.tick(FPS)
