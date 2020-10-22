# TP_Foundations
TP ITBA

# Resumen
Dada una base de datos, se ejecutó un pipeline en el cual se procesan los datos y se genera un reporte que responde a un posible conjunto de problemáticas determinadas por el autor.
A tal efecto, se tomó una base de datos de migraciones de Nueva Zelanda durante el mes de junio de 2020, que colecta datos respecto a los ingresos y egresos de tal país. Algunos datos importantes son: tipos de visa otorgadas, país de origen del migrante, entre otras cosas. Es posible acceder a dicha base a partir de el link:
https://www.stats.govt.nz/assets/Uploads/International-migration/International-migration-June-2020/Download-data/international-migration-June-2020-citizenship-by-visa-by-country-of-last-permanent-residence2.csv .<br/>
Se genero un container de PostgreSQL en Docker para albergar los datos y poder, eventualmente, administrarlos y manejarlos. Luego para poder hacer la ingesta de datos y enviarlos a la base de datos mencionada anteriormente, se creó una rutina en Python que permite tomar los datos desde la dirección de internet, crea y popula la base de datos en el container de PostgreSQL. Se consideró este camino por ser más eficiente dado que el archivo de origen es de tipo csv el cual trae información sobre las columnas. Haberlo creado a priori habría resultado en trabajo redundante, pues habría que haber cortado líneas en el archivo.<br/>
Una vez populada la base de datos se realizan las consultas cuyo reporte se extrae en el archivo _report.html_.

### Contenido:
La estructura de la solución es la siguiente:
            TP_FOUNDATIONS/
            |
             - PostgreSQL/
             - Python/
            docker-compose.yml
            Ejecutar Linux.sh
            Ejecutar Windows.bat
            README.md
En la carpeta PostgreSQL se encuentran los archivos necesarios para generar la imagen de Docker que contiene la base de datos en PostgreSQL.
* Dockerfile
En la carpeta Python se encuentran los archivos necesarios para generar la imagen Docker que contiene las rutinas para colectar la base de datos desde origen, popular la base de datos PostgreSQL y hacer las consultas. Adicionalmente, el template para el reporte también se encuentra en esta carpeta.
* Dockerfile
* datapro.py
* queries.py
* queries2.py
* server.py
* report.html
NOTA: el archivo _server.py_ permite que la ejecución se realice mediante un navegador, tal cual sería la situación en el caso de que se trabajara con servicios web. Para facilitar el trabajo el programa se ejecuta un GET REQUEST. En una situación más realista podría utilizarse una API POST con la base de datos deseada y cualquier comando de interés.    

### Pasos para ejecutar la solución:

1. Descargar las carpetas respetando la estructura mencionada en la sección anterior.
2. En BASH/PowerShell dirigirse a la carpeta TP_FOUNDATIONS. Dependiendo del sistema operativo debe hacerse lo siguiente:
    * Windows:
        Editar el archivo "Ejecutar Windows.bat" y modificar el valor de la variable _volumen_ por una ruta donde se montará un volumen para extraer los resultados. Por ejemplo: "C:/Users/Dario/Desktop/Vol"
    * Linux:
        Editar el archivo "Ejecutar Linux.sh" y modificar el valor de la variable _volumen_ por una ruta donde se montará un volumen para extraer los resultados. Por ejemplo: "/home/Test"
    NOTA: Los directorios deben estar creados antes de ejecutar los archivos por lotes.
3. Ejecutar el archivo "Ejecutar Windows/Linux.bat/sh"
4. Dirigirse a la ruta _volumen_ para extraer el informe y los gráficos.

Para consultas y/o sugerencias contactar a dario.sella@gmail.com