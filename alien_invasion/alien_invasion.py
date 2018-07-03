import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
	
	#inicializa el juego y crea un objeto pantalla (display)
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("New_Order")
	
	#crea una nave
	ship = Ship(ai_settings,screen)
	
	#Loop principal del juego
	while True:

		#chequea eventos nuevos
		gf.check_events(ship)
		#refresca la nave
		ship.update()
		#refresca la pantalla
		gf.update_screen(ai_settings,screen,ship)

run_game()	
