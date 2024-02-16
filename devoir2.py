#devoir 2 Electromagnetisme
# Noah Banville et Olivier Lebel

from typing import TypeAlias
import numpy as np
from numpy import pi, sqrt, dot
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

#xx
def exp_multipolaire(x, y, z, c):
    
    cst1 =(1/(4*pi*epsilon_0))
    R = sqrt(x**2 + y**2 + z**2)
    pot = np.zeros(7)
    
    for i in range(6):
        n = np.zeros(6)
        n[i] = 1
        for k in c:
            Rprime = (sqrt(k.x**2 + k.y**2 + k.z**2))
            angle = ((dot(x,k.x) + dot(y,k.y) + dot(z,k.z)))/(Rprime)/R
            pot[i] += k.q * legendre.legval(angle, n, tensor=True) * (Rprime)**i
        
        pot[i] *= cst1 * (1/(R)**(i+1))
        pot[6] += pot[i]
    #Les 6 première cases du tableau sont les expansions pour n = 0, 1, 2, 3, 4, 5 et la dernière case est la somme des 6.
    return pot
####


def affiche_graph_a1(c,saveName=None):
    fig, axs = plt.subplots(2, 3, figsize=(12, 8), gridspec_kw={'hspace': 0.3, 'wspace': 0.2}, sharex='col', sharey='row')
    fig.suptitle("Figures des premiers termes de l'expansion multipolaire", fontsize=12)
     # Crée une grille de sous-graphiques 2x3
    
    for i, ax in enumerate(axs.flat):  # Itère sur les sous-graphiques
        X, Y = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
        Z = np.zeros((201, 201))
        for j in range(-100, 101):
            for k in range(-100, 101):
                Z[j+100][k+100] = exp_multipolaire(j*(10**(-9)), k*(10**(-9)), 50e-9, c)[i]  # Utilise i pour accéder à chaque terme de l'expansion
        #levels = np.linspace(Z.min(), Z.max(), 100)
        cs = ax.contourf(X, Y, Z, levels=100)
        ax.set_title(f'Terme {i}')
        fig.colorbar(cs, ax=ax)
        ax.set_xlabel("X [nm]")
        ax.set_ylabel("Y [nm]")

    plt.tight_layout()  # Ajuste automatiquement l'espacement entre les sous-graphiques
    if saveName:
        plt.savefig(saveName)
    plt.show()

def affiche_graph_a2(c, saveName = None):
    X, Y = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
    Z = np.zeros((201, 201))
    for i in np.arange(-100, 101):
        for j in np.arange(-100, 101):
            Z[i+100][j+100] = exp_multipolaire(i*(10**(-9)), j*(10**(-9)), 50e-9, c)[6]
    levels = np.linspace(Z.min(), Z.max(), 100)
    fig, ax1= plt.subplots(layout='constrained')
    cs = ax1.contourf(X, Y, Z, levels=100)
    ax1.set_title("Figure de la somme des 6 premiers termes de l'expansion multipolaire", fontsize=12)
    fig.colorbar(cs, ax=ax1)
    ax1.set_xlabel("X [nm]")
    ax1.set_ylabel("Y [nm]")  
    if saveName:
        plt.savefig(saveName)
    plt.show()


def affiche_graph_b1(c, saveName = None):
    pass

def affiche_graph_b2(c, saveName = None):
    pass

    
# Charges 
c = [
    Charge((5e-9, 5e-9, 0), 1.0e-12),
    Charge((-5e-9, 5e-9, 0), -1.0e-12),
    Charge((5e-9, -5e-9, 0), -1.0e-12),
    Charge((-5e-9, -5e-9, 0), 1.0e-12)
]

print(exp_multipolaire(43e-9, 23e-9, 50e-9, c))
affiche_graph_a1(c)  #  (compilation +- 40s)
