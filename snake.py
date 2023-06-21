import pygame

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the snake
snake_block_size = 10
snake_speed = 15
x1 = 400
y1 = 300
x1_change = 0
y1_change = 0
