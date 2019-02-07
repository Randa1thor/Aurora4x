import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, background="bisque")
canvas.pack(side="bottom", fill="both", expand=True)

canvas.create_text(10, 30, anchor="sw", tags=["event"])
canvas.create_text(10, 30, anchor="nw", tags=["cget"])

def show_width(event):
    canvas.itemconfigure("event", text="event.width: %s" % event.width)
    canvas.itemconfigure("cget", text="winfo_width: %s" % event.widget.winfo_width())

canvas.bind("<Configure>", show_width)

root.mainloop()