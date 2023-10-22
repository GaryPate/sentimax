# Materialize your assets in local Docker containers
# Read the docs on Executors to learn more: https://docs.dagster.io/deployment/executors

from dagster_docker import docker_executor
from dagster import define_asset_job
import os

executor = docker_executor.configured({
  'image': 'australia-southeast1-docker.pkg.dev/ml-dev-402423/dagster-docker/image_name:latest',
  'registry': {
    'url': 'australia-southeast1-docker.pkg.dev/ml-dev-402423/dagster-docker',
    'username': 'my_user',
    'password': os.environ['DOCKER_REGISTRY_PASSWORD'],
  },
  'env_vars': ['DAGSTER_HOME'], # environment vars to pass from celery worker to docker
  'container_kwargs': { # keyword args to be passed to the container. example:
    'volumes': ['/mnt/sentimax/data:/mnt/sentimax/data'],
  },
})

docker_enabled_job = define_asset_job("docker_enabled_job", executor_def=executor)
