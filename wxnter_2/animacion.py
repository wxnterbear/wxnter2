import pygame,sys

# Iniciación de Pygame
pygame.init()

# Pantalla - ventana
W, H = 860, 484
AN, AL = 200, 200
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Animación Personaje')
icono=pygame.image.load('img/icon/icon.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('img/fondo/fondo.jpg').convert()
fondo = pygame.transform.scale(fondo, (W, H))

# Carga de imagen para personaje posición quieto
quieto = pygame.image.load('img/personaje/img/Idle/0_Golem_Idle_000.png')
quieto = pygame.transform.scale(quieto, (AN, AL))

# Carga de imágenes para personaje caminar a la derecha	
caminaDerecha = [pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_000.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_001.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_002.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_003.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_004.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_005.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_006.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_007.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_008.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_009.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_010.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_011.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_012.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_013.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_014.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_015.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_016.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_017.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_018.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_019.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_020.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_021.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_022.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_R/0_Golem_Walking_023.png'), (AN, AL))
				]

# Carga de imágenes para personaje caminar a la izquierda
caminaIzquierda = [pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_000.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_001.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_002.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_003.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_004.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_005.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_006.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_007.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_008.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_009.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_010.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_011.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_012.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_013.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_014.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_015.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_016.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_017.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_018.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_019.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_020.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_021.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_022.png'), (AN, AL)),
				pygame.transform.scale(pygame.image.load('img/personaje/img/Walking_L/0_Golem_Walking_023.png'), (AN, AL))
				]

# Carga de imágenes para personaje saltar	
salta = [pygame.transform.scale(pygame.image.load('img/personaje/img/Jump/0_Golem_Jump Start_000.png'), (AN, AL)),
		 pygame.transform.scale(pygame.image.load('img/personaje/img/Jump/0_Golem_Jump Start_001.png'), (AN, AL)),
		 pygame.transform.scale(pygame.image.load('img/personaje/img/Jump/0_Golem_Jump Start_002.png'), (AN, AL)),
		 pygame.transform.scale(pygame.image.load('img/personaje/img/Jump/0_Golem_Jump Start_003.png'), (AN, AL)),
		 pygame.transform.scale(pygame.image.load('img/personaje/img/Jump/0_Golem_Jump Start_004.png'), (AN, AL)),
		 pygame.transform.scale(pygame.image.load('img/personaje/img/Jump/0_Golem_Jump Start_005.png'), (AN, AL)),
		]

# Variables de posición y movimiento del personaje
x = 0
px = 50
py = 290
ancho = 40
velocidad = 5

# Control de FPS -> cambio del tiempo en los fotogramas
reloj = pygame.time.Clock()

# Variable para salto inicializar
salto = False
# Contador de salto inicializar
cuentaSalto = 10 #Controlar la altura y la duración del salto del personaje

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Movimiento
def recarga_pantalla():
	# Variables globales
	global cuentaPasos
	global x

	# Fondo en movimiento
	x_relativa = x % fondo.get_rect().width
	PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < W:
		PANTALLA.blit(fondo, (x_relativa, 0))
	x -= 5

	# Contador de pasos y actualización de animaciones según dirección
	if cuentaPasos + 1 >= 8:
		cuentaPasos = 0

	# Si Movimiento a la izquierda muestra animaciones
	if izquierda:
		PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

		# Si Movimiento a la derecha, muestra animaciones
	elif derecha:
		PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	elif salto + 1 >= 8:
		PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	else:
		PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

# Bucle de acciones y controles
while ejecuta:
	# FPS
	reloj.tick(18)

	# Bucle del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecuta = False

	# Opción tecla pulsada
	keys = pygame.key.get_pressed()

	# Tecla A - Movimiento a la izquierda
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad
		izquierda = True
		derecha = False

	# Tecla D - Movimiento a la derecha
	elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
		px += velocidad
		izquierda = False
		derecha = True

	# Personaje quieto
	else:
		izquierda = False
		derecha = False
		cuentaPasos = 0

	# Tecla W - Movimiento hacia arriba
	if keys[pygame.K_w] and py > 100:
		py -= velocidad

	# Tecla S - Moviemiento hacia abajo
	if keys[pygame.K_s] and py < 300:
		py += velocidad

	# Tecla SPACE - Salto
	if not salto:
		if keys[pygame.K_SPACE]:
			salto = True
			izquierda = False
			derecha = False
			cuentaPasos = 0
	else:
		if cuentaSalto >= -10:
			py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
			cuentaSalto -= 1
		else:
			cuentaSalto = 10
			salto = False

	# Actualización de la ventana
	pygame.display.update()
	#Llamada a la función de actualización de la ventana
	recarga_pantalla()

# Salida del juego
pygame.quit()
