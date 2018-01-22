
import pygame
import constants
from spritesheet_functions import SpriteSheet

class Bullet(pygame.sprite.Sprite):

        bullet_frames = []
        def __init__(self):
                """ Constructor, create the image of the block. """
                pygame.sprite.Sprite.__init__(self)
                sprite_sheet = SpriteSheet("Shuriken.png")

                self.image = sprite_sheet.get_image(146, 121, 11, 11)
                self.bullet_frames.append(self.image)
                self.image = sprite_sheet.get_image(165, 121, 11, 11)
                self.bullet_frames.append(self.image)
                self.image = sprite_sheet.get_image(188, 121, 10, 11)
                self.bullet_frames.append(self.image)

                self.rect = self.image.get_rect()

        def update(self):
                self.rect.x += 25
                self.rect.y += 4

                pos = self.rect.x
                frame = (pos // 5) % len(self.bullet_frames)
                self.image = self.bullet_frames[frame]
