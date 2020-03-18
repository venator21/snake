import pygame

class Snake:
	def __init__(self):
		self.color = (0,150,0) #green
		self.snake_head = [250,250] 
		self.snake_position = [[250,250],[240,250],[230,250]] 
		
		
	def display_snake(self, display):
		for position in self.snake_position:
			pygame.draw.rect(display,self.color, pygame.Rect(position[0],position[1],10,10))

	def snake_move(self, direction):
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
			
		self.snake_position.insert(0,list(self.snake_head))
		self.snake_position.pop()

	def collision_with_self(self):
			if self.snake_head in self.snake_position[1:]:
				return True
			else:
				return False

	def collision_with_apple(self, apple):
		if self.snake_head == apple.apple_position:
			return True
	
	def extend_snake(self):
		self.snake_position.insert(0,list(self.snake_head))
