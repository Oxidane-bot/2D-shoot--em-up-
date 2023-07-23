import pygame
from random import randint
import random


class Alan(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.screen_rect = screen_rect
        self.name = None
        # Load the image and scale it to 32 x 32
        self.images = [pygame.image.load("MiniPixelPack/Enemies/Alan (16 x 16).png").subsurface(
            pygame.Rect(i * 16, 0, 16, 16)) for i in range(6)]
        self.images = [pygame.transform.scale(
            image, (32, 32)) for image in self.images]

        # Set the starting image
        self.image = self.images[0]

        # Set the rect for the sprite
        self.rect = self.image.get_rect()
        self.rect.x = randint(60, self.screen_rect.right-60)
        self.rect.y = 0

        # Set the animation timer
        self.animation_timer = 0
        self.animation_fps = 10
        self.current_frame = 0

        # Load explosion image
        self.explosion_images = [pygame.image.load(
            "MiniPixelPack/Effects/Explosion (16 x 16).png").subsurface(pygame.Rect(i * 16, 0, 16, 16)) for i in range(6)]
        self.explosion_images = [pygame.transform.scale(
            image, (32, 32)) for image in self.explosion_images]
        self.explosion_timer = 0
        self.explosion_fps = 10
        self.explosion_frame = 0
        self.exploding = False

    def update(self):
        self.animation_timer += 1
        if self.animation_timer % self.animation_fps == 0:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]

        self.rect.y += 1

        if self.rect.y > self.screen_rect.bottom:
            self.kill()

        if self.exploding:
            self.explosion_timer += 1
            if self.explosion_timer % self.explosion_fps == 0:
                self.explosion_frame = (
                    self.explosion_frame + 1) % len(self.explosion_images)
                self.image = self.explosion_images[self.explosion_frame]
                if self.explosion_frame == len(self.explosion_images) - 1:
                    self.kill()

    def explode(self):
        self.exploding = True


class Bon(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.screen_rect = screen_rect
        self.name = None
        self.last_shot = 0
        # Load the image and scale it to 64 x 64
        self.images = [pygame.image.load("MiniPixelPack/Enemies/Bon_Bon (16 x 16).png").subsurface(
            pygame.Rect(i * 16, 0, 16, 16)) for i in range(4)]
        self.images = [pygame.transform.scale(
            image, (32, 32)) for image in self.images]

        # Set the starting image
        self.image = self.images[0]

        # Set the rect for the sprite
        self.rect = self.image.get_rect()
        self.rect.x = randint(60, self.screen_rect.right-60)
        self.rect.y = 0

        # Set the animation timer
        self.animation_timer = 0
        self.animation_fps = 10
        self.current_frame = 0

        # Load explosion image
        self.explosion_images = [pygame.image.load(
            "MiniPixelPack/Effects/Explosion (16 x 16).png").subsurface(pygame.Rect(i * 16, 0, 16, 16)) for i in range(6)]
        self.explosion_images = [pygame.transform.scale(
            image, (32, 32)) for image in self.explosion_images]
        self.explosion_timer = 0
        self.explosion_fps = 10
        self.explosion_frame = 0
        self.exploding = False

        # Additional attributes for Bon
        self.direction = random.choice([-1, 1])

    def update(self):
        self.animation_timer += 1
        if self.animation_timer % self.animation_fps == 0:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]

        self.rect.y += 1

        # Movement left and right
        self.rect.x += self.direction
        if self.rect.left < 0 or self.rect.right > self.screen_rect.right:
            self.direction *= -1

        if self.rect.y > self.screen_rect.bottom:
            self.kill()
        if self.exploding:
            self.explosion_timer += 1
            if self.explosion_timer % self.explosion_fps == 0:
                self.explosion_frame = (
                    self.explosion_frame + 1) % len(self.explosion_images)
                self.image = self.explosion_images[self.explosion_frame]
                if self.explosion_frame == len(self.explosion_images) - 1:
                    self.kill()

    def explode(self):
        self.exploding = True


class Lips(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.name = None
        self.last_shot = 0
        self.screen_rect = screen_rect
        self.images = [pygame.image.load("MiniPixelPack/Enemies/Lips (16 x 16).png").subsurface(
            pygame.Rect(i * 16, 0, 16, 16)) for i in range(5)]
        self.images = [pygame.transform.scale(
            image, (32, 32)) for image in self.images]

        # Set the starting image
        self.image = self.images[0]

        # Set the rect for the sprite
        self.rect = self.image.get_rect()
        self.rect.x = randint(60, self.screen_rect.right-60)
        self.rect.y = 0

        # Load explosion image
        self.explosion_images = [pygame.image.load(
            "MiniPixelPack/Effects/Explosion (16 x 16).png").subsurface(pygame.Rect(i * 16, 0, 16, 16)) for i in range(6)]
        self.explosion_images = [pygame.transform.scale(
            image, (32, 32)) for image in self.explosion_images]
        self.explosion_timer = 0
        self.explosion_fps = 10
        self.explosion_frame = 0
        self.exploding = False

        # Set the animation timer
        self.animation_timer = 0
        self.animation_fps = 5  # Set a faster animation speed
        self.current_frame = 0

    def update(self):
        self.animation_timer += 1
        if self.animation_timer % self.animation_fps == 0:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]

        # Move the sprite down
        self.rect.y += 1

        # Remove the sprite if it goes off the screen
        if self.rect.y > self.screen_rect.bottom:
            self.kill()

        if self.exploding:
            self.explosion_timer += 1
            if self.explosion_timer % self.explosion_fps == 0:
                self.explosion_frame = (
                    self.explosion_frame + 1) % len(self.explosion_images)
                self.image = self.explosion_images[self.explosion_frame]
                if self.explosion_frame == len(self.explosion_images) - 1:
                    self.kill()

    def explode(self):
        self.exploding = True
