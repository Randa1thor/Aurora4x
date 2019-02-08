import tkinter as tk
from aurora4x.systemmap.framebuilders.systemtime import TimeFrame
from aurora4x.systemmap.framebuilders.topbuttonframe import TopButtonFrame
from aurora4x.systemmap.framebuilders.systempulse import PulseFrame
from aurora4x.systemmap.framebuilders.tabbedframes.displayframe import DisplayFrame
from aurora4x.systemmap.framebuilders.tabbedframes.bodyinfo import BodyInfoFrame


from tkinter import font as fnt
from tkinter import Frame
import tkinter.ttk as ttk
import aurora4x


root=tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0, bg="#000040")
canvas.pack(fill=tk.BOTH, expand=True)

bg_color="#000060"







topframe=TopButtonFrame(root, bg=bg_color)
topframe.configure(bg=bg_color)
topframe_window = canvas.create_window(0, 5, anchor=tk.NW, window=topframe)



helv10=fnt.Font(family="Helvetica", size=5, weight=fnt.BOLD)


timeframe=TimeFrame(root, font=helv10, foreground="#FFFF00", text="Increment Time [Time will increase by the specified amount and pause]", bg=bg_color)
timeframe.configure(bg=bg_color)
timeframe_window = canvas.create_window(0, 40, anchor=tk.NW, window=timeframe)


pulseframe=PulseFrame(root, font=helv10, foreground="#FFFF00", text="Sub pulse Length: The length of each movement sub-pulse within each time increment."
                                     +" Automatic allows Aurora to select a suitable sub-pulse length", bg=bg_color)
pulseframe.configure(bg=bg_color)
pulseframe_window = canvas.create_window(0, 90, anchor=tk.NW, window=pulseframe)


book_x=[0,15,30]
book_y=[140,160,180]

notebookwidth=215

bgcolor="#ECE9D8"

n=ttk.Notebook(root)

display=DisplayFrame(n, bg=bgcolor)

n.add(display, text="Display")

bodyinfo=BodyInfoFrame(n, bg=bgcolor)

bodyinfo.pack(fill=tk.BOTH, expand=True)

n.add(bodyinfo, text="Body Info")
n.add(Frame(root), text="All Bodies")

n.configure(width=notebookwidth)

display_window=canvas.create_window(book_x[2], book_y[2], anchor=tk.NW, window=n, width=notebookwidth)

n=ttk.Notebook(root)

n.add(Frame(root), text="Sensors")
n.add(Frame(root), text="Waypoints")
n.add(Frame(root), text="Contacts")

display_window=canvas.create_window(book_x[1], book_y[1], anchor=tk.NW, window=n, width=notebookwidth)

n=ttk.Notebook(root)

n.add(Frame(root), text="Military")
n.add(Frame(root), text="Minerals")
n.add(Frame(root), text="Display2")


display_window=canvas.create_window(book_x[0], book_y[0], anchor=tk.NW, window=n, width=notebookwidth)




canvas.create_line(0,0,30,30, fill="red")
canvas.create_line(50,10,100,100, fill="blue")

canvas.create_oval(150,150,125,145, fill="#00FF00");


root.mainloop()

