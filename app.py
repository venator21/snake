import pygame

class App:
	display_width = 500 
	display_height = 500   
	window_color= (200, 200, 200)
	clock = pygame.time.Clock()
	
	def __init__(self):
		pygame.init()
		self.prev_button_direction = 1
		self.button_direction = 1
		self.display = pygame.display.set_mode((self.display_width,self.display_height))
		
	def play(self, snake, apple):
		while 1:
			self.clock.tick(20)
			if snake.snake_head[0]<500:
				pass
			else:
				snake.snake_head[0] = 0
			if snake.snake_head[1]<500:
				pass
			else:
				snake.snake_head[1] = 0
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and self.prev_button_direction != 1:
						self.button_direction = 0
					elif event.key == pygame.K_RIGHT and self.prev_button_direction != 0:
						self.button_direction = 1
					elif event.key == pygame.K_UP and self.prev_button_direction != 2:
						self.button_direction = 3
					elif event.key == pygame.K_DOWN and self.prev_button_direction != 3:
						self.button_direction = 2
					else:
						self.button_direction = self.button_direction
			self.prev_button_direction = self.button_direction
			snake.snake_move(self.button_direction)		
			# ~ snake.snake_head[0] += 10
			snake.snake_starting_position.insert(0,list(snake.snake_head))
			snake.snake_starting_position.pop()
			self.display.fill(self.window_color)   
			snake.display_snake(self.display)
			apple.display_apple(self.display)
			pygame.display.update()
			
		

