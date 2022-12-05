from turtle import Screen
from gameplay import Marker


# Game Screen
window = Screen()
window.setup(824, 768)
window.title("Tic Tac Toe")
window.bgpic('bg.png')


# Turtle
tom = Marker()
window.onscreenclick(tom.draw_location)
window.mainloop()
