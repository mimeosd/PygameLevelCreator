import pygame
import constants
from interface_drawer import side_panel, check_click, selected_image
from file_get_helper import find_png_images

pygame.init()

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGTH))  # TODO add full screen support
pygame.display.set_caption("Level creator")

clock = pygame.time.Clock()

scroll_offset = 0
scroll_speed = 5

clicked_img = None

running = True
while running:
    pressed_mouse = pygame.mouse.get_pressed()
    pressed_key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # lmb
            mouse_pos = event.pos
            clicked_image = check_click(mouse_pos, scroll_offset)
            if clicked_image:
                clicked_img = clicked_image
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # rmb
            clicked_img = None

    if pressed_key[pygame.K_DOWN]:
        scroll_offset -= scroll_speed
    if pressed_key[pygame.K_UP]:
        scroll_offset += scroll_speed

    screen.fill((0, 0, 0))  # Clear screen with black
    side_panel(screen, (0, 0, 0), scroll_offset)

    selected_image(screen, clicked_img)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
