import pygame

class Enemy_bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.images = [pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(0, 0, 16, 16)),
        pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(16, 0, 16, 16)),
        pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(32, 0, 16, 16)),
        pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(48, 0, 16, 16))]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

        

    def update(self):
        self.rect.y += self.speed


class Enemy_bullet_trace(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, target):
        super().__init__()
        self.images = [pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(0, 0, 16, 16)),
                       pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(16, 0, 16, 16)),
                       pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(32, 0, 16, 16)),
                       pygame.image.load("MiniPixelPack\Projectiles\Enemy_projectile (16 x 16).png").subsurface(pygame.Rect(48, 0, 16, 16))]
        self.image = self.images[2]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.target = target
        self.flag = 1
        self.x_offset = 0
        self.y_offset = 0

    def update(self):
        if self.flag == 1:
            # Calculate the x and y offset between the bullet and the target
            self.x_offset = self.target.rect.x - self.rect.x
            self.y_offset = self.target.rect.y - self.rect.y
            self.flag = 0
        # Calculate the ratio between the speed and the offset to determine the direction
        ratio = self.speed / ((self.x_offset ** 2 + self.y_offset ** 2) ** 0.5)

        # Update the bullet's x and y position based on the calculated ratio
        self.rect.x += self.x_offset * ratio
        self.rect.y += self.y_offset * ratio


