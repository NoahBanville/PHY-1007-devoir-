import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#Création du détecteur, nous allons dessiner la forme et faire l'initialisation des valeurs de départ. 

def champ_detecteur():
    #initialisation du détecteur
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
    for i in range(1000):
        for x in range(121):
            for y in range(61):
                if detecteur[y, x] != 0 and detecteur[y, x] != 50 and detecteur[y, x] != -300 :
                    if y == 30:
                        detecteur[y, x] = (detecteur[y, x+1] + detecteur[y, x-1])/2
                    else :
                        detecteur[y, x] = (detecteur[y+1, x] + detecteur[y-1, x] + detecteur[y, x+1] + detecteur[y, x-1])/4 + (detecteur[y+1, x] - detecteur[y-1, x])/(8*(30-y))
    

    #afficher détecteur
    masked_array = np.ma.masked_where(detecteur == 50, detecteur)
    cmap = matplotlib.cm.spring
    cmap.set_bad(color='white')
    plt.imshow( masked_array, cmap = 'plasma' )
    plt.colorbar()
    
    plt.show()


champ_detecteur()