# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:39:11 2022

@author: Uzivatel
"""
import os
import math
os.chdir('c:\\Users\\Uzivatel\Desktop\Plasma')
import matplotlib.pyplot as plt

from vector import Vector
from Integrator import Integrator
from field_force import Field_force
from interface import Interface
from plot import Plot



# Test

#position= Vector([0,-2,0],3)
#velocity = Vector([0,2,0],3)


dt = 0.001

x = []
y = []
z = []

N = 20000

a = Vector([1,1,1],3)

values = Interface.create_particle()
position = values[0]
velocity = values[1]
mass = values[2]
charge = values[3]


values_field = Interface.create_elmag_field()

dimension = values_field[0]
E = values_field[1]
B = values_field[2]

for w in range(N):
    

    field = Field_force(3,B, E)  # self, dimension, charge, B , E
    acceleration = field.E_B_drift(mass, velocity, charge)
    
    position = Vector(Integrator.Euler(position,velocity,acceleration,dt)[0],3)
    velocity = Vector(Integrator.Euler(position,velocity,acceleration,dt)[1],3)

    x.append(Integrator.Euler(position,velocity,acceleration,dt)[0][0])
    y.append(Integrator.Euler(position,velocity,acceleration,dt)[0][1])
    z.append(Integrator.Euler(position,velocity,acceleration,dt)[0][2])
    

Plot.plot_drift(x,y,z,N,dt)

