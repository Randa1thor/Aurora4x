
from math import sin, cos, radians




class CelestialBody:
	#for now 
	#constants earth sidereal year 1 = 365.25636
	#earth orbital distance = 149600 k km 
	#not a great way to do this but I don't know the best oop approach without a really long construction arg list
	
	#current zoom 10 m to 170 pixels
	
	def __init__(self, **kwargs):
		
		self.name=kwargs.get("name","--No Name--")
		self.r=kwargs.get("r",1)*149600
		self.b=kwargs.get("b",0)
		self.zoomr=self.r/1000# this needs to go somewhere else maybe.... maybe
		self.x_coord=sin(radians(self.b))*self.zoomr
		self.y_coord=cos(radians(self.b))*self.zoomr
		
	def set_zoom(self, zoom=1000):
		self.zoomr=self.r/zoom
		self.update_Coords()
		
		
	def setX_Coord( self ) :
		print (self.name + " " + str(self.b))
		self.x_coord= sin(radians(self.b))*self.zoomr
	
	def setY_Coord( self ) :
		self.y_coord= cos(radians(self.b))*self.zoomr
	
	def getX_Coord(self):
		return self.x_coord
	
	def getY_Coord(self):
		return self.y_coord
	
	def update_Coords(self):
		self.setX_Coord()
		self.setY_Coord()