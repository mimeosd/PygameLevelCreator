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
level_size_x = "10"  # Starting examplary level size value for x
level_size_y = "10"  # Starting examplary level size value for y
input_active_x = False
input_active_y = False

running = True
while running:
    pressed_mouse = pygame.mouse.get_pressed()
    pressed_key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            # this first part covers collisions with entry boxes for x and y size of level to be drawn
            mouse_pos = event.pos
            clicked_image = check_click(mouse_pos, scroll_offset) # Check if clicked on rect of an image. if clicked = True else False
            if clicked_image:
                clicked_img = clicked_image

            # Check if the mouse click is within the input boxes below
            if input_box_x.collidepoint(mouse_pos):
                input_active_x = True
                input_active_y = False
            elif input_box_y.collidepoint(mouse_pos):
                input_active_y = True
                input_active_x = False
            else:
                input_active_x = False
                input_active_y = False

            # TODO add check for collision with level grid here, this is second part
            for level_grid_cell in level_grid:
                if level_grid_cell.collidepoint(mouse_pos):
                    print(f"Clicked {level_grid_cell}")
                    draw_level_area(screen, level_size_x_int, level_size_y_int, clicked_image) # This part here making issues....

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

    if pressed_key[pygame.K_DOWN]:
        scroll_offset -= scroll_speed
    if pressed_key[pygame.K_UP]:
        scroll_offset += scroll_speed

    screen.fill((0, 0, 0))  # Clear screen with black
    input_box_x, input_box_y = level_size_value(screen, level_size_x, level_size_y)  # Get the input box rects for collision detection

    
    level_size_x_int = int(level_size_x) if level_size_x.isdigit() else 0
    level_size_y_int = int(level_size_y) if level_size_y.isdigit() else 0
    

    level_grid = draw_level_area(screen, level_size_x_int, level_size_y_int)

    side_panel(screen, (0, 0, 0), scroll_offset)
    selected_image(screen, clicked_img)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
