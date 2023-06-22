FROM jupyter/all-spark-notebook

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG user_root
ARG user
ARG password

# user root: sudo -s
# RUN sudo -s
# RUN sudo apt-get update && sudo apt-get upgrade
# RUN sudo apt install -y netcat
# RUN su ${user}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8888
