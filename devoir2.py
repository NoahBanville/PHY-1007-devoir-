#devoir 2 Electromagnetisme
# Noah Banville et Olivier Lebel

from typing import TypeAlias
import numpy as np
from numpy import pi, sqrt
from scipy.constants import epsilon_0
from numpy.polynomial import legendre
from matplotlib import pyplot as plt

vect3D: TypeAlias = (float, float, float)

class Charge:
    def __init__(self, position: vect3D, charge: float):
        self.position = np.array(position)
        self.q = charge

def exp_multipolaire(x, y, z, c):
    pot = np.zeros(7)
    sqrt_abs_x = sqrt(np.abs(x))
    sqrt_abs_y = sqrt(np.abs(y))
    sqrt_abs_z = sqrt(np.abs(z))
    sqrt_abs_xyz = sqrt_abs_x**2 + sqrt_abs_y**2 + sqrt_abs_z**2
    
    for i in range(6):
        n = np.zeros(6)
        n[i] = 1
        for k in c:
            angle = (k.position[0]*x + k.position[1]*y + k.position[2]*z) / \
                    (sqrt(k.position[0]**2 + k.position[1]**2 + k.position[2]**2) * sqrt_abs_xyz)
            legendre_terme = legendre.legval(angle, n, tensor=True)
            pot[i] += k.q * legendre_terme * (
                                                sqrt(np.abs(k.position[0])**2 + 
                                                     np.abs(k.position[1])**2 + 
                                                     np.abs(k.position[2])**2
                                                     ))**i
        
        pot[i] *= (1/(4*pi*epsilon_0)) * (1/sqrt_abs_xyz)**(i+1)
        pot[6] += pot[i]
    
    return pot

def affiche_graph(c):
    X, Y = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
    Z = np.zeros((201, 201, 6))

    for i in range(1,6):
        for j in np.arange(-100, 101):
            Z[i][j] = exp_multipolaire(i*(10**(-9)), j*(10**(-9)), 50*(10**(-9)), c)[1]
    levels = np.linspace(Z.min(), Z.max(), 100)

    fig, ax1 = plt.subplots()
    cs = ax1.contourf(X, Y, Z, levels=levels)
    cbar = fig.colorbar(cs)

    ax1.set_xlabel("X [nm]")
    ax1.set_ylabel("Y [nm]")

    plt.show()
    
# Charges used for the exercise
c = [
    Charge((5*(10**(-9)), 5*(10**(-9)), 0), 1.0*(10**(-12))), 
    Charge((-5*(10**(-9)), 5*(10**(-9)), 0), -1.0*(10**(-12))),
    Charge((5*(10**(-9)), -5*(10**(-9)), 0), -1.0*(10**(-12))), 
    Charge((-5*(10**(-9)), -5*(10**(-9)), 0), 1.0*(10**(-12)))
]

print(exp_multipolaire(43*(10**(-9)), 23*(10**(-9)), 50*(10**(-9)), c))
affiche_graph(c)  # Uncomment to display the graph
