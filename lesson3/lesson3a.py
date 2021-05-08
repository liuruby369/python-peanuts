from pycat.core import Window,Sprite, KeyCode


window = Window()

class Chick(Sprite):
    def on_create(self):
        self.image = 'chick-a.png'
        self.y = 50
        self.rotation=0

    



    def on_update(self, dt):
        
        if window.is_key_pressed(KeyCode.W):
            self.move_forward(50)

        
        
        if self.x > window.width:
            self.rotation = 90
            self.x -= 50
        if self.y > window.height:
            self.y -= 50
            self.rotation = 180
            
        if self.x > window.width:
            self.x -= 50
            self.rotation = 270
        
        if self.y > window.height:
            self.y -= 50
            self.rotation = 0
        


class Bear(Sprite):
    def on_create(self):
        self.image = 'bear-a.png'
        self.y = 400
        
     

    def on_update(self, dt):
        
        if window.is_key_up(KeyCode.E):
            self.x += 100
        
        if self.x > window.width:
            print('Bear won!')
            window.close() 


class Monster(Sprite):
    def on_create(self):
        self.image = '4.png'
        self.y = 100
        
     

    def on_update(self, dt):
        
        if window.is_key_down(KeyCode.R):
            self.x += 1
        
        if self.x > window.width:
            print('Monster won!')
            window.close() 




window.create_sprite(Chick)
window.create_sprite(Bear)
window.create_sprite(Monster)

window.run()