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
    pot = [0, 0, 0, 0, 0, 0, 0]
    
    for i in range(6):
        pot[i] += (1/(np.sqrt(x**2 + y**2 + z**2))**(i+1))
        n = [0, 0, 0, 0, 0, 0]
        n[i] = 1
        for k in c:
            angle = (k.x*x + k.y*y + k.z*z)/(math.sqrt(k.x**2 + k.y**2 + k.z**2)*math.sqrt(x**2 + y**2 + z**2))
            pot[i] *= ((np.sqrt(k.x**2 + k.y**2 + k.z**2))**i) * (legendre.legval(angle, n)) * k.q
        pot[i] *= (1/(4*np.pi*epsilon_0))
        pot[6] += pot[i]
    #Les 6 première cases du tableau sont les expansions pour n=0, 1, 2, 3, 4, 5 et la dernière case est la somme des 6. 
    return pot

def potentiel_E(x, y, z, charges):
    potentiel = 0
    for charge in charges:
        r = np.sqrt((x - charge.x)**2 + (y - charge.y)**2 + (z - charge.z)**2)
        potentiel += charge.q / (4 * pi * epsilon_0 * r)
    return potentiel

#charges utilisées pour l'exercice
c = [Charge((5, 5, 0), 1.0), Charge((-5, 5, 0), -1.0), Charge((5, -5, 0), -1.0), Charge((-5, -5, 0), 1.0)]
