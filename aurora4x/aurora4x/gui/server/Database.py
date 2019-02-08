import sqlite3





def get_celestial_bodies():
    conn = sqlite3.connect('../server/db1.sqlite3')
    c = conn.cursor()
    c.execute('SELECT Name, OrbitalDistance, Bearing, OrbitNumber, BodyClass FROM SystemBody WHERE SystemID=1050 AND OrbitNumber=0 OR PlanetNumber=100 OR PlanetNumber=101 ORDER BY PlanetNumber ASC')
    dataset=c.fetchall()     
    conn.close()
    
    return dataset