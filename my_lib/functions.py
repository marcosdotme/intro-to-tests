def fahrenheit_to_celsius(f):
    return (5 * (f - 32)) / 9


def get_consul_key(
    key: str,
    host='127.0.0.1',
    port=8500,
    token=None,
    consul_instance=None,
):
    import consul

    if consul_instance:
        print('is using mocked')
        c = consul_instance
    else:
        print('is not using mocked')
        c = consul.Consul(host=host, port=port, token=token)

    index, data = c.kv.get(key=key)
    key_value = data.get('Value').decode()

    return key_value


def execute_query(
    dbname: str,
    host: str,
    port: str,
    user: str,
    password: str,
    query: str
):
    import psycopg2
    from psycopg2.extras import RealDictCursor

    try:
        with psycopg2.connect(dbname=dbname, host=host, port=port, user=user, password=password) as redshift_db:
            with redshift_db.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query)

                results = cursor.fetchall()

                return results

    except Exception as e:
        raise e
