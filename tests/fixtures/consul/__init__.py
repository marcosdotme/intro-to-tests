import time

import consul
import docker
import pytest


CONSUL_VERSION = '1.16'

CONSUL_HOST = 'localhost'
CONSUL_PORT = 8500
CONSUL_TOKEN = None


@pytest.fixture(scope='session')
def consul_docker():
    client = docker.from_env()
    container = client.containers.run(
        image=f"hashicorp/consul:{CONSUL_VERSION}",
        name='test_consul',
        ports={
            '8500/tcp': (CONSUL_HOST, CONSUL_PORT)
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
def consul_mocked(consul_docker):
    c = consul.Consul(
        host=CONSUL_HOST,
        port=CONSUL_PORT,
        token=CONSUL_TOKEN
    )

    c.kv.put(key='name', value='Marcos')

    yield c
