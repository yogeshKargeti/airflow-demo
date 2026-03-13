from airflow.hooks.base import BaseHook
import psycopg2

def fetch_employees():

    # Get connection from Airflow
    conn = BaseHook.get_connection("test_postgres_conn")

    connection = psycopg2.connect(
        host=conn.host,
        user=conn.login,
        password=conn.password,
        dbname=conn.schema,
        port=conn.port
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees;")

    rows = cursor.fetchall()

    print("Query Output:")
    for row in rows:
        print(row)

    cursor.close()
    connection.close()