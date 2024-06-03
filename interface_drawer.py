import pygame
from file_get_helper import find_png_images
import constants

class PictureDrawer(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__()
        self.screen = screen
        self.images_list = []
        self.rects_list = []
        self.holder_width = 350
        self.holder_height = screen.get_height() - 20
        self.holder_x = 830
        self.holder_y = 10
        self.scroll_offset = 0
        self.scroll_speed = 10

        image_spacing = 30  # Space between images

        x, y = image_spacing, image_spacing
        max_x = self.holder_width - image_spacing

        for img_path in find_png_images():
            img = pygame.image.load(img_path).convert_alpha()
            img = self.scale_image(img)
            self.images_list.append(img)
            rect = img.get_rect(topleft=(x, y))
            self.rects_list.append(rect)
            print(f"Loaded image: {img_path}, size: {img.get_size()}, position: {rect.topleft}")
            
            x += img.get_width() + image_spacing
            if x > max_x:
                x = image_spacing
                y += img.get_height() + image_spacing + 10

    def scale_image(self, img):
        if img.get_width() > self.holder_width - 10:
            scale_factor = (self.holder_width - 10) / img.get_width()
            img = pygame.transform.scale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
            print(f"Scaled image to: {img.get_size()}")
        return img

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.scroll_offset = min(self.scroll_offset + self.scroll_speed, 0)
        if keys[pygame.K_DOWN]:
            max_scroll = min(0, self.holder_height - (self.rects_list[-1].bottom + self.scroll_offset + 10))
            self.scroll_offset = max(self.scroll_offset - self.scroll_speed, max_scroll)

    def draw(self, surface: pygame.Surface):
        # Draw "holder" of all items
        holder = pygame.Surface((self.holder_width, self.holder_height))
        holder.fill((255, 122, 61))
        holder_rect = holder.get_rect(topleft=(self.holder_x, self.holder_y))

        # Draw images on holder
        for i in range(len(self.images_list)):
            img_rect = self.rects_list[i].move(0, self.scroll_offset)
            # if holder_rect.collidepoint(img_rect.topleft) or holder_rect.collidepoint(img_rect.bottomright):
                # Draw gray square relative to the holder
            gray_rect = pygame.Rect(img_rect.left - 5, img_rect.top - 5, img_rect.width + 10, img_rect.height + 10)
            pygame.draw.rect(holder, (169, 169, 169), gray_rect.move(-gray_rect.left + img_rect.left, -gray_rect.top + img_rect.top))
            # Draw image
            
            holder.blit(self.images_list[i], (img_rect.left - self.holder_x, img_rect.top - self.holder_y))

        # Blit holder to the main surface
        surface.blit(holder, holder_rect.topleft)
