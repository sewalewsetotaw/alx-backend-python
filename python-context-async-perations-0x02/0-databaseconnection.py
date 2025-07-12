import sqlite3
import os
class DatabaseConnection:
    def __init__(self,dbpath):
        self.dbpath=os.path.abspath(dbpath)
        if self.dbpath:
            print("Path fetched:",self.dbpath)
    def __enter__(self):
        self.conn = sqlite3.connect(self.dbpath)
        if self.conn:
            print("Connected")
        self.cursor=self.conn.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()
if __name__=="__main__":
    dbpath="E:/ALX ProDev Back-End/alx-backend-python/python-decorators-0x01/users.db"
    with DatabaseConnection(dbpath) as cursor:
        cursor.execute('SELECT * FROM users')
        results=cursor.fetchall()
        for row in results:
            print(row)
