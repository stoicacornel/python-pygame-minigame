
import pygame
import constants
import random
from spritesheet_functions import SpriteSheet

class Enemy(pygame.sprite.Sprite):
        """ This class represents a simple block the player collects. """

        walking_frames1 = []
        walking_frames2 = []

        def __init__(self):
                """ Constructor, create the image of the block. """
                pygame.sprite.Sprite.__init__(self)
                sprite_sheet = SpriteSheet("Skeleton1.png")

                self.image = sprite_sheet.get_image(104, 80, 22, 47)
                self.walking_frames1.append(self.image)
                self.image = sprite_sheet.get_image(136, 80, 18, 47)
                self.walking_frames1.append(self.image)
                self.image = sprite_sheet.get_image(167, 80, 22, 47)
                self.walking_frames1.append(self.image)
                self.image = sprite_sheet.get_image(136, 80, 18, 47)
                self.walking_frames1.append(self.image)

                self.image = sprite_sheet.get_image(4, 88, 24, 40)
                self.walking_frames2.append(self.image)
                self.image = sprite_sheet.get_image(36, 87, 24, 40)
                self.walking_frames2.append(self.image)
                self.image = sprite_sheet.get_image(68, 88, 24, 39)
                self.walking_frames2.append(self.image)
                
                self.rect = self.image.get_rect()

        def reset_pos(self):
                """ Called when the block is 'collected' or falls off
                the screen. """
                self.rect.y = random.randrange(100, constants.SCREEN_HEIGHT)
                self.rect.x = random.randrange(1250, 1800)

        def update(self):
                """ Automatically called when we need to move the block. """
                self.rect.x -= 3

                pos = self.rect.x
                if self.rect.y > 520:
                        frame = (pos // 15) % len(self.walking_frames1)
                        self.image = self.walking_frames1[frame]
                else:
                        frame = (pos // 15) % len(self.walking_frames2)
                        self.image = self.walking_frames2[frame]

                if self.rect.x < 11 - self.rect.width:
                        self.reset_pos()
 
