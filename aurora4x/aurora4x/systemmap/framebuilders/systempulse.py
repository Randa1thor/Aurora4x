import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as fnt


class PulseFrame(tk.LabelFrame):
  
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
        
        pulse_increments=["Auto","5 sec", "30 sec","2 min", "5 min", "20 min", "1 Hour","6 Hours", "1 Day"]
        
        helv10=fnt.Font(family="Helvetica", size=8   , weight=fnt.BOLD)
        
        r=len(pulse_increments)-1
        
        for x in range(len(pulse_increments)):
            button1 = tk.Button( self, image=ic, compound="top", font=helv10, text = pulse_increments[x], bg="#00F000", height=15, width=25)
            button1.image=ic
            
            
            if x>0:             
                button1.pack(side="left", fill=None, expand=False, pady=py)
            else:
                button1.pack(side="left", fill=None, expand=False, padx=leftpadding, pady=py)
                
                
                
        pulse=tk.Label(self, text="Automatic Sub-Pulses", font=helv10, wraplength=75, justify=tk.CENTER, bg="#000060", fg="#00F000")
        
        pulse.pack(side="left", fill=None, expand=False)
            
                
        
        