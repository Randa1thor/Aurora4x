from tkinter import *

root = Tk()
root.configure(bg="blue")
canvas = Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0, bg="#000040")
canvas.pack()

canvas.create_line(0,0,30,30, fill="red")
canvas.create_line(50,10,100,100, fill="blue")

canvas.create_oval(150,150,125,145, fill="#00FF00");

quit = Button(root, text='Quit', command=root.quit)
quit.pack(side="left")

root.mainloop()