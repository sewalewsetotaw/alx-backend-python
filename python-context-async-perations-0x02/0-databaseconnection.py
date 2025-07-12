import sqlite3
import os
class DatabaseConnection:
    def __enter__(self):
        db_path=os.path.abspath("E:/ALX ProDev Back-End/alx-backend-python/python-decorators-0x01/users.db")
        self.conn = sqlite3.connect(db_path)
        if self.conn:
            print("Connected to:",db_path)
        self.cursor=self.conn.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()
if __name__=="__main__":
    with DatabaseConnection() as cursor:
        cursor.execute('SELECT * FROM users')
        results=cursor.fetchall()
        for row in results:
            print(row)
