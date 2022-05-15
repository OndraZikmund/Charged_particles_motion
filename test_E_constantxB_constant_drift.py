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


# Test

position= Vector([0,-2,0],3)
#velocity = Vector([0,10,0.5],3)
velocity = Vector([0,2,0],3)


dt = 0.001
mass = 1

x = []
y = []
z = []

N = 20000
for w in range(N):
    
    field = Field_force(1,2,3,1,3,2)  # self, charge,B, dimension, E, directionB, directionE
    
    Lorentz_force = field.homogenous_magnetic_force(velocity)
    acceleration = Lorentz_force.multiplication_scalar(1/mass)
    acceleration = acceleration.addition(field.homogenous_electric_force(2).vector)
    acceleration = Vector(acceleration,3)
    
    
    position = Vector(Integrator.Euler(position,velocity,acceleration,dt)[0],3)
    velocity = Vector(Integrator.Euler(position,velocity,acceleration,dt)[1],3)

    x.append(Integrator.Euler(position,velocity,acceleration,dt)[0][0])
    y.append(Integrator.Euler(position,velocity,acceleration,dt)[0][1])
    z.append(Integrator.Euler(position,velocity,acceleration,dt)[0][2])
    
    if (w%100==0):
        print(Integrator.Euler(position,velocity,acceleration,dt)[0][0])
    
T = [t*dt for t in range(N)]

plt.plot(y,z, color  = "green")  

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.title("Drift ve zkříženém elektromagnetickém poli")

plt.xlabel("axe x")
plt.ylabel("axe y")

plt.xlim([0, 10])
plt.ylim([-5, 5])

ax.plot3D(x, y, z, 'blue')

print("poloha x",x[0])
