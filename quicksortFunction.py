from random import shuffle
import tkinter as tk
import threading as thr
import time

window = tk.Tk()
canWidth,canHeight = 500,500
canvas = tk.Canvas(window, width=canWidth, height=canHeight, bg='light grey')
canvas.pack()

values = [i+(canWidth/canHeight) for i in range(canWidth)]
shuffle(values)

def drawLines(z):
    for i in range (len(z)):
        canvas.create_line(i, canHeight, i, canHeight-z[i], fill= 'black')

def quicksort(z, start, end, depth = 0):
    if end - start < 1:
        return
    
    pivot = z[end]

    i, j = start, end

    while i < j:
        while i < j and z[i] < pivot:
            i += 1
        while i < j and z[j] > pivot:
            j -= 1

        if i < j:
            z[i], z[j] = z[j], z[i]
            time.sleep(0.01)

            if z[i] < pivot:
                i += 1
            if z[j] > pivot:
                j -= 1

    quicksort(z, start, z.index(pivot) - 1, depth + 1)
    quicksort(z, z.index(pivot) + 1, end, depth + 1)

    return z

def render():
    canvas.delete("all")

    drawLines(values)

    window.after(16, render)

quicksortThread = thr.Thread(target=quicksort, args=(values, 0, len(values)-1))
quicksortThread.start()

render()
window.mainloop()