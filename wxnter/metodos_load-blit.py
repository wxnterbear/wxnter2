import pygame,sys
from pygame.locals import *
from random import randint
pygame.init()

ancho, alto = 800,516

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Imagen")

# Carga la imagen de fondo
fondo = pygame.image.load('img/fondo_mov.gif')
# Dibuja la imagen de fondo
ventana.blit(fondo,(0,0)) #blit -> a partir de donde va a rellenar

#Ajusta el tamaño de la imagen al tamaño de la ventana (si es necesario)
#fondo = pygame.transform.scale(fondo, (ancho, alto))

# Carga la imagen del objeto
perrito = pygame.image.load("img/perrito.png")
perrito = pygame.transform.scale(perrito, (200, 230)) #alto y ancho
# Declarar e inicializar los valores de posición en X, Y
posX, posY = 200, 20
# Dibuja la imagen del objeto
#posX, posY = randint(10,300), randint(10,200)
ventana.blit(perrito, (posX, posY))


while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()