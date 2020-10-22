set volumen=C:/Users/Dario/Desktop/Vol
cd PostgreSQL
docker build -t posi .
cd ..
cd Python
docker build -t pythoni .
cd ..
docker volume create --driver local --opt type=nfs--opt device=:%volumen% myvolume
docker-compose up -d
start http://localhost:5000