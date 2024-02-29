import psycopg2


def connect_db():
    try:
        connections = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="123456",
        )
        return connections
    except psycopg2.Error as ex:
        print(f"Error: {ex}. While connecting to Database or Database not exist.")

    except Exception as e:
        print(f"Error: {e}. Unexpected error in Database connect.")
