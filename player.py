
import pygame
import constants
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
        """ This class represents the player. """

        # Direction of the player
        direction = "R"
        speed_x = 0
        speed_y = 0
        walking_frames_l = []
        walking_frames_r = []
        walking_frames_u = []
        walking_frames_d = []

        def __init__(self):

                pygame.sprite.Sprite.__init__(self)
                sprite_sheet = SpriteSheet("Ninja.png")

                #This holds all the images for the animated walk
                
                
                #Load all the right facing images into a list
                image = sprite_sheet.get_image(14, 54, 24, 24)
                self.walking_frames_r.append(image)
                image = sprite_sheet.get_image(51, 56, 24, 24)
                self.walking_frames_r.append(image)
                image = sprite_sheet.get_image(86, 54, 24, 24)
                self.walking_frames_r.append(image)
                image = sprite_sheet.get_image(114, 57, 24, 24)
                self.walking_frames_r.append(image)

                #Load all the right facing images, tehn flip them(left)
                image = sprite_sheet.get_image(14, 54, 24, 24)
                image = pygame.transform.flip(image, True, False)
                self.walking_frames_l.append(image)
                image = sprite_sheet.get_image(51, 56, 24, 24)
                image = pygame.transform.flip(image, True, False)
                self.walking_frames_l.append(image)
                image = sprite_sheet.get_image(86, 54, 24, 24)
                image = pygame.transform.flip(image, True, False)
                self.walking_frames_l.append(image)
                image = sprite_sheet.get_image(114, 57, 24, 24)
                image = pygame.transform.flip(image, True, False)
                self.walking_frames_l.append(image)

                #Load UP facing images
                image = sprite_sheet.get_image(96, 118, 24, 24)
                self.walking_frames_u.append(image)
                image = sprite_sheet.get_image(123, 118, 24, 24)
                self.walking_frames_u.append(image)

                #Load Down facing images
                image = sprite_sheet.get_image(99, 90, 24, 24)
                self.walking_frames_d.append(image)

                #Set the image the player starts with
                self.image = self.walking_frames_r[0]

                #Set a referance to the image rect
                self.rect = self.image.get_rect()
               

        def update(self):
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                posx = self.rect.x
                posu = self.rect.y
                if self.speed_x == 0 and self.speed_y == 0:
                        self.direction = "S"
                if self.direction == "R":
                        # Number 30 is the speed to change animations
                        frame = (posx // 30) % len(self.walking_frames_r)
                        self.image = self.walking_frames_r[frame]
                elif self.direction == "L":
                        frame = (posx // 30) % len(self.walking_frames_l)
                        self.image = self.walking_frames_l[frame]
                elif self.direction == "U":
                        frame = (posu // 30) % len(self.walking_frames_u)
                        self.image = self.walking_frames_u[frame]
                elif self.direction == "D":
                        frame = (posu // 30) % len(self.walking_frames_d)
                        self.image = self.walking_frames_d[frame]
                else:
                        self.image = self.walking_frames_r[0]

        #Player-controlled movement:
        def go_left(self):
                self.speed_x = -6
                self.direction = "L"

        def go_right(self):
                self.speed_x = 6
                self.direction = "R"

        def go_up(self):
                self.speed_y = -6
                self.direction = "U"

        def go_down(self):
                self.speed_y = 6
                self.direction = "D"

        def stopx(self):
                self.speed_x = 0

        def stopy(self):
                self.speed_y = 0

        
