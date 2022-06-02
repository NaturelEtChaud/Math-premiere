#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:20:55 2022

@author: laurent chaudet
"""

import matplotlib.pyplot as plt

annees = [1900+i for i in range(0,111,5)]
vraies_donnees = [44.8 ,47 ,50.7, 53.4 ,55.9 ,59.7 ,64.5, 69.3, 73.1, 72.4 ,83.6, 87.9,92.5, 98.8, 104.7, 111.9, 116.8, 120.8, 123.5, 125.6, 126.9, 127.4, 128.6]


# le modèle
annees_modele = [1900+i for i in range(50,111,5)]
v50 = 83.6
q = 1.011151
v_modele = [v50*q**(i-50) for i in range(50,111,5)]

v73 = v50*q**(73-50)

##############
# le graphique
##############

# les dimensions du graphique
plt.figure(1, figsize=(12, 8))

# la courbe de l'évolution de la population réelle
plt.plot(annees, vraies_donnees, label="population réelle")

# la courbe du modèle géométrique à partir de 1950
plt.plot(annees_modele, v_modele, 'r*', label="population modélisée")

# l'année 1973 d'après le modèle
plt.plot(1973, v73, 'g*', label="année 1973 d'après le modèle")

# les titres
plt.xlabel('années')
plt.ylabel('population exprimée en million')
plt.title("évolution de la population Japonaise")
plt.legend()

# on trace le graphique
plt.plot()

# on enregistre le résultat sous la forme d'une image
plt.savefig("population_japon.png")

