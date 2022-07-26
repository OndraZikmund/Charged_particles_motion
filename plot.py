# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:18:00 2022

@author: Uzivatel
"""

import matplotlib.pyplot as plt

class Plot:

    def plot_drift(x,y,z, N,dt):
        

        T = [t*dt for t in range(N)]
        
        plt.plot(y,z, color  = "green")  
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        plt.title("Drift ve zkříženém elektromagnetickém poli")
        
        plt.xlabel("axe x")
        plt.ylabel("axe y")
        
# =============================================================================
#         plt.xlim([0, 10])
#         plt.ylim([-5, 5])
# =============================================================================
        
        ax.plot3D(x, y, z, 'blue')
        
        pass
        
  