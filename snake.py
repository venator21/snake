import pygame

class Snake:
	def __init__(self):
		self.red = (255,0,0)
		self.snake_head = [250,250] 
		self.snake_starting_position = [[250,250],[240,250],[230,250]] 
		
		
	def display_snake(self, display):
		for position in self.snake_starting_position:
			pygame.draw.rect(display,self.red, pygame.Rect(position[0],position[1],10,10))

	def snake_move (self, button_direction):
		""" Function doc """
		if button_direction == 1:
			self.snake_head[0] += 10
		elif button_direction == 0:
			self.snake_head[0] -= 10
		elif button_direction == 2:
			self.snake_head[1] += 10
		elif button_direction == 3:
			self.snake_head[1] -= 10
		else:
			pass
