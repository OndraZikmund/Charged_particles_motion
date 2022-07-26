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
    
    def __init__(self, dimension,B,E):
        
        self.dimension = dimension
        self.B = B
        self.E = E
        

# =============================================================================
#         self.directionG = directionG
#         self.G = G
# =============================================================================
        
    
    def homogenous_magnetic_force(self,velocity, charge):  # B, direction and velocity are vectors. Charge is scalar (+ or -)
        
        Magnetic_field = self.B
        
        Magnetic_field = Magnetic_field.multiplication_scalar(charge) 

        Lorentz_force = Vector([0,0,0],3)
        
        Lorentz_force = Magnetic_field.multiplication_vector(velocity)

        
        return Vector(Lorentz_force,3)
    
    def homogenous_electric_force(self, charge):
        
        
        Electric_field = self.E

        Lorentz_force = Vector([0,0,0],3)
        Electric_force = Electric_field.multiplication_scalar(charge)

        return Vector(Electric_force,3)
    
    def E_B_drift(self, mass,velocity, charge):
        
        Lorentz_force = self.homogenous_magnetic_force(velocity, charge)
        acceleration = Lorentz_force.multiplication_scalar(1/mass)
        acceleration = acceleration.addition(self.homogenous_electric_force(charge).vector)
        acceleration = Vector(acceleration,3)
        
        return acceleration
        
        
