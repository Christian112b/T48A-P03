# -*- coding: utf-8 -*-
"""Estadistica.ipynb

	Autor: Christian Aarón Zavala Sánchez
"""

import numpy as np

#Generar datos aleatorios para alturas y cintura
altura = np.random.normal(loc=1.65, scale=0.1, size=100)
cintura = np.random.normal(loc=80, scale=10, size=100)

#Crear el array de NumPy de dos dimensiones
datos_mexico = np.column_stack((altura, cintura))

import matplotlib.pyplot as plt

def genHistogram(data, bins, label, color):

  plt.hist(
    data,
    bins=bins,
    label=label,
    color=color,
    edgecolor='black',
    histtype='bar',
  )

  plt.legend(fontsize=10)
  plt.show()

genHistogram(data=datos_mexico[:,0], bins= 10, label='Cintura', color='red')
genHistogram(data=datos_mexico[:,1], bins= 10, label='Altura', color='blue')

