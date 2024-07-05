import pygame
import constants
from interface_drawer import side_panel, check_click, selected_image, level_size_value, draw_level_area

pygame.init()

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGTH))  # TODO add full screen support
pygame.display.set_caption("Level creator")

clock = pygame.time.Clock()

scroll_offset = 0
scroll_speed = 5
clicked_img = None
level_size_x = "10"  # Starting exemplary level size value for x
level_size_y = "10"  # Starting exemplary level size value for y
input_active_x = False
input_active_y = False
cell_images = {}

running = True
while running:
    pressed_mouse = pygame.mouse.get_pressed()
    pressed_key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if event.button == 1:  # Left mouse button click
                clicked_image = check_click(mouse_pos, scroll_offset)
                if clicked_image:
                    clicked_img = clicked_image

                if input_box_x.collidepoint(mouse_pos):
                    input_active_x = True
                    input_active_y = False
                elif input_box_y.collidepoint(mouse_pos):
                    input_active_y = True
                    input_active_x = False
                else:
                    input_active_x = False
                    input_active_y = False

                for r, level_grid_cell in enumerate(level_grid):
                    if level_grid_cell.collidepoint(mouse_pos):
                        cell_pos = (r // level_size_y_int, r % level_size_y_int)
                        if clicked_img:
                            cell_images[cell_pos] = clicked_img
                        else:
                            cell_images.pop(cell_pos, None)  # Remove image if clicked_img is None

            elif event.button == 3:  # Right mouse button click
                for r, level_grid_cell in enumerate(level_grid):
                    if level_grid_cell.collidepoint(mouse_pos):
                        cell_pos = (r // level_size_y_int, r % level_size_y_int)
                        cell_images.pop(cell_pos, None)  # Remove the image from the clicked cell
                clicked_img = None

        # this part handles input of level grid size row x col
        elif event.type == pygame.KEYDOWN:
            if input_active_x:
                if event.key == pygame.K_RETURN:
                    input_active_x = False
                elif event.key == pygame.K_BACKSPACE:
                    level_size_x = level_size_x[:-1]
                else:
                    level_size_x += event.unicode
            elif input_active_y:
                if event.key == pygame.K_RETURN:
                    input_active_y = False
                elif event.key == pygame.K_BACKSPACE:
                    level_size_y = level_size_y[:-1]
                else:
                    level_size_y += event.unicode

    # this part handles side panel moving up and down
    if pressed_key[pygame.K_DOWN]:
        scroll_offset -= scroll_speed
    if pressed_key[pygame.K_UP]:
        scroll_offset += scroll_speed

    screen.fill((0, 0, 0))  # Clear screen with black
    input_box_x, input_box_y = level_size_value(screen, level_size_x, level_size_y)  # Get the input box rects for collision detection

    level_size_x_int = int(level_size_x) if level_size_x.isdigit() else 0
    level_size_y_int = int(level_size_y) if level_size_y.isdigit() else 0

    level_grid = draw_level_area(screen, level_size_x_int, level_size_y_int, cell_images)

    side_panel(screen, (0, 0, 0), scroll_offset)
    selected_image(screen, clicked_img)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
