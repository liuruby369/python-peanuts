from pycat.core import Window
window=Window()

chick=window.create_sprite()
chick.image="chick-a.png"
chick.x=90
chick.y=100

dot=window.create_sprite()
dot.image="dot-a.png"
dot.x=1170
dot.y=150


window.run()