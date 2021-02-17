import pygame
import random
import sys
 


pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

shape_position = (width / 2, height / 2)
shape_size = (100, 100)

shape_rect = pygame.Rect(shape_position, shape_size)

#Colors
shape_color = (142, 58, 60)
line_color = (51, 116, 48)
circle_color = (143, 122, 59)

#Coin Color

coin_color = (233, 131, 229)
line_color = (51, 116, 48)
circle_color = (143, 122, 59)
 

coin_collission = pygame.rect(coin_pos[0] - coin_radius, coin_pos[1] - coin_radius, coin_radius * 2, coin_radius * 2 )

coin_collected = False

circle_pos = (50,50)
circle_radius = 25

#Start Colliossion Box

player_collission = pygame.rect(circle_pos[0] - circle_radius, circle_pos[1] - circle_radius, circle_radius * 2, circle_radius * 2)