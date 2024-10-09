import pygame
from pygame.locals import* #importa todas las librerías del módulo pygame
import sys


morado = (175,122,197)

icono = pygame.image.load("img/icono.ico")

ventana = pygame.display.set_mode((500, 400)) #ancho.alto -- Tupla - coordenadad (x,y)
pygame.display.set_caption("Para el amor de mi vida")
ventana.fill(morado)

pygame.display.set_icon(icono)

#especificar fono de ventana
fondo = pygame.image.load("img/panda.jfif").convert()
x = 130
y = 80

run = True
while run: #la ventana itera continuamente hasta que se cierre
    for evento in pygame.event.get():
        if evento.type ==  QUIT: #Si el evento es igual a salida
            pygame.quit() #cierra el módulo pygame
            sys.exit() #salir del programa o sistema
            
    ventana.blit(fondo, (x,y)) # dibujar la imágen

    pygame.display.update() #Actualiza la ejecucuón ventana