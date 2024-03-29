import pygame
import sys

MOVEMENT_SPEED = 1
GRAVITY = 0.2
TILE_SIZE = 24

class PhysicsEntity:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])


    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        print(self.pos)

        # X movement and collision
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x


        # Y movement and collision
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):


                if frame_movement[1] >= 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                    frame_movement = frame_movement[0], 0
                    self.velocity[1] = 0


                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True

                self.pos[1] = entity_rect.y



        # Gravity babyyyyyy
        

                if self.collisions['down'] or self.collisions['up'] == True:
                    self.velocity[1] = 0
                    print('stopped')
                if self.collisions['left'] or ['right'] == True:
                    self.velocity[0] = 0

        if self.collisions['down'] or self.collisions['up'] == True:
            pass
        else:
            self.velocity[1] = min(5, self.velocity[1] + GRAVITY)







    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

