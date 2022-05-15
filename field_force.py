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
    
    def __init__(self, charge,B, dimension, E, directionB, directionE):
        self.charge = charge
        self.B =B
        self.dimension = dimension
        self.E = E
        self.directionB = directionB
        self.directionE = directionE

        

    
    def homogenous_magnetic_force(self,velocity):  # B, direction and velocity are vectors. Charge is scalar (+ or -)
        
        B_x = 0
        B_y = 0
        B_z = 0
        
        direction = self.directionB
        
        if (direction==1):
            B_x = self.B
        if (direction==2):
            B_y = self.B
        if (direction==3):
            B_z = self.B
        Magnetic_field = Vector([B_x,B_y,B_z],3)
        
        Magnetic_field = Magnetic_field.multiplication_scalar(self.charge)

        Lorentz_force = Vector([0,0,0],3)
        
        Lorentz_force = Magnetic_field.multiplication_vector(velocity)

        
        return Vector(Lorentz_force,3)
    
    def homogenous_electric_force(self,direction):
        
        
        E_x = 0
        E_y = 0
        E_z = 0
        
        direction = self.directionE
        if (direction==1):
            E_x = self.E
        if (direction==2):
            E_y = self.E
        if (direction==3):
            E_z = self.E
        Electric_field = Vector([E_x,E_y,E_z],3)

        Lorentz_force = Vector([0,0,0],3)
        Electric_force = Electric_field.multiplication_scalar(self.charge)

        return Vector(Electric_force,3)

        
        
        
