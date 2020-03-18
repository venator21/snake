import pygame
import random

class Apple:
	
	def __init__(self):
		self.color = (255,0,0) #red
		self.apple_position = [random.randrange(1,50)*10, random.randrange(1,50)*10] 		
			
	def display_apple(self, display):
		pygame.draw.rect(display,self.color,pygame.Rect(self.apple_position[0],self.apple_position[1],10,10))
		
	def generate_new_position(self):
		""" Function doc """
		self.apple_position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
				
