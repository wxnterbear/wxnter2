import pygame
from pygame.locals import* #importa todas las librerías del módulo pygame
import sys

#Definición de colores
azul = (214, 234, 248)
rosa = (245, 187, 234)
blanco = (255, 255, 255)
morado = (175,122,197)
verde = (30, 132, 73)
skin = (233, 150, 122)
window = ()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Juego increíble")
screen.fill(verde)

#Zona de dibujo persona
pygame.draw.circle(screen, skin, (200,270), 17) # 1 y 2 (X y Y), 3 (tamaño del circulo)
pygame.draw.rect(screen, skin, [(195.8, 286), (10,10)])
pygame.draw.polygon(screen, azul, [(180, 310), (190, 290), (210, 290), (220, 310)]) #mas de una omg
pygame.draw.rect(screen, azul, [(190, 310), (21, 15)])
pygame.draw.rect(screen, rosa, [(190, 325), (21, 5)])
pygame.draw.rect(screen, rosa, [(190, 330), (9, 20)])
pygame.draw.rect(screen, rosa, [(202, 330), (9, 20)])
pygame.draw.polygon(screen, blanco, [(100, 12), (77, 50), (35, 50), (65, 70), (40, 110), (100, 80), (160, 110), (135, 70), (165, 50), (123, 50)]) #mas de una omg

run = True
while run: #la ventana itera continuamente hasta que se cierre
    for evento in pygame.event.get():
        if evento.type ==  QUIT: #Si el evento es igual a salida
            pygame.quit() #cierra el módulo pygame
            sys.exit() #salir del programa o sistema

    pygame.display.update() #Actualiza la ejecucuón ventana