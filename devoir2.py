#devoir 2 Electromagnetisme
# Noah Banville et Olivier Lebel

from typing import TypeAlias
import numpy as np
from numpy import pi
from scipy.constants import epsilon_0
from numpy.polynomial import legendre
from matplotlib import pyplot as plt
from matplotlib import rcParams


from scipy.integrate import quad


vect3D: TypeAlias = (float, float, float)
class Charge:
   def __init__(self,position:vect3D,charge:float):
      self.x = position[0]
      self.y = position[1]
      self.z = position[2]
      self.q = charge
      
"""def potentiel_E(x, y, z, charges):
    potentiel = 0
    for charge in charges:
        r = np.sqrt((x - charge.x)**2 + (y - charge.y)**2 + (z - charge.z)**2)
        potentiel += charge.q / (4 * pi * epsilon_0 * r)
    return potentiel"""

#charges utilisées pour l'exercice
c = [Charge((5, 5, 0), 1.0), Charge((-5, 5, 0), -1.0), Charge((5, -5, 0), -1.0), Charge((-5, -5, 0), 1.0)]

def exp_multipolaire():
   pass
      


#Devoir d'onde : 
A = 0.1
E = 0.5
def integrand(x, a):
   return np.absolute(a*np.cos(10 * np.sqrt(2) * x))
for i in range(96): 
   Ef = 0.981 * (quad(integrand, 0, np.pi/16, args=(A)))[0]
   E = E - Ef
   A = np.sqrt((E*2)/100)
   if (i+1)*(1/16) %1 == 0 : 
      print("(",  (i+1)*(1/16), "pi, ", A, ")")