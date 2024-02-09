#devoir 2 Electromagnetisme
# Noah Banville et Olivier Lebel

from typing import TypeAlias
import numpy as np
from numpy import pi
from scipy.constants import epsilon_0
from matplotlib import pyplot as plt
from matplotlib import rcParams

vect3D: TypeAlias = (float, float, float)
class Charge:
   def __init__(self,position:vect3D,charge:float):
      self.x = position[0]
      self.y = position[1]
      self.z = position[2]
      self.q = charge

#charges utilisées pour l'exercice
c = [Charge((5, 5, 0), 1.0), Charge((-5, 5, 0), -1.0), Charge((5, -5, 0), -1.0), Charge((-5, -5, 0), 1.0)]