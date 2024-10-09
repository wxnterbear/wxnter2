import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola Mundo")

perrito = pygame.image.load("img/perrito.png")
perrito = pygame.transform.scale(perrito, (100, 200))
posX, posY = randint(10,300), randint(10,200)
ventana.blit(perrito, (posX, posY))


while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()