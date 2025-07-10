import sqlite3
import functools

# #### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if 'query' in kwargs:
            query=kwargs['query']
        elif 'query' in args:
            query=args['query']
        else:
            query=None
        print(f"[LOG] Executing SQL Query: {query}")
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

