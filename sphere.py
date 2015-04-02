import math

class Sphere:
    def __init__(self,r=1,x=0,y=0,z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
    def get_volume(self):
        volume = (4.0/3.0)*math.pi*self.r**3
        return volume
    def get_square(self):
        s = 4*math.pi*self.r**2
        return s
    def get_radius(self):
        return self.r
    def get_center(self):
        return (self.x,self.y,self.z)
    def set_radius(self,r):
        self.r=r
    def set_center(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def is_point_inside(self,x,y,z):
        if math.sqrt((x-self.x)**2+(y-self.y)**2+(z-self.z)**2) < self.r:
            return True
        else:
            return False
        