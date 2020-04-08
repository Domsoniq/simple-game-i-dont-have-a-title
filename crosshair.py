import pyglet


class Crosshair:
    def __init__(self):
        self.crosshair = pyglet.image.load("crosshair.png")
        self.x = 0
        self.y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.crosshair.anchor_x = self.crosshair.width // 2
        self.crosshair.anchor_y = self.crosshair.height // 2

    def draw(self):
        self.crosshair.blit(self.x, self.y)
        pyglet.gl.glBlendFunc(
            pyglet.gl.GL_SRC_ALPHA,
            pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def update(self):
        self.x = self.mouse_x
        self.y = self.mouse_y


c = Crosshair()
