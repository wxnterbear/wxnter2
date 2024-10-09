# importación de paquetes
import pygame,sys

# Inicialización de Pygame
pygame.init()

# Creación de la pantalla
ANCHO, ALTO = 735, 490
ventana = pygame.display.set_mode((ANCHO, ALTO))
#Configuración de tiempo de transición
FPS = 20
RELOJ = pygame.time.Clock()

# Especificación de título
pygame.display.set_caption('Animación')

# Especificar fondo de ventana.Convert adecua pixeles imagen-ventana
fondo = pygame.image.load("img/fondo_mov.gif").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
x = 0
y = 0

# Bucle de ejecución
while True:
	# Cerrar Juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

# Movimiento del fondo	
	x_relativa = x % fondo.get_rect().width
	ventana.blit(fondo, (x_relativa - fondo.get_rect().width,0))
	if x_relativa < ANCHO:
		ventana.blit(fondo, (x_relativa,0))
		x -= 1
       # Actualización de la ventana
	pygame.display.update()

	# Control de FPS- Llamado al metodo clock del objeto reloj
	RELOJ.tick(FPS)