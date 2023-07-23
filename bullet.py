import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("MiniPixelPack/Projectiles/Player_beam (16 x 16).png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.x = x - 8
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
    
    def explode(self):
        pass
