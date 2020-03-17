import pygame

class Snake:
	def __init__(self):
		self.color = (0,150,0) #green
		self.snake_head = [250,250] 
		self.snake_starting_position = [[250,250],[240,250],[230,250]] 
		
		
	def display_snake(self, display):
		for position in self.snake_starting_position:
			pygame.draw.rect(display,self.color, pygame.Rect(position[0],position[1],10,10))

	def snake_move (self, direction):
		if direction == 1:
			self.snake_head[0] += 10
		elif direction == 0:
			self.snake_head[0] -= 10
		elif direction == 2:
			self.snake_head[1] += 10
		elif direction == 3:
			self.snake_head[1] -= 10
		else:
			pass
			
		self.snake_starting_position.insert(0,list(self.snake_head))
		self.snake_starting_position.pop()
