#devoir 1/PHY-1007/Noah Banville et Olivier Lebel
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
   """ Calcul le champ vectoriel d'un ensemble de charges"""
   # Definissons le 'monde'
   x = np.linspace(-1,5,400)
   y = np.linspace(-2,2,400)
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

def magnitude_x(charges, y=0, z=0):
    """Calcul de la magnitude du champ électrique en fonction de x( question a) )."""
    x_val = np.linspace(0, 5, 400)
    magnitude_val = np.zeros_like(x_val)

    for i, x in enumerate(x_val):
        Ex, Ey = 0, 0
        for charge in charges:
            I, J = calcul_E(x, y, charge)
            Ex += I
            Ey += J
        magnitude_val[i] = np.sqrt(Ex**2 + Ey**2)

    return x_val, magnitude_val

def affiche_graph(charges:list[Charge],title="",saveName=None):
    """ calcul et affiche le champ """
    X, Y, Ex, Ey, P = champ_charges(charges)
   
    # figure des lignes de champs
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16,6))
    
    pax = ax1.streamplot(X, Y, Ex, Ey, color=np.log(P), density=1.2 ,linewidth=2,\
                       cmap="winter", arrowsize=1.)
    for c in charges:
        ax1.add_patch(plt.Circle((c.x, c.y), radius=0.05, color='k',zorder=20))
    ax1.set_xlim([-1,5])
    ax1.set_ylim([-2,2])
    ax1.set_xlabel(r'$x$')
    ax1.set_ylabel(r'$y$')
    ax1.set_aspect('equal')
    ax1.set_title("Lignes de champ des charges")
    
    #figure de la magnétude du champ selon x
    x_val, magnitude_val = magnitude_x(charges)
    ax2.plot(x_val, magnitude_val)
    ax2.set_xlabel(r'$x$')
    ax2.set_ylabel(r'Magnitude du champ électrique')
    ax2.set_title('Magnitude du champ électrique selon x')
    
    # Afficher la figure combinée
    plt.tight_layout()
    
    if saveName:
        plt.savefig(saveName)
    plt.show()

#charges utilisées pour l'exercice
c = [Charge((2.5,1.8),1.5), Charge((0,1.2),0.3), Charge((2,-1.5),0.5), Charge((0.6,-1.2),-0.5)]

#affiche les 2 graphs
affiche_graph(c)








