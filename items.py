
import pygame
import constants
from spritesheet_functions import SpriteSheet

class Heart(pygame.sprite.Sprite):

        life_frames = []
        i = 0

        def __init__(self):
                """ Constructor, create the image of the block. """
                pygame.sprite.Sprite.__init__(self)
                sprite_sheet = SpriteSheet("Hearts.png")

                self.image = sprite_sheet.get_image(0, 0, 15, 13)
                self.life_frames.append(self.image)
                self.image = sprite_sheet.get_image(15, 0, 15, 13)
                self.life_frames.append(self.image)
                self.image = sprite_sheet.get_image(30, 0, 15, 13)
                self.life_frames.append(self.image)
                self.image = sprite_sheet.get_image(45, 0, 15, 13)
                self.life_frames.append(self.image)
                self.image = sprite_sheet.get_image(60, 0, 15, 13)
                self.life_frames.append(self.image)
                self.image = sprite_sheet.get_image(75, 0, 15, 13)
                self.life_frames.append(self.image)
                self.image = sprite_sheet.get_image(90, 0, 15, 13)
                self.life_frames.append(self.image)

                self.rect = self.image.get_rect()

                #self.rect.x = None
                #self.rect.y = None

        def update(self):
                self.i += 1

                pos = self.i
                frame = (pos // 1) % len(self.life_frames)
                self.image = self.life_frames[frame]

class Emperor_Heart(pygame.sprite.Sprite):

        emperor_life_frames = []
        i = 0

        def __init__(self):
                """ Constructor, create the image of the block. """
                pygame.sprite.Sprite.__init__(self)
                sprite_sheet = SpriteSheet("Hearts2.png")

                self.image = sprite_sheet.get_image(0, 0, 15, 13)
                self.emperor_life_frames.append(self.image)
                self.image = sprite_sheet.get_image(15, 0, 15, 13)
                self.emperor_life_frames.append(self.image)
                self.image = sprite_sheet.get_image(30, 0, 15, 13)
                self.emperor_life_frames.append(self.image)
                self.image = sprite_sheet.get_image(45, 0, 15, 13)
                self.emperor_life_frames.append(self.image)
                self.image = sprite_sheet.get_image(60, 0, 15, 13)
                self.emperor_life_frames.append(self.image)
                self.image = sprite_sheet.get_image(75, 0, 15, 13)
                self.emperor_life_frames.append(self.image)
                self.image = sprite_sheet.get_image(90, 0, 15, 13)
                self.emperor_life_frames.append(self.image)

                self.rect = self.image.get_rect()

                #self.rect.x = None
                #self.rect.y = None

        def update(self):
                self.i += 1

                pos = self.i
                frame = (pos // 1) % len(self.emperor_life_frames)
                self.image = self.emperor_life_frames[frame]
