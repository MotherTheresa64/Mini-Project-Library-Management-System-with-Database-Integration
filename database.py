import mysql.connector
from mysql.connector import Error  # Import Error from mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            database='library_management',  # Change this to your actual database name
            user='root',
            password='Buffy20!'
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def fetch_all(self, query, data=None):
        cursor = self.connection.cursor()
        result = []
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
        return result
