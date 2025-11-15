FROM selenium/node-chrome:latest

USER root

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pytest selenium

WORKDIR /tests
COPY ../tests /tests

CMD ["sleep", "infinity"]
