
import pygame

import constants
import random

from player import Player
from enemy import Enemy
from bullet import Bullet
from items import Heart
from items import Emperor_Heart

# --- Classes ---

class Game():
        """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
        enemy_list = None
        all_sprite_list = None
        player = None
        game_over = False
        bullet_list = None
        lifes = None
        emperor_lifes = None
        items_list = None
        items_list2 = None

        def __init__(self):
                """ Constructor. Create all our attributes and initialize
                the game. """

                self.score = 0
                self.game_over = False
                self.lifes = 3
                self.emperor_lifes = 5
                pygame.mixer.music.load("Song.ogg")
                pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
                pygame.mixer.music.play()

                # Create sprite lists
                self.enemy_list = pygame.sprite.Group()
                self.all_sprites_list = pygame.sprite.Group()
                self.bullet_list = pygame.sprite.Group()
                self.items_list = pygame.sprite.Group()
                self.items_list2 = pygame.sprite.Group()

                # Create the block sprites
                for i in range(50):
                        enemy = Enemy()

                        enemy.rect.x = random.randrange(1250, 1800)
                        enemy.rect.y = random.randrange(100, constants.SCREEN_HEIGHT - 20)

                        self.enemy_list.add(enemy)
                        self.all_sprites_list.add(enemy)

                # Create the player
                self.player = Player()
                self.player.rect.x = 20
                self.player.rect.y = 600
                self.all_sprites_list.add(self.player)

        def process_events(self):
                """ Process all of the events. Return a "True" if we need
                to close the window. """

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if self.game_over:
                                        self.__init__()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        self.player.go_left()
                                if event.key == pygame.K_RIGHT:
                                        self.player.go_right()
                                if event.key == pygame.K_UP:
                                        self.player.go_up()
                                if event.key == pygame.K_DOWN:
                                        self.player.go_down()
                                if event.key == pygame.K_SPACE:
                                        #Add the bullet
                                        self.bullet = Bullet() # This creates one bullet everytime
                                        self.bullet_list.add(self.bullet)
                                        self.all_sprites_list.add(self.bullet)
                                        self.bullet.rect.x = self.player.rect.x + 15
                                        self.bullet.rect.y = self.player.rect.y + 5
                                        
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT:
                                        self.player.stopx()
                                if event.key == pygame.K_RIGHT:
                                        self.player.stopx()
                                if event.key == pygame.K_UP:
                                        self.player.stopy()
                                if event.key == pygame.K_DOWN:
                                        self.player.stopy()
                        if event.type == pygame.constants.USEREVENT:
                                pygame.mixer.music.load("Song.ogg")
                                pygame.mixer.music.play()

                return False

        def run_logic(self):
                """
                This method is run each time through the frame. It
                updates positions and checks for collisions.
                """
                if not self.game_over:
                        if self.player.rect.x < 3:
                                self.player.rect.x = 4
                        if self.player.rect.x > 1160:
                                self.player.rect.x = 1159
                        if self.player.rect.y < 10:
                                self.player.rect.y = 11
                        if self.player.rect.y > 670:
                                self.player.rect.y = 669
                        self.player.rect.x = self.player.rect.x + self.player.speed_x
                        self.player.rect.y = self.player.rect.y + self.player.speed_y
                        # See if the player block has collided with anything.
                        self.enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
                        for enemy in self.enemy_hit_list:
                                self.lifes -= 1
                                self.score += 1
                                enemy = Enemy()
                                enemy.rect.x = random.randrange(1250, 1800)
                                enemy.rect.y = random.randrange(100, constants.SCREEN_HEIGHT - 20)
                                self.enemy_list.add(enemy)
                                self.all_sprites_list.add(enemy)
                        for enemy in self.enemy_list:
                                if enemy.rect.x < -10:
                                        if self.emperor_lifes > 0:
                                                self.emperor_lifes -= 1
                                        else:
                                                self.emperor_lifes = 0

                        for self.bullet in self.bullet_list:
                                self.enemy_hit_list = pygame.sprite.spritecollide(self.bullet, self.enemy_list, True)
                                self.Life = Heart()
                                self.Emperor_Life = Emperor_Heart()
                                # Check the list of collisions.
                                for enemy in self.enemy_hit_list:
                                        self.bullet_list.remove(self.bullet)
                                        self.all_sprites_list.remove(self.bullet)
                                        self.score += 1
                                        if enemy.rect.x % 10 == 0:
                                                self.items_list.add(self.Life)
                                                self.all_sprites_list.add(self.Life)
                                                self.Life.rect.x = enemy.rect.x
                                                self.Life.rect.y = enemy.rect.y
                                        elif enemy.rect.x % 19 == 0:
                                                self.items_list2.add(self.Emperor_Life)
                                                self.all_sprites_list.add(self.Emperor_Life)
                                                self.Emperor_Life.rect.x = enemy.rect.x
                                                self.Emperor_Life.rect.y = enemy.rect.y

                                        enemy = Enemy()
                                        enemy.rect.x = random.randrange(1250, 1800)
                                        enemy.rect.y = random.randrange(100, constants.SCREEN_HEIGHT - 20)
                                        self.enemy_list.add(enemy)
                                        self.all_sprites_list.add(enemy)


                                if self.bullet.rect.x > 1250:
                                        self.bullet_list.remove(self.bullet)
                                        self.all_sprites_list.remove(self.bullet)

                        for self.Life in self.items_list:
                                self.life_collect = pygame.sprite.spritecollide(self.player, self.items_list, True)
                                for self.Life in self.life_collect:
                                        self.items_list.remove(self.Life)
                                        self.all_sprites_list.remove(self.Life)
                                        if self.lifes < 10:
                                                self.lifes += 1
                        for self.Emperor_Life in self.items_list2:
                                self.emperor_life_collect = pygame.sprite.spritecollide(self.player, self.items_list2, True)
                                for self.Emperor_Life in self.emperor_life_collect:
                                        self.items_list2.remove(self.Emperor_Life)
                                        self.all_sprites_list.remove(self.Emperor_Life)
                                        if self.emperor_lifes < 10:
                                                self.emperor_lifes += 1
                        # Move all the sprites
                        self.all_sprites_list.update()

                        if len(self.enemy_list) == 0:
                                self.game_over = True
                        if self.lifes == 0:
                                self.game_over = True
                        if self.emperor_lifes == 0:
                                self.game_over = True
                                

        def display_frame(self, screen):
                """ Display everything to the screen for the game. """
                screen.fill(constants.WHITE)
                control1_image = pygame.image.load("Control1.png").convert()
                control1_image.set_colorkey(constants.WHITE)
                sign_image = pygame.image.load("Sign.png").convert()
                sign_image.set_colorkey(constants.WHITE)
                control2_image = pygame.image.load("Control2.png").convert()
                control2_image.set_colorkey(constants.WHITE)
                hp_image = pygame.image.load("HP1.png").convert()
                hp_image.set_colorkey(constants.WHITE)
                score_frame = pygame.image.load("ButtonOrange.png").convert()
                score_frame.set_colorkey(constants.WHITE)
                background_image = pygame.image.load("Morning.jpg").convert()
                life_image = pygame.image.load("heart1.png").convert()
                emperor_life_image = pygame.image.load("heart2.png").convert()
                life_image.set_colorkey(constants.WHITE)
                emperor_life_image.set_colorkey(constants.WHITE)

                font = pygame.font.SysFont("Serif", 25, False, True,)
                font2 = pygame.font.SysFont("Lithos", 35, True, True)
                text_emperor = font2.render("Protect the Emperor", True, constants.BLACK)
                text_score = font.render("Score: " + str(self.score), True, constants.BLACK)
                text_control1 = font.render("Move", True, constants.BLACK)
                text_control2 = font.render("Shuriken", True, constants.BLACK)
                
                if self.game_over:
                        if self.lifes == 0 :
                                font = pygame.font.SysFont("serif", 25)
                                text = font.render("You died, click to restart", True, constants.BLACK)
                                center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
                                center_y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
                                center_x_s = (constants.SCREEN_WIDTH // 2) - (text_score.get_width() // 2)
                                center_y_s = (constants.SCREEN_HEIGHT // 2) - (text_score.get_height() // 2)
                                screen.blit(text, [center_x, center_y])
                                screen.blit(text_score, [center_x_s, center_y_s + 25])
                        elif self.emperor_lifes == 0:
                                font = pygame.font.SysFont("serif", 25)
                                text = font.render("The Emperor died, click to restart", True, constants.BLACK)
                                center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
                                center_y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
                                center_x_s = (constants.SCREEN_WIDTH // 2) - (text_score.get_width() // 2)
                                center_y_s = (constants.SCREEN_HEIGHT // 2) - (text_score.get_height() // 2)
                                screen.blit(text, [center_x, center_y])
                                screen.blit(text_score, [center_x_s, center_y_s + 25])
 
                        else:
                                font = pygame.font.SysFont("serif", 25)
                                text = font.render("Game Over, click to restart", True, constants.BLACK)
                                center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
                                center_y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
                                center_x_s = (constants.SCREEN_WIDTH // 2) - (text_score.get_width() // 2)
                                center_y_s = (constants.SCREEN_HEIGHT // 2) - (text_score.get_height() // 2)
                                screen.blit(text, [center_x, center_y])
                                screen.blit(text_score, [center_x_s, center_y_s + 25])
                if not self.game_over:
                        screen.blit(background_image, [0,0])
                        screen.blit(score_frame, [7, 10])
                        screen.blit(text_score, [25, 25])
                        screen.blit(hp_image, [993, 10])
                        screen.blit(control1_image, [250, 10])
                        screen.blit(control2_image, [600, 25])
                        screen.blit(text_control1, [400, 20])
                        screen.blit(text_control2, [775, 20])
                        screen.blit(text_emperor, [480, 85])
                        screen.blit(sign_image, [40, 500])
                        for i in range(self.lifes):
                                screen.blit(life_image, [-(i * 15) + 1175, 20])
                        for i in range(self.emperor_lifes):
                                screen.blit(emperor_life_image, [-(i * 15) + 1175, 50])

                        self.all_sprites_list.draw(screen)

                pygame.display.flip()


def main():
        """ Main program function. """
        # Initialize Pygame and set up the window
        pygame.init()

        size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Zombjas")
        pygame.mouse.set_visible(False)

        # Create our objects and set the data
        done = False
        clock = pygame.time.Clock()

        # Create an instance of the Game class
        game = Game()

        # Main game loop
        while not done:

                # Process events (keystrokes, mouse clicks, etc)
                done = game.process_events()

                # Update object positions, check for collisions
                game.run_logic()

                # Draw the current frame
                game.display_frame(screen)

                # Pause for the next frame
                clock.tick(60)

        # Close window and exit
        pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
        main()
