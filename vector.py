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
            
            value = self.vector[i]+another_vector[i]
            vector_addition.append(value)
        
        return vector_addition
    
    def multiplication_scalar(self, scalar):
        
        vector_mult_scal = []
        
        for i in range(self.dimension):
            
            value = self.vector[i]*scalar
            vector_mult_scal.append(value)
        
        return vector_mult_scal
    
    def multiplication_vector(self, vA):
        
        vecteurB = [vA[1]*self.vector[2]-vA[2]*self.vector[1], vA[2]*self.vector[0]-vA[0]*self.vector[2],vA[0]*self.vector[1]-vA[1]*self.vector[0]]
        
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
        
        
#Tests


a = Vector([1,2,3],3)
b = [2,1,2]

c = a.addition(b)
d = a.multiplication_scalar(5)
e = a.multiplication_vector(b)
f = a.norme_vector()




