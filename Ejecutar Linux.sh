$volumen=/home/
cd PostgreSQL
docker build -t posi .
cd ..
cd Python
docker build -t pythoni .
cd ..
docker volume create --driver local --opt type=nfs--opt device=:$volumen myvolume
docker-compose up -d
sensible-browser http://localhost:5000