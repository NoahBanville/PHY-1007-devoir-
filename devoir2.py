#devoir 2 Electromagnetisme
# Noah Banville et Olivier Lebel

from typing import TypeAlias
import numpy as np
from numpy import pi
from scipy.constants import epsilon_0
from numpy.polynomial import legendre
from matplotlib import pyplot as plt
from matplotlib import rcParams
import math

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
        A = 0
        for k in c:
            angle = (k.x*x + k.y*y + k.z*z)/(math.sqrt(k.x**2 + k.y**2 + k.z**2)*math.sqrt(x**2 + y**2 + z**2))
            legendre_terme = legendre.legval(angle, n)
            pot[i] += k.q * legendre_terme * (1/(np.sqrt(x**2 + y**2 + z**2))**(i+1)) * (np.sqrt(k.x**2 + k.y**2 + k.z **2))**i
            
        pot[i] *= (1/(4*np.pi*epsilon_0))
        pot[6] += pot[i]
    #Les 6 première cases du tableau sont les expansions pour n = 0, 1, 2, 3, 4, 5 et la dernière case est la somme des 6.
    return pot

def potentiel_E(x, y, z, charges):
    potentiel = 0
    for charge in charges:
        r = np.sqrt((x - charge.x)**2 + (y - charge.y)**2 + (z - charge.z)**2)
        potentiel += charge.q / (4 * pi * epsilon_0 * r)
    return potentiel

def affiche_graph(c):
    plt.style.use('_mpl-gallery-nogrid')

    # make data
    X, Y = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
    Z = np.zeros((201, 201))
    for i in np.arange(-100, 101):
        for j in np.arange(-100, 101):
            Z[i][j] = exp_multipolaire(i*(10**(-9)), j*(10**(-9)), 50*(10**(-9)), c)[4]
    levels = np.linspace(Z.min(), Z.max(), 100)

    # plot
    fig, ax1= plt.subplots(layout='constrained')

    cs = ax1.contourf(X, Y, Z, levels=levels)
    cbar = fig.colorbar(cs)

    ax1.set_xlabel("x [nm]")
    ax1.set_ylabel("y [nm]")

    plt.show()
    
#charges utilisées pour l'exercice
c = [Charge((5*(10**(-9)), 5*(10**(-9)), 0), 1.0*(10**(-12))), Charge((-5*(10**(-9)), 5*(10**(-9)), 0), -1.0*(10**(-12))), Charge((5*(10**(-9)), -5*(10**(-9)), 0), -1.0*(10**(-12))), Charge((-5*(10**(-9)), -5*(10**(-9)), 0), 1.0*(10**(-12)))]

print(exp_multipolaire(43*(10**(-9)), 23*(10**(-9)), 50*(10**(-9)), c))
#affiche_graph(c)
