import random as rd
import pygame as pg
from settings import *
Vec = pg.math.Vector2

class AsteroidAbstract(pg.sprite.Sprite):
    def __init__(self, init_pos):
        super().__init__()
        self.animation_count = 0.0
        self.direction = Vec(rd.randint(-10, 10), rd.randint(1, 10)).normalize()
        self.pos = init_pos
        self.image = None
        self.rect = None
        self.speed = rd.randint(1, 5)
        self.damage = 0

    def update(self):
        self.animation_count += 0.1
        self.pos += self.speed * self.direction.normalize()
        self.image = self.images[int(self.animation_count) % 15]

        mask = self.image.get_bounding_rect()
        self.image = self.image.subsurface(mask).copy()
        self.rect = self.image.get_rect(center=self.pos)

        if self.pos.x + self.rect.width / 2 < TEXT_WIDTH:
            self.pos.x = TEXT_WIDTH - self.rect.width / 2
            self.direction.x *= -1
        if self.pos.x + self.rect.width / 2 > WIDTH:
            self.pos.x = WIDTH - self.rect.width / 2
            self.direction.x *= -1
        if self.pos.y + self.rect.height / 2 < 0:
            self.pos.y = -self.rect.height / 2
            self.direction.y *= -1
        if self.pos.y + self.rect.height / 2 > HEIGHT:
            self.pos.y = HEIGHT - self.rect.height / 2
            self.direction.y *= -1

    def draw(self, surface):
        pg.draw.rect(surface, (0, 0, 255), self.rect, 2)
