from os.path import join
import random as rd
import pygame as pg
from settings import *

class RocketStdIcon(pg.sprite.Sprite):
    def __init__(self, init_pos):
        super().__init__()
        self.pos = init_pos
        self.image = pg.image.load(join('assets', 'Ships', 'Weapons', 'rocket_std.png'))
        self.image = pg.transform.scale_by(self.image, 3)
        self.amount = rd.randint(1, 10)
        mask = self.image.get_bounding_rect()
        self.image = self.image.subsurface(mask).copy()
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, surface):
        pg.draw.rect(surface, (0, 255, 0), self.rect, 1)
