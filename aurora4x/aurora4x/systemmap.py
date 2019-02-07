
from celestialbody import CelestialBody
######################################################
class SystemMap:
    
    
    
    
    def __init__(self, **kwargs):        
        
        self.colors={"background":"#000040", 
                     "planets":"#00FF00",
                     "planets_text":"#FFFF00"}
        
        self.planets =[]
        self.asteroids=[]
        self.moons=[]
        
        
        self.x_offset=0
        self.y_offset=0
        
        self.offset=10
        
        #self.bind(pos=self.update_canvas)
        #self.bind(size=self.update_canvas)
        
        self.min_zoom=5.3
        self.max_zoom=100000
        self.current_zoom=1000
        
        
    def move_right(self, instance):
        self.x_offset-=self.offset
        self.update_canvas()
    
    def move_left(self, instance):
        self.x_offset+=self.offset
        self.update_canvas()
    
    def move_up(self, instance):
        self.y_offset-=self.offset
        self.update_canvas()
    
    def move_down(self, instance):
        self.y_offset+=self.offset
        self.update_canvas()
    
    def zoom_in(self, instance):
        self.current_zoom/=2
        self.update_planets_zoom()
        
    
    def zoom_out(self, instance):
        self.current_zoom*=2
        self.update_planets_zoom()
        
    
    def update_planets_zoom(self):
        for pl in self.planets:
            pl.set_zoom(self.current_zoom)
        for pl in self.asteroids:
            pl.set_zoom(self.current_zoom)
        for pl in self.moons:
            pl.set_zoom(self.current_zoom)
        self.update_canvas()
        
        
    def add_planet(self, name, r, b):
        self.planets.append(CelestialBody(name=name, r=r, b=b))
        
    def add_asteroid(self, name, r, b):
        self.asteroids.append(CelestialBody(name=name, r=r, b=b))
    
    
    
    def update_canvas(self, *args):
    #need to reset everything
        self.canvas.clear()
        
        centerx=self.width/2+self.x_offset
        centery=self.height/2+self.y_offset
        
        
        eigth=self.width/8
        
        
        with self.canvas:
            
            get_color(self.colors.get("background"))
            Rectangle(pos=self.pos, size=self.size)
        #context instruction
            Color(1,1,1,1)
        #vertex instruction
            Ellipse (pos = (centerx,centery), size=(10,10)) 
            
            Color(1,1,0,1)    
            simple_text("Sol", 12, centerx, centery+10)
            
            
            self.draworbit(self.planets, centerx, centery)
            self.drawbodies(self.asteroids, centerx, centery)
            
            #Draw bodies
            
            
            #!!!!!!!!!!!!!!!Problem words go on TOP so I need to store all xy coords a second time or just recompute each
            
                
            #for pl in self.planets:
                #simple_text(pl.name, 8, centerx+pl.getX_Coord(), centery+pl.getY_Coord()+5)
            
            
            
            
            
            simple_text("10 m km", 12, 10, 15)
            Line(points=[10,10,eigth+10,10], width=0.5)
######################################################

    def drawbodies(self, cbodies, centerx, centery):
        for pl in cbodies:
                Color(0,0,1,1)
                Ellipse (pos = (pl.getX_Coord()+centerx, pl.getY_Coord()+centery), size=(5,5))
                Color(1,1,0,1)
                simple_text(pl.name, 8, centerx+pl.getX_Coord(), centery+pl.getY_Coord()+5)

    
    def draworbit(self, cbodies,centerx, centery):   
        for pl in cbodies:
                print (pl.name)
                Color(0,1,0,1)
                Line(circle = (centerx+2.5, centery+2.5, pl.zoomr), width = 0.5)
                Color(0,0,1,1)
                Ellipse (pos = (pl.getX_Coord()+centerx, pl.getY_Coord()+centery), size=(5,5))
                Color(1,1,0,1)
                simple_text(pl.name, 8, centerx+pl.getX_Coord(), centery+pl.getY_Coord()+5)
        

    
    
    
    