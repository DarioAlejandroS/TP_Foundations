vol1=/home/dario/Desktop/Files
cd PostgreSQL
docker build -t posi .
cd ..
cd Python
docker build -t pythoni .
cd ..
docker volume create --driver local --opt type=none --opt device=$vol1 --opt o=bind myvolume
docker-compose up -d
curl http://localhost:5000