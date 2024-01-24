# Affichage du champ de charge électriques discrètes en 2D

# %%
from typing import TypeAlias

import numpy as np
from numpy import pi
from scipy.constants import epsilon_0
from matplotlib import pyplot as plt
from matplotlib import rcParams

# %%
rcParams['font.size'] = 14
vect2D: TypeAlias = (float, float)

class Charge:
   def __init__(self,position:vect2D,charge:float):
      self.x = position[0]
      self.y = position[1]
      self.q = charge

# %%

def calcul_E(x,y,charge:Charge):
   """ Defini des valeurs de champ électrique au point (x,y) pour une charge de
       magnitude 'q' positionné à (xq,yq)
   
       x,y peuvent être des array de même dimension, auquel cas les valeurs du
       champ sont calculé pour tout les couples de position 
   """
   
   r = np.sqrt( (x - charge.x)**2 + (y - charge.y)**2 )
   Ex = charge.q/4/pi/epsilon_0*(x-charge.x)/r**3
   Ey = charge.q/4/pi/epsilon_0*(y-charge.y)/r**3

   return Ex, Ey

def champ_charges(charges:list[Charge]):
   """ Calcul le champ vectoriel d'un ensemble de charges

       Placées dans un 'monde' allant de -1 à 1 en x et y
   """

   # Definissons le 'monde'
   x = np.linspace(-1,5,200)
   y = np.linspace(-2,2,200)
   X,Y = np.meshgrid(x,y)

   Ex = np.zeros(X.shape)
   Ey = np.zeros(Y.shape)

   # On calcul le champ pour chaque charge
   for c in charges:
      I, J = calcul_E(X,Y,c)
      # Selon le principe de superposition
      Ex += I
      Ey += J
   P = np.sqrt(Ex**2 + Ey**2) # magnitude du champ
   return X, Y, Ex, Ey, P

def affiche_E(charges:list[Charge],title="",saveName=None):
    """ calcul et affiche le champ """
    X, Y, Ex, Ey, P = champ_charges(charges)
   
    #Construisons la figure
    fig, ax = plt.subplots(figsize=(8,6))
    
    pax = ax.streamplot(X, Y, Ex, Ey, color=np.log(P), density=1.2 ,linewidth=2,\
                       cmap="winter", arrowsize=1.)
    for c in charges:
        ax.add_patch(plt.Circle((c.x, c.y), radius=0.05, color='k',zorder=20))
    ax.set_xlim([-1,5])
    ax.set_ylim([-2,2])
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_aspect('equal')
    plt.title(title)
    if saveName:
        f = plt.savefig(saveName)
    plt.show()
# %%

c = [Charge((2.5,1.8),1.5), Charge((0,1.2),0.3), Charge((2,-1.5),0.5), Charge((0.6,-1.2),-0.5)]
affiche_E(c)