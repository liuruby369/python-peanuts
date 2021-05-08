from pycat.sprite import Sprite
from pycat.window import Window

window=Window()
chick=window.create_sprite()
chick.image="chick-a.png"

chick.y=100

print("The sprite at position (",chick.x,chick.y,")",' has the image',chick.image)

x=input('Enter the x position: ')
print(x)
chick.x=int(x)

class Chick(Sprite):

    def on_create(self):
        self.image = 'chick-a.png'
        self.goto_random_position()


c1 = window.create_sprite(Chick)
c2 = window.create_sprite(Chick)



window.run()