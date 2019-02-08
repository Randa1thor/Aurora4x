import tkinter as tk
import tkinter.ttk as ttk

root=tk.Tk()

canvas = tk.Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0, bg="#000040")
canvas.pack(fill=tk.BOTH, expand=True)

notebookwidth=215

bgcolor="#ECE9D8"

tabs1=ttk.Notebook(canvas)

frame=tk.Frame(tabs1)

tree=ttk.Treeview( frame, columns=('Name', 'Info'), show="tree", displaycolumns=[0,1])

tree.column('#0', stretch=tk.YES, minwidth=0,width=0)
tree.column('#1', stretch=tk.YES)
tree.column('#2', stretch=tk.YES)

# Initialize the counter
i = 0
s=["Name","Venus","Body Type","Terrestrial Planet","Diameter","12104 km","Orb Distance","108m km","Gravity","0.91"]
        
for x in range(0, len(s), 2):
    tree.insert('', 'end', text="Item_"+str(i), values=(s[x], s[x+1]))
    # Increment counter
    i = i + 1 
        
tree.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH, expand=True)
#tree.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
frame.pack(side="left", anchor=tk.NW, fill=tk.BOTH, expand=True)
tabs1.add(frame, text="Body Info")
tabs1.pack(side="left", anchor=tk.NW, fill=tk.BOTH, expand=True)
display_window=canvas.create_window(10, 10, anchor=tk.NW, window=tabs1, width=notebookwidth)

root.mainloop()
