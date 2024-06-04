import pygame
import constants
from interface_drawer import side_panel


pygame.init()

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGTH)) # TODO add full screen support
pygame.display.set_caption("Level creator")


clock = pygame.time.Clock()

running = True
while running:
    pressed = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    side_panel(screen, (0, 0, 0))
    
    pygame.display.update()
    clock.tick(60)


