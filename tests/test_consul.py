from my_lib.functions import get_consul_key

from tests.fixtures.consul import CONSUL_HOST
from tests.fixtures.consul import CONSUL_PORT
from tests.fixtures.consul import CONSUL_TOKEN


def test_get_name_key(consul_mocked):
    key_value = get_consul_key(
        key='name',
        host=CONSUL_HOST,
        port=CONSUL_PORT,
        token=CONSUL_TOKEN
    )

    assert key_value == 'Marcos'
