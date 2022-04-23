# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:23:35 2022

@author: Uzivatel
"""

import os
import math
os.chdir('c:\\Users\\Uzivatel\Desktop\Plasma')

from vector import Vector



class Integrator:

    def Euler(position,velocity,acceleration, dt):
        
        change_position = velocity.multiplication_scalar(dt)
        change_velocity = acceleration.multiplication_scalar(dt)
        
        position = position.addition(change_position)
        velocity = velocity.addition(change_velocity)
        
        return position, velocity


#Test

position= Vector([1,1,1],3)
velocity = Vector([1,1,1],3)
acceleration= Vector([1,1,1],3)

dt = 0.1

change_position = Integrator.Euler(position, velocity, acceleration,dt)
print(change_position)
