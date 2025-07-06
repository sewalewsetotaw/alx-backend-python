seed = __import__('seed')


def paginate_users(page_size, offset):
    #    Fetch a page of users from the database.
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows
def lazy_paginate(page_size):
    #    Generator that lazily yields user pages using offset pagination.
    #    Only fetches the next page when needed.
    offset=0
    while True:
        page=paginate_users(page_size,offset)
        if not page:
            break
        yield page 
        offset+=page_size
        return