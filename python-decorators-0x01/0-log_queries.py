import sqlite3
import functools
from datetime import datetime
# #### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if 'query' in kwargs:
            query=kwargs['query']
        elif len(args) > 0:
            query = args[0]
        else:
            query=None
         # Get current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #  Log with timestamp
        print(f"[{timestamp}] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    print( results)

#### fetch users while logging the query
fetch_all_users(query="SELECT * FROM users")

