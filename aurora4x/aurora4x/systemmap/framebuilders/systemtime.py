import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as fnt


class TimeFrame(tk.LabelFrame):
  
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args,**kwargs)   
         
        self.initUI()

        
    def initUI(self):
        
        self.pad=1;
        
        icon=Image.new("RGB",(1,1))  
        
        ic=ImageTk.PhotoImage(icon)
        
        
        leftpadding=(10,0)
        rightpadding=(0,10)
        py=(0,5)
        
        time_increments=["5 secs", "30 secs", "2 min", "5 min", "20 min",   
                    "1 Hour", "3 Hours", "8 Hours", "1 Day", "5 Days", "30 Days"]
        
        helv10=fnt.Font(family="Helvetica", size=8, weight=fnt.BOLD)
        
        r=len(time_increments)-1
        
        for x in range(len(time_increments)):
            button1 = tk.Button( self, image=ic, compound="top", font=helv10, text = time_increments[x], bg="#00F000", height=15, width=25)
            button1.image=ic
            
            
            if x<r and x>0:             
                button1.pack(side="left", fill=None, expand=False, pady=py)
            elif x<1:
                button1.pack(side="left", fill=None, expand=False, padx=leftpadding, pady=py)
            else:
                button1.pack(side="left", fill=None, expand=False, padx=rightpadding, pady=py)
                
        
        