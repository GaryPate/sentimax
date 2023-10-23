FROM python:3.10.4

WORKDIR /models

COPY models/* ./
RUN apt-get update -y && apt-get install -y 
RUN pip3 install -r requirements.txt
RUN python -m textblob.download_corpora 


