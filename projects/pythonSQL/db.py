import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="student_db",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
