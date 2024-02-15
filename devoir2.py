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
    def __init__(self, position: vect3D, charge: float):
        self.position = np.array(position)
        self.q = charge

def exp_multipolaire(x, y, z, c):
    pot = np.zeros(7)
    xyz_norm = np.linalg.norm([x, y, z])
    
    for i in range(6):
        n = np.zeros(6)
        n[i] = 1
        
        legendre_values = legendre.legval(
            np.sum(np.array([k.position for k in c]) * [x, y, z], axis=1) /
            (np.linalg.norm([k.position for k in c], axis=1) * xyz_norm),
            n,
            tensor=True
        )
        
        pot[i] = np.sum([charge.q * legendre_value * np.linalg.norm(charge.position)**i for charge, legendre_value in zip(c, legendre_values)])
        
    pot[:6] *= (1 / (4 * pi * epsilon_0)) * (1 / xyz_norm**(np.arange(1, 7)))
    pot[6] = np.sum(pot[:6])
    
    return pot



def affiche_graph(c):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10), constrained_layout=True)

    X, Y = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
    Z = np.zeros((201, 201, 6))

    for i in range(1,6):
        for j in np.arange(-100, 101):
            for k in np.arange(-100, 101):
                Z[j][k][i] = exp_multipolaire(j*(10**(-9)), k*(10**(-9)), 50*(10**(-9)), c)[i]

        levels = np.linspace(Z[:, :, i].min(), Z[:, :, i].max(), 100)
        ax = axs[i // 3][i % 3]
        cs = ax.contourf(X, Y, Z[:, :, i], levels=levels)
        fig.colorbar(cs, ax=ax)
        ax.set_xlabel("X [nm]")
        ax.set_ylabel("Y [nm]")
        ax.set_title(f"Terme {i}")

    fig.suptitle("Figures pour les termes de l’expansion multipolaire dans le plan x-y quand z = 50 nm")
    plt.show()
    
#charges utilisées pour l'exercice
c = [
    Charge((5e-9, 5e-9, 0), 1.0e-12),
    Charge((-5e-9, 5e-9, 0), -1.0e-12),
    Charge((5e-9, -5e-9, 0), -1.0e-12),
    Charge((-5e-9, -5e-9, 0), 1.0e-12)
]
print(exp_multipolaire(43e-9, 23e-9, 50e-9, c))

#prends plus de temps car les 6 graphs affichent dans la meme fenetre
affiche_graph(c)
