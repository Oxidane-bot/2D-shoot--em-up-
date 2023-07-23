import pygame

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self,image,screen_rect):
        super().__init__()
        self.image = pygame.image.load('MiniPixelPack\PlayerShip\Player_ship (16 x 16).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (96, 32))
        self.images = [self.image.subsurface(pygame.Rect(i * 32, 0, 32, 32)) for i in range(3)]
        self.image = self.images[1]
        self.normal_image = self.image
        self.imune_image = pygame.Surface((self.image.get_width(), self.image.get_height()), pygame.SRCALPHA)
        self.imune_image.fill((255, 255, 255, 0))

        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        self.rect.center = self.screen_rect.center
        self.lives = 10   # how many lives player has
        self.imune = False

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        if self.imune:
            current_time = pygame.time.get_ticks()
            if current_time - self.imune_timer >= 2000:  # 2 seconds in milliseconds
                self.imune = False
            else:
                # Show alternate image for every 50 milliseconds to create flashing effect
                if current_time % 100 < 50:
                    self.image = self.imune_image
                else:
                    self.image = self.normal_image
        else:
            self.image = self.normal_image
    
    def hit(self):
        if self.imune == False:
            self.lives -= 1 
            self.imune = True
            self.imune_timer = pygame.time.get_ticks()







