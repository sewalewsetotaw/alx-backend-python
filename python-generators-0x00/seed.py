import mysql.connector
import csv
import uuid

def connect_db():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="sewalew",
            password="Sew@bunna123"
            )
        if connection:
             print("MySQL Server connection successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_database(connection):
    try:
        cursor=connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully!")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Database creation error: {err}")

def connect_to_prodev():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="sewalew",
            password="Sew@bunna123",
            database='ALX_prodev'
            )
        if connection:
             print("ALX_prodev database connection successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_table(connection):
    try:
        cursor=connection.cursor()
        cursor.execute ("""
                        CREATE TABLE IF NOT EXISTS user_data (
                        user_id VARCHAR(36) PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR (100) NOT NULL,
                        age DECIMAL (10,2) NOT NULL
                        )
                        """)
        print("Table user_data created successfully!")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
def csv_generator(file_path):
    try:
        with open(file_path,newline='') as csv_file:
            reader=csv.DictReader(csv_file)
            for row in reader:
                yield {
                    'user_id':str(uuid.uuid4()),
                    'name':row['name'],
                    'email':row['email'],
                    'age':float(row['age'])
                }   
    except  FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error reading CSV: {e}")  

def insert_data(connection, file_path):
    try:
        cursor=connection.cursor()
        insert_query="""
            INSERT INTO user_data(user_id,name,email,age) 
            VALUES (%s,%s,%s,%s)
        """
        for row in csv_generator(file_path):
            cursor.execute("SELECT COUNT(*) FROM user_data where email=%s",(row['email'],))
            if cursor.fetchone()[0]==0:
                cursor.execute(insert_query, (row['user_id'],row['name'],row['email'],row['age']))
                print(f"Inserted: {row['email']}")
            else:
                print(f"Skipped (duplicate): {row['email']}")
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    server_conn  = connect_db()
    if server_conn :
        create_database(server_conn )  
        server_conn.close()

    db_conn = connect_to_prodev()
    if db_conn:
        create_table(db_conn)
        insert_data(db_conn, 'user_data.csv')
        db_conn.close()
