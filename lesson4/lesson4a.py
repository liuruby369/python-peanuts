from pycat.core import Window,Sprite
from pycat.keyboard import KeyCode
from pyglet import image

window = Window(background_image='img/sea.png')

class Player(Sprite):
    def on_create(self):
        self.image='img/ork1.png'
        self.scale=0.1
     
    def on_update(self, dt):
        self.move_forward(8)
        if window.is_key_up(KeyCode.UP):
            self.rotation = 90
        if window.is_key_down(KeyCode.LEFT):
            self.rotation = 180
        if window.is_key_down(KeyCode.RIGHT):
            self.rotation = 0
        if window.is_key_down(KeyCode.DOWN):
            self.rotation = 270
        
        if self.x > 1200:
            print('You win!')
            window.close()

        if self.is_touching_any_sprite():
            print('You lose!')
            window.close()



class RoundAndRound(Sprite):

    def on_create(self):
        self.image = 'owl.png'
        self.x = 800
        self.y = 500

    def on_update(self, dt):
        self.move_forward(5)
        self.rotation += 5







class UpAndDown(Sprite):

    def on_create(self):
        self.image = 'owl.png'
        self.x = 300
        self.y = 500
        self.rotation = 90

    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_window_edge():
            self.rotation += 90
        

class RubysEnemy(Sprite):

    def on_create(self):
        self.image = 'chick-a.png'
        self.x = 800
        self.y = 1000
        self.rotation = 180

    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_window_edge():
            self.rotation += 180




# s=window.create_sprite()
# s.x=500
# s.y=500
# s.image='img/beach.png'

window.create_sprite(Player)
window.create_sprite(UpAndDown)
window.create_sprite(UpAndDown, x=700)
window.create_sprite(UpAndDown, x=1000)
window.create_sprite(RoundAndRound)
window.create_sprite(RoundAndRound , x=600 , y=400)
window.create_sprite(RoundAndRound , x=900 , y=300)


# window.create_sprite(image='img/beach.png', x=400, y=500)
# window.create_sprite(image='img/beach.png', x=800, y=400)
# window.create_sprite(image='img/beach.png', x=1000, y=100)
# window.create_sprite(image='img/beach.png', x=400, y=100)
window.create_sprite(image='chick-a.png', x=400, y=100)


window.run()