 # -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:02:04 2022

@author: Uzivatel
"""

import os
import math
os.chdir('c:\\Users\\Uzivatel\Desktop\Plasma')
import matplotlib.pyplot as plt

from vector import Vector
from Integrator import Integrator

class Field_force:
    
    def __init__(self, dimension, charge, B , E, G, directionG):
        self.charge = charge
        self.B =B
        self.dimension = dimension
        self.E = E

        self.directionG = directionG
        self.G = G
        

        

    
    def homogenous_magnetic_force(self,velocity):  # B, direction and velocity are vectors. Charge is scalar (+ or -)
        
        B_x = self.B[0]
        B_y = self.B[1]
        B_z = self.B[2]
        
        Magnetic_field = Vector([B_x,B_y,B_z],3)
        
        Magnetic_field = Magnetic_field.multiplication_scalar(self.charge)

        Lorentz_force = Vector([0,0,0],3)
        
        Lorentz_force = Magnetic_field.multiplication_vector(velocity)

        
        return Vector(Lorentz_force,3)
    
    def homogenous_electric_force(self):
        
        
        E_x = self.E[0]
        E_y = self.E[1]
        E_z = self.E[2]
        
        Electric_field = Vector([E_x,E_y,E_z],3)

        Lorentz_force = Vector([0,0,0],3)
        Electric_force = Electric_field.multiplication_scalar(self.charge)

        return Vector(Electric_force,3)
    
    def homogenous_gravity_force(self,mass):
        
        G_x = 0
        G_y = 0
        G_z = 0
        
        direction = self.directionG
        if (direction==1):
            G_x = self.G
        if (direction==2):
            E_G = self.G
        if (direction==3):
            E_G = self.G
        Gravity_field = Vector([G_x,G_y,G_z],3)

        Lorentz_force = Vector([0,0,0],3)
        Gravity_force = Gravity_field.multiplication_scalar(mass)

        return Vector(Gravity_force,3)
    
    def E_B_drift(self, mass,velocity):
        
        Lorentz_force = self.homogenous_magnetic_force(velocity)
        acceleration = Lorentz_force.multiplication_scalar(1/mass)
        acceleration = acceleration.addition(self.homogenous_electric_force().vector)
        acceleration = Vector(acceleration,3)
        
        return acceleration
