import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import jinja2
df = pd.read_csv("db1.csv")

#Paises que estan tramitando ciudadania en NZ
paises=df.groupby(by=["country_of_residence"]).count()
paises=paises.loc[paises["status"]>5500]
pais=paises.index.tolist()
cantidad=paises["status"].to_list()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(pais,cantidad)
plt.xticks(rotation=90)
plt.show()
plt.savefig('/var/output/residencia.png')
#Estado de la ciudadania
citizenship=df.groupby(by=["status"]).count()
#citizenship=citizenship.loc[citizenship["estimate"]]
aux=citizenship/(citizenship.iloc[0,0]+citizenship.iloc[1,0])*100
status=aux.index.tolist()
ciudadania=aux["estimate"].to_list()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(status,ciudadania)
plt.xticks(rotation=90)
plt.show()
plt.savefig('/var/output/ciudadania.png')
# Que tipo de visa y cuantas hay
visa=df.groupby(by=["visa"]).count()
visa=visa/np.sum(visa["status"].to_numpy())*100
tipo=visa.index.tolist()
cantidad=visa["status"].to_list()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(tipo,cantidad)
plt.xticks(rotation=90)
plt.show()
plt.savefig('/var/output/visa.png')
#Cuantos Estudiantes x pais hay
estudiantes=df.loc[df["visa"]=="Student"]
estudiantesporpais=estudiantes.groupby(by=["country_of_residence"]).count()
estudiantesporpais=estudiantesporpais.loc[estudiantesporpais["status"]>750]
pais=estudiantesporpais.index.tolist()
cantidad=estudiantesporpais["status"].to_list()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(pais,cantidad)
plt.xticks(rotation=90)
plt.show()
plt.savefig('/var/output/estudiantes.png')
#Cuantos Argentinos status de tramite
argentinos=df.loc[df["country_of_residence"]=="Argentina"]
argentinosfinalizado=argentinos.groupby(by=["status"]).count()
argentinosfinalizado=argentinosfinalizado/np.sum(argentinosfinalizado["estimate"].to_numpy())*100
tipo=argentinosfinalizado.index.tolist()
cantidad=argentinosfinalizado["estimate"].to_list()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(tipo,cantidad)
plt.xticks(rotation=90)
plt.show()
plt.savefig('/var/output/argentinos.png')