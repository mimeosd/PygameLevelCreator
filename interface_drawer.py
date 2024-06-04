import pygame
from file_get_helper import find_png_images
import constants

def side_panel(surface: pygame.Surface, color: tuple):
    main_holder = pygame.draw.rect(surface, (215, 0, 0), (constants.WIDTH - 350, 10, 330, constants.HEIGTH - 30), 5) 
    # height is 780 each block is 30x30px
    
    # load images
    all_cells = []
    
    for row in range(15):
        for cell in range(6):
            cell = pygame.draw.rect(surface, (215, 0, 0), (850 + cell * 55, row * 55 + 10, 55, 55), 5)
            all_cells.append([cell.topleft[0], cell.topleft[1], 55, 55])

    all_images = find_png_images()
    for _index, _image in enumerate(all_images):
        img = pygame.image.load(_image)
        img_rect = img.get_rect()
        print(img_rect.width)
        img_rect.topleft = (all_cells[_index][0], all_cells[_index][1])
        surface.blit(img, img_rect)
