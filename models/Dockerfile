FROM python:3.10.4

WORKDIR /

# creating the file to write XComs to
RUN mkdir -p airflow/xcom
RUN echo "" > airflow/xcom/return.json

COPY models/* ./
RUN apt-get update -y && apt-get install -y \
    && google-cloud-sdk \
RUN pip3 install -r requirements.txt
RUN python -m textblob.download_corpora 


