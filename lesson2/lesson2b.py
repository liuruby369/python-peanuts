from pycat.base.color import Color
from pycat.sprite import Sprite
from pycat.window import Window
from pyglet.gl.glext_arb import GL_FONT_HEIGHT_NV
from random import randint
window=Window()


class Chick(Sprite):

    def on_create(self):
        self.image = 'chick-a.png'
        self.goto_random_position()
        self.opacity = 500
        self.scale = 1
        self.rotation = randint(0, 360)


# c1 = window.create_sprite(Chick)
# c2 = window.create_sprite(Chick)

for i in range(1000):
    e = window.create_sprite(Chick)
    e.opacity = 200
    e.scale = 2
    e.color = Color.RED

window.run()