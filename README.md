[![Apache Spark](https://img.shields.io/static/v1?style=flat-square&message=Apache+Spark&color=E25A1C&logo=Apache+Spark&logoColor=FFFFFF&label=)](https://archive.apache.org/dist/spark/)
[![Jupyter](https://img.shields.io/static/v1?style=flat-square&message=Jupyter&color=F37626&logo=Jupyter&logoColor=FFFFFF&label=)](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
[![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)](https://www.python.org/dev/peps/pep-0537/#schedule-first-bugfix-release)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/jupyter/all-spark-notebook/tags?page=2)
![GitHub last commit](https://img.shields.io/github/last-commit/hubertronald/TemplateDockerDjango?style=flat-square)
[![MIT](https://img.shields.io/github/license/hubertronald/TemplateDockerDjango?style=flat-square)](LICENSE)


# SparkWork
Puedes correr un ambiente standalone de spark en local


# Inicio

Una vez se clone el proyecto

```bash
git clone https://github.com/HubertRonald/SparkWork.git
``` 

Luego habilita los siguientes scripts de bash para que puedan ser ejecutados:

```bash
chmod +x start.sh stop.sh
```

Después asegurase de tener **docker encendido**

Se puede iniciar rápidamente desde la terminal con (desde la carpeta `SparkWork`):

```bash
./start.sh
```

Copia el siguiente enlace

![](./src/url_notebook.png)

Si en caso no apareciera en los logs, intentar los siguiente:

```bash
docker-compose logs
```

Asimismo asegurarse de no tener abierto alguna sesión previa. Caso contratio cerrar esa pestaña del navegador y ejecutar nuevamente el script `./start.sh` en la terminal.

Hecho lo anterior en la parte izquierda, se verá el notebook [Spark_DataFrames_Ejemplo.ipynb](work/Spark_DataFrames_Ejemplo.ipynb)

![](./src/notebook.png)

# Datos Zip Code
El archivo [zipcodesUSDummy](./work/data/zipcodeUSDummy.json) es una pequeña muestra tomada de [US-Zip-Codes-JSON](https://github.com/millbj92/US-Zip-Codes-JSON/tree/master). Creditos a [Brandom Miller](https://brandonmiller.io)

# Enlaces

- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)

- [Specific Docker Image Options](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/specifics.html#specific-docker-image-options)

- [US-Zip-Codes-JSON](https://github.com/millbj92/US-Zip-Codes-JSON/tree/master)

# .gitignore

Fue generado en [gitignore.io](https://www.toptal.com/developers/gitignore/) con los filtros `python`, `macos`, `windows` y consumido mediante su API como archivo crudo desde la terminal:

```bash
curl -L https://www.toptal.com/developers/gitignore/api/python,macos,windows > .gitignore
```


# Autores
---
* **Hubert Ronald** - *Trabajo Inicial* - [HubertRonald / SparkWork](https://github.com/HubertRonald/SparkWork)

Ve también la lista de [contribuyentes](https://github.com/HubertRonald/SparkWork/contributors) que participaron en este proyecto.



# Licencia
---
Este proyecto está bajo licencia MIT - ver la [LICENCIA](LICENSE) archivo (en inglés) con más detalles