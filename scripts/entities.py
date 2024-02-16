import pygame

class PhysicsEntity:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = size

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

