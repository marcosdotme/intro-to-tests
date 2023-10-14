import time

import docker
import psycopg2
import pytest


POSTGRES_VERSION = '16'

POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432
POSTGRES_DB = 'postgres'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'password'


@pytest.fixture(scope='session')
def postgres_docker():
    client = docker.from_env()
    container = client.containers.run(
        image=f"postgres:{POSTGRES_VERSION}",
        name='test_postgres',
        environment=dict(
            POSTGRES_PASSWORD=POSTGRES_PASSWORD,
        ),
        ports={
            '5432/tcp': (POSTGRES_HOST, POSTGRES_PORT)
        },
        auto_remove=True,
        detach=True,
        remove=True,
    )

    # Wait for the container to start
    time.sleep(5)

    yield

    container.stop()


@pytest.fixture(scope='session')
def postgres_connection(postgres_docker):
    yield psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
    )


@pytest.fixture(scope='session')
def postgres_mocked(postgres_connection):
    cursor = postgres_connection.cursor()

    with open('tests/fixtures/redshift/schema.sql', mode='r') as file:
        cursor.execute(file.read())
    
    postgres_connection.commit()

    yield postgres_connection
