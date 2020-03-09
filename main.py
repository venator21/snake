import pygame
# ~ import random

pygame.init()

clock = pygame.time.Clock()
clock.tick(20)


display_width = 500 
display_height = 500    
display = pygame.display.set_mode((display_width,display_height))
window_color= (200, 200, 200)
display.fill(window_color)    
pygame.display.update()

red = (255,0,0)  
black = (0,0,0)
# ~ apple_image = pygame.image.load('apple.jpg') 
snake_head = [250,250] 
snake_position = [[250,250],[240,250],[230,250]] 
# ~ apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
 
def display_snake(snake_position):
    for position in snake_position:
        pygame.draw.rect(display,red,pygame.Rect(position[0],position[1],10,10))
 
def display_apple(display,apple_position, apple):
    display.blit(apple,(apple_position[0], apple_position[1]))
    

display_snake(snake_position)
pygame.display.update()
