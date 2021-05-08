from pycat.core import Window, Sprite, AudioLoop, Player
from random import shuffle
from typing import List

from pycat.geometry import point


window = Window(draw_sprite_rects=True, background_image='forest_04.png')
click_sprite : List['Card']= []
music = AudioLoop("LoopLivi.wav")
music.play()
hit_card = Player('hit.wav')
laugh = Player('laugh.wav')
pointe = Player('point.wav')


class Button(Sprite):

    def on_create(self):
        self.y = 300
        self.x = 1050
        self.image = 'button.png'
    def on_left_click(self):
         if len(click_sprite) == 2:
            a = click_sprite[0]
            b = click_sprite[1]
            if a.image == b.image:
                a.is_rotion = True
                b.is_rotion = True
                print('you have a match')
                pointe.play(  )
            else:
                a.is_visible = False
                b.is_visible = False
                laugh.play()

            click_sprite.clear()



class Card(Sprite):

    def on_create(self):
        self.y = 500
        self.is_visible = False
        self.is_rotion = False
    def on_left_click(self):
        if len(click_sprite) < 2:

            self.is_visible = True
            if self not in click_sprite:
                click_sprite.append(self)
                hit_card.play()

    def on_update(self, dt):
        if self.is_rotion:
            self.rotation += 10
            if self.rotation > 270:
                self.delete()      
            

       
for y in range(150,200,75):
        
    img_list = 2 *['1.png','2.png','3.png','4.png']
    shuffle(img_list)
    for i in range(len(img_list)):
        card = window.create_sprite(Card)
        card.x = 100 + i*100
        card.y = y
        card.image = img_list.pop()

for i in range(4, 18, 3):
    print(i)
window.create_sprite(Button)
window.run() 