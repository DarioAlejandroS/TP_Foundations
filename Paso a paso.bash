#Crear imagen 
docker build -t posi .
docker build -t pythoni .
#Correr imagen
docker run --name posc -p 5432:5432 -d posi
docker run --name pythonc -p 5000:5000 -d pythoni
#Conectarse a la base
docker exec -it posc /bin/sh
# Crea base "db" despues de iniciar el container
docker exec -it psql psql -U postgres -c "CREATE DATABASE db;"
# Corre el Scipt de sql que crea la tabla
docker exec -it posc psql -U root -d db -f /home/data/db.sql