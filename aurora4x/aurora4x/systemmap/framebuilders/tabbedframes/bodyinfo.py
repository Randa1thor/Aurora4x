import tkinter as tk 
import tkinter.ttk as ttk


class BodyInfoFrame(tk.Frame):
  
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args,**kwargs)   
         
        self.initUI()

        
    def initUI(self):
        
        self.tree = ttk.Treeview( self, columns=('Dose', 'Modification date'))
        
        
    
        self.tree.column('#0', stretch=tk.YES, minwidth=0, width=0)
        self.tree.column('#1', stretch=tk.YES, width=110)
        self.tree.column('#2', stretch=tk.YES, width=110)
        #self.tree.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.treeview = self.tree
        # Initialize the counter
        self.i = 0
        s=["Name","Venus","Body Type","Terrestrial Planet","Diameter","12104 km","Orb Distance","108m km","Gravity","0.91"]
        
        for x in range(0, len(s), 2):
            self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(s[x], s[x+1]))
            # Increment counter
            self.i = self.i + 1 
        
        self.tree.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH, expand=True)



