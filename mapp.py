import pyglet

tilesize = 60


class Mapp:
    def __init__(self, filename):
        self.wall = pyglet.image.load("wall.png")
        self.data = []
        with open(filename) as f:
            for line in f:
                self.data.append(line)

    def draw(self):
        wall_y = 0
        for line in self.data:
            wall_x = 0
            for spot in line:
                if spot == '#':
                    self.wall.blit(wall_x, wall_y)
                wall_x += 60
            wall_y += 60

    def collision(self, xx, yy):
        nk = int(xx // tilesize)
        nl = int(yy // tilesize)
        line = self.data[nl]
        spot = line[nk]
        return spot == "#"

