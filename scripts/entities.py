import pygame

MOVEMENT_SPEED = 1

class PhysicsEntity:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]


    def update(self, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # X movement and collision
        self.pos[0] += frame_movement[0]

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

