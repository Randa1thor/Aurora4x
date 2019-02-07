import tkinter as tk
import tkinter.ttk as ttk

class DisplayFrame(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args,**kwargs)   
         
        self.initUI()

        
    def initUI(self):
        
        
        
        
        
        
        
        s_bodies=["Planets","Moons", "Asteroids","Jump Pts"]
        self.s_bodies_var=[tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1)]        
        
        system_bodies=tk.LabelFrame(self, text="System Bodies", bg="#ECE9D8")
        
        
        self.fillLabelFrame(system_bodies, s_bodies, self.s_bodies_var)
        
        #system_bodies.pack(side="left", fill=None, expand=False,anchor=tk.NW)
        system_bodies.grid(row=0, column=0)
        
        
        
        s_orbitpath=["Stars","Planets", "Moons","Asteroids"]
        self.s_orbitpath_var=[tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar()]        
        
        system_bodies=tk.LabelFrame(self, text="Orbital Paths", bg="#ECE9D8")
        
        self.fillLabelFrame(system_bodies, s_orbitpath, self.s_orbitpath_var)
        
        #system_bodies.pack(side="left", fill=None, expand=False,anchor=tk.NW)
        system_bodies.grid(row=0, column=1)
        
        s_names=["Stars","Planets", "Moons","Asteroids"]
        self.s_names_var=[tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1)]        
        
        system_bodies=tk.LabelFrame(self, text="Names", bg="#ECE9D8")
        
        self.fillLabelFrame(system_bodies, s_names, self.s_names_var    )
        
        #system_bodies.pack(side="left", fill=None, expand=False,anchor=tk.NW)
        system_bodies.grid(row=1, column=0)
        
        
        
        
        s_objects=["Fleets","Move Tail", "Colonies","Comet Path"]
        self.s_objects_var=[tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar()]        
        
        system_bodies=tk.LabelFrame(self, text="Objects", bg="#ECE9D8")
        
        self.fillLabelFrame(system_bodies, s_objects, self.s_objects_var   )
        
        #system_bodies.pack(side="left", fill=None, expand=False,anchor=tk.NW)
        system_bodies.grid(row=1, column=1)
        
        
        
        combobox=ttk.Combobox(self)
        combobox.grid(row=2, column=0, columnspan=2)
        
        
        
        
        s_options=["Center On Selected Objects","Show JP Survey Locations", "Show Way Point Locations",
                   "Show Next Order", "Show Order Time and Distance", "Show Fleet/Contact Heading", "Show Events",
                   "Show Mineral Packets", "Show Lifepods", "Show Wrecks", "Highlight Own Colonies", "Hyper Limit"]
        self.s_options_var=[tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=0),
                            tk.IntVar(value=0),tk.IntVar(value=0),tk.IntVar(value=1),tk.IntVar(value=1),tk.IntVar(value=1),
                            tk.IntVar(value=0),tk.IntVar(value=0),]        
        
        system_bodies=tk.LabelFrame(self, text="Options", bg="#ECE9D8")
        
        self.fillLabelFrame(system_bodies, s_options, self.s_options_var   )
        
        #system_bodies.pack(side="left", fill=None, expand=False,anchor=tk.NW)
        system_bodies.grid(row=3, column=0, columnspan=2)
        
        
        
    
    def fillLabelFrame(self, parent, cbx_text, cbx_var):
        
        for x in range(len(cbx_text)):
            checkbox=tk.Checkbutton(parent, text=cbx_text[x], variable=cbx_var[x], bg="#ECE9D8", highlightthickness=0)
            checkbox.pack(side="top", fill=None, expand=False, anchor=tk.W)
        
        
        