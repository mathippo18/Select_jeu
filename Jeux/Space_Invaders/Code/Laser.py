import pygame
import os


# File Importing (Changes Directory to Where the File is Saved)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill("White")
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.height_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()