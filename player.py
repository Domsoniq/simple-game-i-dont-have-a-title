import math

import pyglet
from pyglet import window
from pyglet.window import key

from mapp import Mapp

m = Mapp("mapp.txt")


class Char:

    def __init__(self):
        self.x = 100
        self.y = 100

        self.Image = pyglet.image.load("player.png")
        self.Image.anchor_x = self.Image.width // 2
        self.Image.anchor_y = self.Image.height // 2
        self.player = pyglet.sprite.Sprite(self.Image, self.x, self.y)
        self.speed = 500
        self.keys = ['w', 'a', 's', 'd']
        self.kstate = [0, 0, 0, 0]

    def draw(self):
        self.player.update(self.x, self.y)
        self.player.draw()

    def key_press(self, symbol):
        i = 0
        for k in self.keys:
            if symbol == ord(k):
                self.kstate[i] = 1
            i = i + 1

    def key_release(self, symbol):
        i = 0
        for k in self.keys:
            if symbol == ord(k):
                self.kstate[i] = 0
            i = i + 1

    def update(self, dt):
        self.dy = 0
        self.dx = 0
        if self.kstate[0] == 1:
            self.dy = self.speed * dt
        if self.kstate[2] == 1:
            self.dy = -self.speed * dt
        if self.kstate[3] == 1:
            self.dx = self.speed * dt
        if self.kstate[1] == 1:
            self.dx = -self.speed * dt

        self.x += self.dx
        self.y += self.dy

        if self.map_collide(self.x, self.y):
            self.x -= self.dx
            self.y -= self.dy

    def map_collide(self, x, y):
        dx = self.Image.width // 2
        dy = self.Image.height // 2
        w1 = m.collision(x-dx, y+dy)
        w2 = m.collision(x+dx, y+dy)
        w3 = m.collision(x+dx, y-dy)
        w4 = m.collision(x-dx, y-dy)

        return w1 or w2 or w3 or w4


p = Char()
