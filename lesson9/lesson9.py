from pycat.base import image
from pycat.core import Window,Sprite

w = Window()
# image_list = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
image_list = ['1.jpg','2.jpg','3.jpg']
text_list = ['bus','bus stop','bus stop_2']
w.background_image = image_list[0]
label = w.create_label()
label.text = text_list[0]
class Button(Sprite):

    def on_create(self):
        self.image = "button_next.png"
        self.scale = 0.8
        self.x = w.width/2
        self.y = self.height/2
        self.c = 0
    def on_left_click(self):
        self.c += 1
        if self.c == len(image_list):
            w.close()
            return
        w.background_image = image_list[self.c]
        label.text = text_list[self.c]

class ThunmbsUp(Sprite):

    def on_create(self):
        self.image = 'thumbs_up.png'
        self.x = 0.75*w.width
        self.scale = 0.5
        self.y = 500
    def on_left_click(self):
        print('Good')



class ThunmbsDown(Sprite):

    def on_create(self):
        self.image = 'thumbs_up.png'
        self.rotation = 180
        self.x = 0.25*w.width
        self.scale = 0.5
        self.y = 500
    def on_left_click(self):
        print('Bad')

        

w.create_sprite(ThunmbsUp)

w.create_sprite(ThunmbsDown)
w.create_sprite(Button)
w.run()