FROM python:3.10.4


ARG DAGSTER_VERSION

# All packages are hard-pinned to `dagster`, so setting the version on just `DAGSTER` will ensure
# compatible versions.
RUN pip install \
    dagster==1.5.4 \
    dagster-postgres \
    dagster-aws \
    dagster-k8s \
    dagster-celery[flower,redis,kubernetes] \
    dagster-celery-k8s

# Get example pipelines
COPY example/ /