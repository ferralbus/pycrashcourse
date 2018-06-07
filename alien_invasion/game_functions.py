import sys
import pygame

def check_keydown_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ship):
	#mira eventos de teclado o raton en la pantalla
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
def update_screen(ai_settings,screen,ship):
	#vuelve a dibujar el color de fondo
	screen.fill(ai_settings.bg_color)
	ship.blitme()		
	#refresca la pantalla
	pygame.display.flip()
