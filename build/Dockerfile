FROM jupyter/all-spark-notebook

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG spark_work

WORKDIR ${spark_work}
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8888
