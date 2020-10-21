FROM amancevice/pandas:1.1.3

ENV FLASK_ENV=development

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install python-csv
RUN pip install regex
RUN pip install sqlalchemy
RUN pip install sqlalchemy-utils
RUN pip install psycopg2

RUN mkdir /var/output

COPY datapro.py /home/datapro.py
COPY server.py /home/server.py
COPY queries.py /home/queries.py
COPY queries2.py /home/queries2.py
COPY report.html /home/report.html

ENTRYPOINT ["python", "/home/server.py"]