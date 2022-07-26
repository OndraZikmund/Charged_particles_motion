# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:10:23 2022

@author: Uzivatel
"""

from vector import Vector 
    
class Interface:
    
    def __init__(self, a):
        self.a = a
        
        
    def create_particle():
        
        position = Vector([0,0,0],3)
    
        x = input("Zadejte počáteční pozici x ")
        y = input("Zadejte počáteční pozici y ")
        z = input("Zadejte počáteční pozici z ")
    
        x = float(x)
        y = float(y)
        z = float(z)
        position= Vector([x,y,z],3)

        vx = input("Zadejte počáteční rychlost vx ")
        vy = input("Zadejte počáteční rychlost vy ")
        vz = input("Zadejte počáteční rychlost vz ")
    
        vx = float(vx)
        vy = float(vy)
        vz = float(vz)
    
        velocity = Vector([vx,vy,vz],3)
        
        mass = input("Určete hmotnost částice ")
        mass = float(mass)
        
        charge = input("Určete elektrický náboj částice ")
        charge = float(charge)
        
        return position, velocity, mass, charge
    
    
    def create_elmag_field():
        
            dimension = 3
            
            Ex = input("Zadejte x-ovou složku elektrického pole ")
            Ey = input("Zadejte y-ovou složku elektrického pole ")
            Ez = input("Zadejte z-ovou složku elektrického pole ")
            
            electric_field = Vector([float(Ex), float(Ey), float(Ez)], dimension)
            
            Bx = input("Zadejte x-ovou složku magnetického pole ")
            By = input("Zadejte y-ovou složku magnetického pole ")
            Bz = input("Zadejte z-ovou složku magnetického pole ")
            
          #  magnetic_field = Vector([float(Bx), float(By), float(Bz)], dimension)
            magnetic_field = Vector([float(Bx), float(By), float(Bz)], dimension)
        
            return dimension, electric_field, magnetic_field
    
    