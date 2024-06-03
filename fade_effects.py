import pygame

WIDTH, HEIGHT = 800, 600


class FadeScreen(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, size_x, size_y) -> None:
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.size_x = size_x
        self.size_y = size_y
        self.surface = pygame.Surface((size_x, size_y))
        self.surface.fill((0, 255, 0))
        self.speed = 5
        self.font = pygame.font.Font(None, 36)
        
        

    def update(self):
        
        if self.start_x >= WIDTH:
            self.start_x += 0
            self.render_text(screen)
        else:
            self.start_x += 5



    def draw(self, screen: pygame.Surface):
        for i in range(HEIGHT // self.size_y):
            screen.blit(self.surface, (self.start_x - 10, self.start_y * i))

    
    def render_text(self, screen):
        font_surf = self.font.render("Your text here", True, (255, 255, 255), (0, 0, 0))
        font_rect = font_surf.get_rect(center=(400, 300))
        screen.blit(font_surf, font_rect)


class FadeScreen2(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, size_x, size_y) -> None:
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.size_x = size_x
        self.size_y = size_y
        self.surface = pygame.Surface((size_x, size_y))
        self.surface.fill((255, 0, 0))
        self.speed = -5
        self.font = pygame.font.Font(None, 36)
        
        

    def update(self):
        
        if self.start_x <= -10:
            self.start_x += 0
            self.render_text(screen)
        else:
            self.start_x += self.speed



    def draw(self, screen: pygame.Surface):
        for i in range(HEIGHT // self.size_y):
            screen.blit(self.surface, (self.start_x, self.start_y * i + 10))

    def render_text(self, screen):
        font_surf = self.font.render("Your text here", True, (255, 255, 255), (0, 0, 0))
        font_rect = font_surf.get_rect(center=(400, 300))
        screen.blit(font_surf, font_rect)


pygame.init()


fade_group = pygame.sprite.Group()

f1 = FadeScreen(0, 20, 10, 8)
fade_group.add(f1)

# Uncomment to add this animation
# f2 = FadeScreen2(WIDTH, 20, 10, 8)
# fade_group.add(f2)



screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for f in fade_group:
        f.update()
        f.draw(screen)
    
    pygame.display.update()
    clock.tick(60)