import pygame


class App:
	display_width = 500 
	display_height = 500   
	window_color= (200, 200, 200)
	clock = pygame.time.Clock()
	
	def __init__(self):
		pygame.init()
		self.prev_direction = 1
		self.direction = 1
		self.final_score = 0
		self.display = pygame.display.set_mode((self.display_width,self.display_height))


	def key_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # Check if user hit the red x
				pygame.quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and self.prev_direction != 1:
					self.direction = 0
				elif event.key == pygame.K_RIGHT and self.prev_direction != 0:
					self.direction = 1
				elif event.key == pygame.K_UP and self.prev_direction != 2:
					self.direction = 3
				elif event.key == pygame.K_DOWN and self.prev_direction != 3:
					self.direction = 2
				else:
					self.direction = self.direction
					
				self.prev_direction = self.direction
					
					
	def draw_display (self, snake, apple):
		self.display.fill(self.window_color) 
		snake.display_snake(self.display)
		apple.display_apple(self.display)
		pygame.display.update()
			
			
	def display_score(self):
		largeText = pygame.font.Font('freesansbold.ttf',35)
		TextSurf = largeText.render('Your Score is: ' + str(self.final_score), True, (0, 0, 0))
		TextRect = TextSurf.get_rect()
		TextRect.center = ((self.display_width/2),(self.display_height/2))
		self.display.blit(TextSurf, TextRect)
		pygame.display.update()
		time.sleep(2)
		
		
	def play(self, snake, apple):
		while 1:
			self.clock.tick(20)
			self.key_event()
			if snake.collision_with_boundaries():
				break
			if snake.collision_with_self():
				break
			if snake.collision_with_apple(apple):
				snake.extend_snake()
				apple.generate_new_position()
				self.final_score += 1
			snake.snake_move(self.direction)		
			self.display.fill(self.window_color)   
			self.draw_display(snake, apple)
		self.display_score()
		pygame.quit()


			

