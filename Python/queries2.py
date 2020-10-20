# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:00:42 2020

@author: Dario
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("db1.csv")

#Paises que estan tramitando ciudadania en NZ
paises=df.groupby(by=["country_of_residence"]).count()

plt.bar()
plt.show()

#Estado de la ciudadania
citizenship=df.groupby(by=["status"]).count()

plt.bar()
plt.show()

# Que tipo de visa y cuantas hay
visa=df.groupby(by=["visa"]).count()

plt.bar()
plt.show()

#Cuantos Estudiantes x pais hay
estudiantes=df.loc[df["visa"]=="Student"]
estudiantesporpais=estudiantes.groupby(by=["country_of_residence"]).count()

plt.bar()
plt.show()

#Cuantos Argentinos status de tramite
argentinos=df.loc[df["country_of_residence"]=="Argentina"]
argentinosfinalizado=argentinos.groupby(by=["status"]).count()

plt.bar()
plt.show()