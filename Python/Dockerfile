#publicly available docker image "python" on docker hub will be pulled

FROM amancevice/pandas:1.1.3

ENV FLASK_ENV=development

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install python-csv
RUN pip install regex
RUN pip install sqlalchemy
RUN pip install sqlalchemy-utils
RUN pip install psycopg2
RUN pip install kaggle

RUN mkdir /home/data
RUN mkdir /var/Output

COPY datapro.py /home/datapro.py
COPY server.py /home/server.py

ENTRYPOINT ["python", "/home/server.py"]
