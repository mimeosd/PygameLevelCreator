import pygame
from file_get_helper import find_png_images
import constants

def side_panel(surface: pygame.Surface, color: tuple, offset=0):
    main_holder = pygame.draw.rect(surface, (215, 0, 0), (constants.WIDTH - 350, 10, 330, constants.HEIGTH - 30), 5)
    
    all_cells = []
    all_images = find_png_images()
    
    for row in range(15):
        for cell in range(6):
            cell_rect = pygame.draw.rect(surface, (215, 0, 0), (850 + cell * 55, row * 55 + 10 + offset, 55, 55), 5)
            all_cells.append(cell_rect)

    for _index, _image in enumerate(all_images):
        img = pygame.image.load(_image)
        if img.get_width() < 33 or img.get_width() > 70:  # slightly bigger than square
            img = pygame.transform.scale(img, (55, 55))
        
        img_rect = img.get_rect()
        img_rect.topleft = all_cells[_index].topleft
        surface.blit(img, img_rect)
        all_cells[_index] = (img_rect, _image)  # Store the image rect and its name

    return all_cells

def check_click(mouse_pos, offset):
    all_cells = side_panel(pygame.Surface((constants.WIDTH, constants.HEIGTH)), (0, 0, 0), offset)
    for img_rect, img_name in all_cells:
        if img_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            return img_name
    return None

def selected_image(surface: pygame.Surface, img_path=None):
    img_rect_border = pygame.draw.rect(surface, (215, 0, 0), (15, 740, 55, 55), 5)  # draws reddish square around
    if img_path is not None:
        image = pygame.image.load(img_path)
        image = pygame.transform.scale(image, (55, 55))  # Scale the image to fit within the border
        img_rect = image.get_rect()
        img_rect.center = img_rect_border.center  # Center the image within the border
        surface.blit(image, img_rect)
