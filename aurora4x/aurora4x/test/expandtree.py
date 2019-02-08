#! coding=utf-8
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack(fill=tk.BOTH,expand=True)

tree.insert("", index="end",iid="Main", text="main branch", open=False)
tree.insert("Main", index="end", text="Stuff 1")
tree.insert("Main", index="end", text="Stuff 2")

root.mainloop()