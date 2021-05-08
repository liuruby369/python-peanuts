from pycat.core import Window,Sprite
from pycat.keyboard import KeyCode
from pyglet import image

window = Window(background_image='img/sea.png')

class Player(Sprite):
    def on_create(self):
        self.image='img/owl.png'
     
    def on_update(self, dt):
        self.move_forward(10)
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


s=window.create_sprite()
s.x=500
s.y=500
s.image='img/beach.png'

window.create_sprite(Player)

window.create_sprite(image='img/beach.png', x=400, y=500)
window.create_sprite(image='img/beach.png', x=800, y=400)
window.create_sprite(image='img/beach.png', x=1000, y=100)
window.create_sprite(image='img/beach.png', x=400, y=100)



window.run()