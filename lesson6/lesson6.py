from pycat.base.base_sprite import RotationMode
from pycat.core import Window,Sprite,Scheduler
from random import choice

w=Window(background_image='underwater_04.png')
label=w.create_label()
label.text='score: 0'
label.x = 200



class SpaceShip(Sprite):

    def on_create(self):
        self.image = 'saucer.png'
        self.x = 200
        self.y = 500
        
        self.scale = 0.2
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.score = 0

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.rotation+=180

class Alien(Sprite):
    def on_create(self):
        self.image = choice(['1.png','2.png','3.png','4.png','5.png'])
        self.scale = 0.3
        self.x = 0
        self.y = 50
        self.clicked = False

        self.x_speed = 5
        self.y_speed = 20
    def on_left_click(self):
        self.clicked = True

    def on_update(self, dt):
        if self.clicked:
            self.y += 10
            if self.y>w.height:    
                self.delete()
            if self.is_touching_sprite(s):
                self.delete()
                s.score += 1
                label.text='score: ' + str(s.score)
        else:        
            self.x += self.x_speed
            self.y += self.y_speed
            self.y_speed -= 5
            if self.y < 100:
                self.y_speed = 20
            if self.x > w.width:
                self.delete()
def create_alien(dt):
    w.create_sprite(Alien)

Scheduler.update(create_alien, 0.5)
w.create_sprite(Alien)
s=w.create_sprite(SpaceShip)
w.run()