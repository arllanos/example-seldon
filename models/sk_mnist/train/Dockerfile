FROM python:2

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install libssl-dev

COPY /requirements.txt /tmp/
RUN cd /tmp && \
    pip install --no-cache-dir -r requirements.txt

RUN mkdir training
COPY ./create_model.py /training/create_model.py
COPY ./train.sh /training/train.sh
WORKDIR /training
RUN chmod 777 /training/train.sh

CMD ["/training/train.sh"]
