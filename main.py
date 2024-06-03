import pygame
import constants
from interface_drawer import PictureDrawer


pygame.init()

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGTH)) # TODO add full screen support
pygame.display.set_caption("Level creator")


clock = pygame.time.Clock()

pd = PictureDrawer(screen)
pd_group = pygame.sprite.Group()
pd_group.add(pd)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for p in pd_group:
        p.update()
        p.draw(screen)


    
    pygame.display.update()
    clock.tick(60)