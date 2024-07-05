import pygame
from file_get_helper import find_png_images
import constants

def side_panel(surface: pygame.Surface, color: tuple, offset=0): # remove color parameter and make sure to clear it in main call
    main_holder = pygame.draw.rect(surface, (215, 0, 0), (constants.WIDTH - 350, 10, 330, constants.HEIGTH - 30), 5)
    
    all_cells = []
    all_images = find_png_images()
    
    for row in range(15):
        for cell in range(6):
            cell_rect = pygame.draw.rect(surface, (215, 0, 0), (850 + cell * 55, row * 55 + 10 + offset, 55, 55))
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

def level_size_value(surface: pygame.Surface, level_size_x: str, level_size_y: str):
    font = pygame.font.Font(None, 22)
    text_x = "Level size X: "
    text_y = "Level size Y: "
    font_surf_x = font.render(text_x, True, (255, 255, 255))
    font_surf_y = font.render(text_y, True, (255, 255, 255))
    font_rect_x = font_surf_x.get_rect()
    font_rect_y = font_surf_y.get_rect()
    
    font_rect_x.topleft = (80, 750)
    font_rect_y.topleft = (290, 750)
    
    # Drawing input boxes
    input_box_x = pygame.Rect(font_rect_x.right + 10, font_rect_x.y, 100, 32)
    input_box_y = pygame.Rect(font_rect_y.right + 10, font_rect_y.y, 100, 32)
    pygame.draw.rect(surface, (255, 255, 255), input_box_x, 2)
    pygame.draw.rect(surface, (255, 255, 255), input_box_y, 2)
    
    # Render the level sizes inside the input boxes
    level_size_surf_x = font.render(level_size_x, True, (255, 255, 255))
    level_size_surf_y = font.render(level_size_y, True, (255, 255, 255))
    level_size_rect_x = level_size_surf_x.get_rect()
    level_size_rect_y = level_size_surf_y.get_rect()
    level_size_rect_x.topleft = (input_box_x.x + 5, input_box_x.y + 5)
    level_size_rect_y.topleft = (input_box_y.x + 5, input_box_y.y + 5)
    surface.blit(level_size_surf_x, level_size_rect_x)
    surface.blit(level_size_surf_y, level_size_rect_y)
    
    surface.blit(font_surf_x, font_rect_x)
    surface.blit(font_surf_y, font_rect_y)
    
    return input_box_x, input_box_y


def draw_level_area(surface: pygame.Surface, rows: int, columns: int, cell_images=None):
    all_cells = []
    size = 30
    starting_value = (20, 20)
    if cell_images is None:
        cell_images = {}

    for r in range(rows):
        for c in range(columns):
            cell_rect = pygame.Rect(starting_value[0] + c * size + 5, starting_value[1] + r * size + 5, 30, 30)
            cell_pos = (r, c)
            if cell_pos in cell_images and cell_images[cell_pos]:
                image = pygame.image.load(cell_images[cell_pos])
                image = pygame.transform.scale(image, (30, 30))
                surface.blit(image, cell_rect.topleft)
            else:
                pygame.draw.rect(surface, (255, 255, 255), cell_rect, 3)
            all_cells.append(cell_rect)

    return all_cells

