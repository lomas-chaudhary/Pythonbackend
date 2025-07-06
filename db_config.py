import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        database="mypythonapp",
        user="root",
        password="root",
        port=3306
    )