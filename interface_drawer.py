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

        
    def exporter(self):
        return self.images_list

    def scale_image(self, img):
        if img.get_width() > self.holder_width - 10:
            scale_factor = (self.holder_width - 10) / img.get_width()
            img = pygame.transform.scale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
            print(f"Scaled image to: {img.get_size()}")
        return img

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            for rect in self.rects_list:
                rect.y += self.scroll_speed
        if keys[pygame.K_DOWN]:
            for rect in self.rects_list:
                rect.y -= self.scroll_speed


    def draw(self, surface: pygame.Surface):
        holder = pygame.Surface((self.holder_width, self.holder_height))
        holder.fill((255, 122, 61)) # orange
        holder_rect = holder.get_rect(topleft=(self.holder_x, self.holder_y))

        # Draw images on holder
        for i in range(len(self.images_list)):
            img_rect = self.rects_list[i].move(0, self.scroll_offset)
            
            gray_rect = pygame.Rect(img_rect.left - 5, img_rect.top - 5, img_rect.width + 10, img_rect.height + 10)
            
            holder.blit(self.images_list[i], self.rects_list[i])

        
        surface.blit(holder, holder_rect.topleft)


class ChosenPicture(pygame.sprite.Sprite):
    def __init__(self, location_x, location_y, image=None) -> None:
        super().__init__()
        self.location_x = location_x
        self.location_y = location_y
        self.image = image
        
            

    def update(self) -> None:
        if self.image == None:
            self.image = pygame.Surface((40, 40))
            self.image.fill((200, 100, 50))
            self.rect = self.image.get_rect(center=(self.location_x, self.location_y))
        else:
            self.image = self.image
            self.rect = self.image.get_rect(center=(self.location_x, self.location_y))
    
    def state_setter(self):
        self.image = None
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
        