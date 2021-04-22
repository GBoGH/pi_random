import tkinter as tk

import random
import math
from tkinter.constants import CURRENT


screen_width = 500
screen_height = 500
r = 200

PI = 3.14159265358979323846264338327

canvas = tk.Canvas(width=screen_width, height=screen_height)
canvas.pack()

canvas.create_oval(50,50,450,450, width=2)
canvas.create_rectangle(50,50,450,450, width=2)

in_circle = 0
in_square = 0

best_pi = 0


def is_in_circle(x, y):
    distance = math.sqrt((250-x)**2 + (250-y)**2)
    if distance <= 200:
        return True
    return False

while True:
    x = random.randrange(0,500000000000000)/1000000000000
    y = random.randrange(0,500000000000000)/1000000000000
    if is_in_circle(x,y):
        in_circle += 1
    if (50 <= x <= 450) and (50 <= y <= 450):
        in_square += 1

    canvas.create_oval(x-1,y-1,x+1,y+1, fill="red")
    canvas.update()

    if in_square == 0:
        continue

    pi = (in_circle/in_square)*4
    smallest_difference = abs(PI - best_pi)
    difference = abs(PI-pi)

    if difference < smallest_difference:
        smallest_difference = difference
        best_pi = pi
        print(best_pi)

tk.mainloop()
