FROM ubuntu
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt-get update && \
    apt-get -y install python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000