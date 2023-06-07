FROM jupyter/all-spark-notebook

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG spark_work

RUN pip install findspark jupyterlab_theme_solarized_dark 

EXPOSE 8888
