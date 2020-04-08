import math

import pyglet

from player import Char, p
from crosshair import c

#p = Char()


class Gun:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bron = pyglet.image.load("gun.png")
        self.gun = pyglet.sprite.Sprite(self.bron, self.x, self.y)
        self.bron.anchor_x = self.bron.width // 2
        self.bron.anchor_y = self.bron.height // 2
        self.mouse_x = 0
        self.mouse_y = 0

    def draw(self):
        self.gun.update(self.x, self.y, self.mangle)
        self.gun.draw()

    def update(self):
        self.x = p.x
        self.y = p.y - 5
        self.mangle = self.get_angle(self.mouse_x, self.mouse_y)
        print(self.mangle)
    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def get_angle(self, mouse_x, mouse_y):
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        return angle
    #def on_mouse_press(self, x, y, button, modifiers):

    #def on_mouse_release(self, x ,y , button, modifiers):

