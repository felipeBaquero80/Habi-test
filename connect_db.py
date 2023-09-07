import mysql.connector
import os


# configuration bd
def connect_db():
    """
    Establish a connection to the database using the provided environment variables.

    Returns:
        tuple: A tuple containing the connection and cursor objects.
    """
    config = {
        'host': os.environ.get('host_test'),
        'port': os.environ.get('port_test'),
        'user': os.environ.get('user_test'),
        'password': os.environ.get('pass_test'),
        'database': os.environ.get('database_test')
    }

    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conn.cursor()
            return conn, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
