# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:39:41 2022

@author: Uzivatel
"""

import os
import math
os.chdir('c:\\Users\\Uzivatel\Desktop\Plasma')
import matplotlib.pyplot as plt

from vector import Vector
from Integrator import Integrator


position= Vector([0,0,0],3)
velocity = Vector([0,0,0],3)
acceleration= Vector([0,0,-9.8],3)

dt = 0.1


z = []

for w in range(100):
    position = Vector(Integrator.Euler(position,velocity,acceleration,dt)[0],3)
    velocity = Vector(Integrator.Euler(position,velocity,acceleration,dt)[1],3)
    
    z.append(Integrator.Euler(position,velocity,acceleration,dt)[0][2])

T = [t*dt for t in range(100)]

plt.plot(T,z)