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
pygame.display.set_caption('Objetos wuiwui')

# fondo 
fondo = pygame.image.load("img/fondo_mov.gif").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# perrito
perrito = pygame.image.load("img/perrito2.png").convert_alpha()
perrito = pygame.transform.scale(perrito,(290, 300))
perrito_rect = perrito.get_rect()  # dimensiones 

# perrito 2
perrito2 = pygame.image.load("img/perrito.png").convert_alpha()
perrito2 = pygame.transform.scale(perrito2,(290, 300))
perrito2_rect = perrito2.get_rect()  # dimensiones 

# mariposa
mariposa = pygame.image.load("img/perrito3.png").convert_alpha()
mariposa = pygame.transform.scale(mariposa,(290, 300))
mariposa_rect = mariposa.get_rect()  # dimensiones 

# pajaro
pajaro = pygame.image.load("img/pajaro.png").convert_alpha()
pajaro = pygame.transform.scale(pajaro,(290, 300))
pajaro_rect = pajaro.get_rect()  # dimensiones 

# Posiciones iniciales de los objetos
x_perrito2 = 0
y_perrito2 = 0 # esquina superior izquierda

x_mariposa = ANCHO - mariposa_rect.width
y_mariposa = 0 # esquina superior derecha

x_perrito = ANCHO - perrito_rect.width
y_perrito = ALTO - perrito_rect.height  # esquina inferior derecha

x_pajaro = 0
y_pajaro = ALTO - pajaro_rect.height  # esquina inferior izquierda

# velocidad objetos
velocidad_objeto = 5

# bucle de ejecución
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la mariposa (arriba -> abajo)
    y_mariposa += velocidad_objeto
    if y_mariposa > ALTO:
        y_mariposa = -mariposa_rect.height  # reaparecer en la parte superior

    # Movimiento del perrito2 (izquierda -> derecha)
    x_perrito2 += velocidad_objeto
    if x_perrito2 > ANCHO:
        x_perrito2 = -perrito2_rect.width  # reaparecer a la izquierda

    # Movimiento del pájaro (abajo -> arriba)
    y_pajaro -= velocidad_objeto
    if y_pajaro < -pajaro_rect.height:
        y_pajaro = ALTO  # reaparecer en la parte inferior

    # Movimiento del perrito (derecha -> izquierda)
    x_perrito -= velocidad_objeto
    if x_perrito < -perrito_rect.width:
        x_perrito = ANCHO  # reaparecer en la parte derecha

    # llenar fondo
    ventana.blit(fondo, (0, 0))

    # dibujar los objetos en pantalla
    ventana.blit(mariposa, (x_mariposa, y_mariposa))  # mariposa desde la esquina superior izquierda
    ventana.blit(perrito2, (x_perrito2, y_perrito2))  # perrito2 desde la esquina superior derecha
    ventana.blit(pajaro, (x_pajaro, y_pajaro))  # pájaro desde la esquina inferior derecha
    ventana.blit(perrito, (x_perrito, y_perrito))  # perrito desde la esquina inferior izquierda

    # actualiza la ejecución de la ventana
    pygame.display.update()

    # control de FPS
    RELOJ.tick(FPS)
