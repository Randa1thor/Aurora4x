import tkinter as tk
from PIL import Image, ImageTk

class TopButtonFrame(tk.Frame):
  
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args,**kwargs)   
         
        self.initUI()

        
    def initUI(self):
        
        self.pad=1;
        
        icon=Image.open("./gui/images/buttons/blank.png")
        ic=ImageTk.PhotoImage(icon)
        
        
        
        for x in range(27):
                      
            button1 = tk.Button( self, image=ic,text = str(x), height=25, width = 25, bg="#000040")
            button1.image=ic
            button1.pack(side="left", fill=None, expand=False)
                
        