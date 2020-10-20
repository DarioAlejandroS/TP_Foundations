#Crear imagen 
docker build -t posi .
docker build -t pythoni .
#Correr imagen
#docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
#--name "nombre" para setearle un nombre al container
#-e environment "variable" 
#-p expone puertos
#-d corre en backgroud
docker run --name posc -p 5432:5432 -d posi 
#Conectarse a la base
docker exec -it posc /bin/sh
# Crea base "db" despues de iniciar el container
docker exec -it psql psql -U postgres -c "CREATE DATABASE db;"
# Corre el Scipt de sql que crea la tabla
docker exec -it posc psql -U root -d db -f /home/data/db.sql