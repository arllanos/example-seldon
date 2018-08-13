FROM arllanos/ie_base_image

COPY /requirements.txt /tmp/

RUN cd /tmp && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /microservice

EXPOSE 5000
CMD ["python","-u","microservice.py","MnistConsumer","REST","--service-type","MODEL","--persistence","0"]