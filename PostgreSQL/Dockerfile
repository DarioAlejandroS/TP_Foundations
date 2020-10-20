FROM postgres:9.6.19
ENV POSTGRES_PASSWORD=pos
ENV POSTGRES_USER=root
RUN mkdir /home/data
#COPY ./DATABASE.csv /home/data/
COPY ./db.sql /home/data/
COPY ./Script.sh /home/data/Script.sh