from random import shuffle
import tkinter as tk

window = tk.Tk()
canWidth,canHeight = 1000, 1000
canvas = tk.Canvas(window, width=canWidth, height=canHeight, bg='light grey')
canvas.pack()

values = [i+(canWidth/canHeight) for i in range(canWidth)]
shuffle(values)

def drawLines(z):
    for i in range (len(z)):
        canvas.create_line(i, canHeight, i, canHeight-z[i], fill= 'black')

def render():
    global values
    canvas.delete("all")

    if not all(values[i] <= values[i+1] for i in range(len(values) - 1)):
        shuffle(values)
    drawLines(values)

    window.after(50, render)


render()
window.mainloop()