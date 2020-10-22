:: Cambiar la variable vol1 por una ruta local donde se alojaran los archivos
set vol1=C:/Users/Dario/Desktop/Vol
cd PostgreSQL
docker build -t posi .
cd ..
cd Python
docker build -t pythoni .
cd ..
docker volume create --driver local --opt type=none --opt device=%vol1% --opt o=bind myvolume
docker-compose up -d
start http://localhost:5000