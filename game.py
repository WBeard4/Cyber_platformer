import pygame
import sys

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
FPS = 60
START_LOCATION = [300, 30]
TILE_SIZE = 24

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('cyber platformer')
        self.screen = pygame.display.set_mode((640, 480))
      #  self.screen = pygame.Surface((640, 480))
        self.clock = pygame.time.Clock()

        self.img_pos = (self.screen.get_width() / 2), (self.screen.get_height() / 2)
        self.movement = [False, False]
        
        self.assets = {
            'player': load_image('entities/player.png'),
            'base': load_images('tiles/base'),
        }


        self.tilemap = Tilemap(self, tile_size=TILE_SIZE)
        self.tilemap.load('map.json')
        self.player = PhysicsEntity(self,  START_LOCATION, (17, 46))

        self.scroll = [0, 0]

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            # This is the formula that locks the camera to the character
            self.scroll[0] += (self.player.rect().centerx - self.screen.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.screen.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))


            self.tilemap.render(self.screen, offset=(0, 0))

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_F12: # Resets character back to 0,0
                        self.player.pos[0] = START_LOCATION[0]
                        self.player.pos[1] = START_LOCATION[1]
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    


            #self.screen.blit(self.screen, (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
game = Game()
game.run()