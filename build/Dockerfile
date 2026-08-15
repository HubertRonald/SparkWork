ARG BASE_IMAGE=quay.io/jupyter/all-spark-notebook:00987883e58d
FROM ${BASE_IMAGE}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /tmp/sparkwork-requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/sparkwork-requirements.txt

WORKDIR /home/jovyan/work
EXPOSE 8888 4040
