import pygame

class Apple:
	green = (0,100,0)
	apple_position = [300,300] 
	
	
	def __init__(self):
		self.green = (0,255,0)
		self.apple_position = [300,300] 		
			
	def display_apple(self, display):
		pygame.draw.rect(display,self.green,pygame.Rect(self.apple_position[0],self.apple_position[1],10,10))
				
