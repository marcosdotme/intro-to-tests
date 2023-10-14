from my_lib.functions import execute_query

from tests.fixtures.redshift import POSTGRES_HOST
from tests.fixtures.redshift import POSTGRES_PORT
from tests.fixtures.redshift import POSTGRES_DB
from tests.fixtures.redshift import POSTGRES_USER
from tests.fixtures.redshift import POSTGRES_PASSWORD


def test_count_grand_chase_table(postgres_mocked):
    result = execute_query(
        dbname=POSTGRES_DB,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        query='SELECT COUNT(*) AS count FROM grand_chase;'
    )

    assert result[0].get('count') == 2
