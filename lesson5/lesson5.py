from pycat.core import Window, KeyCode, Scheduler
from pycat.sprite import Sprite
from random import randint

window = Window(background_image="img/beach_03.png", draw_sprite_rects=True)


class Player(Sprite):
    def on_create(self):
        self.image='img/cat.png'
        self.x=100
        self.y=80

    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.LEFT):
            self.x -= 5
        if window.is_key_pressed(KeyCode.RIGHT):
            self.x += 5

class Gem(Sprite):
     def on_create(self):
        self.image='img/gem_shiny01.png'
        self.y = window.height
        self.x = randint(0,window.width)
        self.scale=0.5

     def on_update(self, dt):
        self.y -= 10
        if self.y < 5:
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()




player = window.create_sprite(Player)

def create_gem(dt):
    window.create_sprite(Gem)

Scheduler.update(create_gem, 2)

window.run()