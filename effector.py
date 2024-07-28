import pygame as pyg
from force import Force
import math
import array as arr
from arrow import draw_arrow

MAX_VEL = 200

class Effector:
    coords = None #position
    color = (255, 0, 0)
    screen = None
    radius = 15
    mass = 5 # KG
    x_vel = 0 # x-velocity
    y_vel = 0 #y-velocity

    forces = []

    def __init__(self, screen, coords):
        self.coords = coords
        self.screen = screen
        self.forces = []
        self.mass = 0.5

    def grow(self, factor):
        self.radius += 5
        self.mass *= 2

    def add_forces(self, effectors):
        self.forces.clear()
        for eff in effectors:
            ## Magnitude must be calculated using Physics 1 calculations
            if(eff.coords != self.coords):
                ##  atan(y-difference / x-difference) -> Gives the relative angle
                self.forces.append(Force(self, eff))

    def show_forces(self, screen):
        draw_arrow(screen, self.coords, self.net_force()+self.coords, (0,255,0), 5, 8, 8)

    def show_all_forces(self, screen):
        for force in self.forces:
             draw_arrow(screen, self.coords, (force.comp_form()/4)+self.coords, (0,255,0), 5, 8, 8)


        
    def net_force(self):
        net = pyg.math.Vector2(0,0)
        for force in self.forces:
            net += force.comp_form() ##comp form gives the force's component form
        return net
    
    def move(self, timems):
        if(self.radius < 35):  
            time = timems/1000
            x_fac = (self.x_vel*time) + (0.5*(self.net_force().x/self.mass)*math.pow(time,2))
            y_fac = (self.y_vel*time) + (0.5*(self.net_force().y/self.mass)*math.pow(time,2))
            self.x_vel = x_fac/time
            self.y_vel = y_fac/time
            print("x" + str(self.x_vel))
            print("y" + str(self.y_vel))
            self.coords += pyg.math.Vector2(x_fac,y_fac)
        else:
            self.color = (0,120, 120)

    
        