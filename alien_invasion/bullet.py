import pygame
from pygame import Sprite

class Bullet(Sprite):
	def __init__(self,screen,ai_settings):
		super().__init__()
		self.screen = screen
		#Crear un Rect en (0,0) para la bala y luego colocarlo en
		#la parte de arriba de la nave
		self.rect = pygame.Rect(0,0,ai_settings.
	
