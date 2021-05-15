from pycat.core import Window,Sprite
import random
from typing import List
w = Window()
class Particle(Sprite):

    def on_create(self):
        self.scale = 5
        self.goto_random_position()
        self.rotation = random.randint(0,360)
        

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.rotation += 180

class ColorButton (Sprite):

    def on_create(self):
        self.y = 100
        self.scale = 50

    def on_left_click(self):
        for i in range(len(p)):
            p[i].color = self.color

class CreatButton(Sprite):

    def on_left_click(self):
        for i in range(50):
            p.append(w.create_sprite(Particle))

class Button(Sprite):

    def on_left_click(self):
        for i in range(len(p)):
            p[i].delete()

    



    



blue = w.create_sprite(ColorButton)
blue.color = (0,0,255)
blue.x = 200

green = w.create_sprite(ColorButton)
green.color = (0,255,0)
green.x = 250

red = w.create_sprite(ColorButton)
red.color = (255,0,0)
red.x = 150

p: List[Particle] = []
for i in range(50):
    p.append(w.create_sprite(Particle))

s = w.create_sprite(CreatButton)
s.scale = 50
s.y = 500
s.x = 100

c = w.create_sprite(Button)
c.scale = 50
c.x = 200
c.y = 500

w.run()