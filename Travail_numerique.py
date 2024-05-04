import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Initialisation du détecteur
detecteur = np.full((61, 121), 50.0)
for i in range(30, 121):
    detecteur[0, i] = -300
    detecteur[60, i] = -300
for i in range(1, 60):
    detecteur[i, 120] = 0
for i in range(45, 120):
    detecteur[30, i] = 0
for i in range(0, 30):
    detecteur[i, 30-i] = -300
    detecteur[60-i, 30-i] = -300
detecteur[30, 0] = -300
for i in range(1, 30):
    for j in range(31-i, 120):
        detecteur[i, j] = -150
for i in range(31, 60):
    for j in range(-29+i, 120):
        detecteur[i, j] = -150
for i in range(1, 45):
    detecteur[30, i] = -150

#Calculer le potentiel
différence = 0.001

for i in range(1000000):
    a = detecteur[45, 38]
    for x in range(121):
        for y in range(61):
            if detecteur[y, x] != 0 and detecteur[y, x] != 50 and detecteur[y, x] != -300 :
                if y == 30:
                    detecteur[y, x] = (detecteur[y, x+1] + detecteur[y, x-1])/2
                else :
                    detecteur[y, x] = (detecteur[y+1, x] + detecteur[y-1, x] + detecteur[y, x+1] + detecteur[y, x-1])/4 + (detecteur[y+1, x] - detecteur[y-1, x])/(8*(30-y))
    if (abs(a-detecteur[45,38]))*100 < différence and i > 100:
        #afficher détecteur

        masked_array = np.ma.masked_where(detecteur == 50, detecteur)
        cmap = matplotlib.cm.spring
        cmap.set_bad(color='white')
        plt.imshow( masked_array, cmap = 'plasma' )
        plt.colorbar()
        plt.title(f'Potentiel dans le détecteur [r-z]  ({i} itérations)')
        plt.xlabel("z [1e-4 m]")
        plt.ylabel('r [1e-4 m]')
        plt.show()
        break