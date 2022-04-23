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
    
    def __init__(self, charge,B, dimension):
        self.charge = charge
        self.B =B
        self.dimension = dimension

    
    def homogenous_magnetic_force(self,velocity, direction):  # B, direction and velocity are vectors. Charge is scalar (+ or -)
        
        B_x = 0
        B_y = 0
        B_z = 0
        direction = 1
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
   

# Test

position= Vector([0,0,0],3)
velocity = Vector([0,0,1],3)
acceleration= Vector([0,0,-9.8],3)

dt = 0.001
mass = 1

y = []
z = []

N = 10000
for w in range(N):
    
    field = Field_force(1,2,3)
    
    Lorentz_force = field.homogenous_magnetic_force(velocity,1)
    acceleration = Lorentz_force.multiplication_scalar(1/mass)
    position = Vector(Integrator.Euler(position,velocity,acceleration,dt)[0],3)
    velocity = Vector(Integrator.Euler(position,velocity,acceleration,dt)[1],3)
    
    y.append(Integrator.Euler(position,velocity,acceleration,dt)[0][1])
    z.append(Integrator.Euler(position,velocity,acceleration,dt)[0][2])

    
T = [t*dt for t in range(N)]

plt.plot(y,z)  
    
