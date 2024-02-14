#devoir 2 Electromagnetisme
# Noah Banville et Olivier Lebel

from typing import TypeAlias
import numpy as np
from numpy import pi, sqrt
from scipy.constants import epsilon_0
from numpy.polynomial import legendre
from matplotlib import pyplot as plt
from matplotlib import rcParams
#import math

vect3D: TypeAlias = (float, float, float)
class Charge:
   def __init__(self,position:vect3D,charge:float):
      self.x = position[0]
      self.y = position[1]
      self.z = position[2]
      self.q = charge

def exp_multipolaire(x, y, z, c):
    pot = np.zeros(7)
    
    for i in range(6):
        n = np.zeros(6)
        n[i] = 1
        for k in c:
            angle = (k.x*x + k.y*y + k.z*z)/(sqrt(k.x**2 + k.y**2 + k.z**2)*sqrt(x**2 + y**2 + z**2))
            legendre_terme = legendre.legval(angle, n, tensor=True)
            pot[i] += k.q * legendre_terme * (sqrt(np.absolute(k.x)**2 + np.absolute(k.y)**2 + np.absolute(k.z) **2))**i
        
        pot[i] *= (1/(4*pi*epsilon_0)) * (1/(sqrt(np.absolute(x)**2 + np.absolute(y)**2 + np.absolute(z)**2))**(i+1))
        pot[6] += pot[i]
    #Les 6 première cases du tableau sont les expansions pour n = 0, 1, 2, 3, 4, 5 et la dernière case est la somme des 6.
    return pot



def affiche_graph(c):

    # make data
    X, Y = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
    Z = np.zeros((201, 201))
    for i in np.arange(-100, 101):
        for j in np.arange(-100, 101):
            Z[i][j] = exp_multipolaire(i*(10**(-9)), j*(10**(-9)), 50*(10**(-9)), c)[1]
    levels = np.linspace(Z.min(), Z.max(), 100)

    # plot
    fig, ax1= plt.subplots(layout='constrained')

    cs = ax1.contourf(X, Y, Z, levels=levels)
    cbar = fig.colorbar(cs)

    ax1.set_xlabel("X [nm]")
    ax1.set_ylabel("Y [nm]")

    plt.show()
    
#charges utilisées pour l'exercice

c = [
Charge((5*(10**(-9)), 5*(10**(-9)), 0), 1.0*(10**(-12))), 
     Charge((-5*(10**(-9)), 5*(10**(-9)), 0), -1.0*(10**(-12))),
     Charge((5*(10**(-9)), -5*(10**(-9)), 0), -1.0*(10**(-12))), 
     Charge((-5*(10**(-9)), -5*(10**(-9)), 0), 1.0*(10**(-12)))
     ]

print(exp_multipolaire(43*(10**(-9)), 23*(10**(-9)), 50*(10**(-9)), c))
#affiche_graph(c)
