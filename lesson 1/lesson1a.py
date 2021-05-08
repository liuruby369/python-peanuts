from pycat.core import Window
answer=input('waiting for you: ')
window=Window()
animal=window.create_sprite()
animal.x=80
animal.y=100

if answer == "chick":
    animal.image="chick-a.png"
    
if answer == "dot": 
    animal.image="dot-a.png"

answer=input('big or small: ')

if answer=='big':
    animal.scale=2

if answer=='small':
    animal.scale=0.5


window.run()