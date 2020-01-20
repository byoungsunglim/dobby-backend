from tkinter import *
master = Tk()

canvas_width = 960
canvas_height = 540
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height,
           bg="white")
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="black")

mainloop() 
