import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        pygame.display.set_caption('Zelda')
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sounds = pygame.mixer.Sound('audio/main.ogg')
        main_sounds.play(loops=-1)
        main_sounds.set_volume(0.4)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
