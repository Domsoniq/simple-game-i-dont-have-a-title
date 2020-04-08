import pyglet
from pyglet.window import mouse

from crosshair import Crosshair, c
from gun import Gun
from mapp import Mapp
from player import Char,p

window = pyglet.window.Window(fullscreen=True)
pyglet.gl.glClearColor(0.8, 0.8, 0.8, 0)
#p = Char()
m = Mapp("mapp.txt")
g = Gun()
fps = 120
window.set_mouse_visible(False)


@window.event
def on_key_press(symbol, modifiers):
    p.key_press(symbol)


@window.event
def on_key_release(symbol, modifiers):
    p.key_release(symbol)


@window.event
def on_mouse_motion(x, y, dx, dy):
    c.on_mouse_motion(x, y, dx, dy)
    g.on_mouse_motion(x, y, dx, dy)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        c.on_mouse_motion(x, y, dx, dy)


@window.event
def update(dt):
    p.update(dt)
    c.update()
    g.update()


@window.event
def on_draw():
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    window.clear()
    p.draw()
    c.draw()
    m.draw()
    g.draw()


pyglet.clock.schedule_interval(update, 1/fps)
pyglet.app.run()
