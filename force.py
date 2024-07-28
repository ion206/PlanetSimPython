import pygame as pyg
import math
MAX_MAG = 1000
BIG_G = (6.67430*math.pow(10,-11))
SCALAR = math.pow(10,17)
class Force:
    magnitude = 50
    degrees = 0
    target = None
    base = None
    

    def __init__(self, base, target):
        self.base = base
        self.target = target
        ## put formula here
        self.degrees = math.atan2((self.target.coords.x-self.base.coords.x),(self.target.coords.y-self.base.coords.y))
        self.magnitude = (BIG_G*self.base.mass*self.target.mass)/math.pow(base.coords.distance_to(target.coords),2)
        self.magnitude *= SCALAR
        if(self.magnitude > 1000):
            self.magnitude = 1000
        print(self.magnitude)

    def comp_form(self) -> pyg.math.Vector2:
        comp = pyg.math.Vector2(self.magnitude * math.sin(self.degrees),(self.magnitude * math.cos(self.degrees)))
        return comp
    
    def define(self):
        return ("I am the force at: " + str(self.base.coords.x) +" / "+ str(self.base.coords.y) + ", and am pointing at: " + str(self.target.coords.x) +" / "+ str(self.target.coords.y))