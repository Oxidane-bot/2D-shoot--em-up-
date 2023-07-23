import pygame
import random


class power_item(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        super().__init__()
        self.screen_rect = screen_rect
        self.image= pygame.image.load("MiniPixelPack\Items\Power_item (16 x 16).png").subsurface(pygame.Rect(0, 0, 16, 16))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(60,self.screen_rect.right-60)
        self.rect.y = 0
        self.speed = 1

    
    def update(self):
        self.rect.y += self.speed