# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 01:34:23 2022

@author: Uzivatel
"""
import os
os.chdir('c:\\Users\\Uzivatel\Desktop\Plasma')

import math

class Vector:

    def __init__(self, vector, dimension):
        self.vector = vector
        self.dimension = dimension
        
    def addition(self, another_vector):
        
        vector_addition = []
        
        for i in range(self.dimension):
            
            value = self.vector[i]+another_vector.vector[i]
            vector_addition.append(value)
        
        return vector_addition
    
    def multiplication_scalar(self, scalar):
        
        vector_mult_scal = []
        
        for i in range(self.dimension):
            
            value = self.vector[i]*scalar
            vector_mult_scal.append(value)
        
        return Vector(vector_mult_scal,self.dimension)
    
    def multiplication_vector(self, vA):
        
        vecteurB = [vA.vector[1]*self.vector[2]-vA.vector[2]*self.vector[1], vA.vector[2]*self.vector[0]-vA.vector[0]*self.vector[2],vA.vector[0]*self.vector[1]-vA.vector[1]*self.vector[0]]
        
        return vecteurB
    
    def norme_vector(self):
        
        norme_list = []
        
        for i in range(len(self.vector)):
            norme_list.append(self.vector[i])
        
        norme = 0
        for j in range(len(norme_list)):
            norme += norme_list[j]**2
        norme = math.sqrt(norme)

        return norme
        

    def interface():
        
        position = Vector([0,0,0],3)
    
        x = input("Zadejte počáteční pozici x ")
        y = input("Zadejte počáteční pozici y ")
        z = input("Zadejte počáteční pozici z ")
    
        x = int(x)
        y = int(y)
        z = int(z)
        position= Vector([x,y,z],3)
    
    
        vx = input("Zadejte počáteční rychlost x ")
        vy = input("Zadejte počáteční rychlost y ")
        vz = input("Zadejte počáteční rychlost z ")
    
        vx = int(vx)
        vy = int(vy)
        vz = int(vz)
    
        velocity = Vector([vx,vy,vz],3)
        
        mass = input("Určete hmotnost částice ")
        mass = int(mass)
        
        return position, velocity, mass
        
#Tests


# =============================================================================
# a = Vector([1,2,3],3)
# b = Vector([2,1,2],3)
# c = Vector([0,0,0],3)
# 
# c = a.addition(b)
# print(c)
# =============================================================================
# =============================================================================
# c = a.addition(b)
# d = a.multiplication_scalar(5)
#e = a.multiplication_vector(b)
#print(e)
# f = a.norme_vector()
# 
# =============================================================================



