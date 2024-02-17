import pygame
import sys

from scripts.utils import load_image
from scripts.entities import PhysicsEntity
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('cyber platformer')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()

        #self.img_pos = (self.display.get_width() / 2), (self.display.get_height() / 2)
        self.movement = [False, False]
        
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, (0, 0), (17, 46))
    def run(self):
        while True:
            self.display.fill((255, 255, 255))
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
game = Game()
game.run()