#./Dockerfile
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

ADD requirements.txt ./
# RUN apt-get install -y --no-install-recommends \
#     default-libmysqlclient-dev

RUN pip install -r requirements.txt

# RUN pip install -r requirements.txt
# COPY . .

