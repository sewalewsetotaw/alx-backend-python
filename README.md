✅ Tasks Overview
0. 🛠️ Getting Started with Python Generators

    Script: seed.py

    Goal: Create and populate ALX_prodev MySQL database with user_data table.

    Functions:

        def connect_db()

        def create_database()

        def connect_to_prodev()

        def create_table()

        def insert_data(connection, file_path)

1. 🔄 Stream Users One by One

    Script: 0-stream_users.py

    Goal: Use a generator to yield users one by one from the database.

    Function:
    
        def stream_users()

2. 📦 Batch Processing Large Data

    Script: 1-batch_processing.py

    Goal: Stream data in batches and filter users older than 25.

    Functions:

        def stream_users_in_batches(batch_size)
        def batch_processing(batch_size)

3. ⏩ Lazy Pagination

    Script: 2-lazy_paginate.py

    Goal: Lazily paginate users using LIMIT and OFFSET.

    Functions:

        def paginate_users(page_size, offset)
        def lazy_pagination(page_size)

4. 📊 Average Age with Generator

    Script: 4-stream_ages.py

    Goal: Use a generator to compute average age without loading all data.

    Functions:

        def stream_user_ages()
        def calculate_average_age()

📁 Data Source

    CSV File: user_data.csv

    Sample user data used to populate the MySQL database.

🚀 How to Run

    ✅ Install dependencies:

    pip install mysql-connector-python

✅ Seed the database:

    python seed.py

✅ Run tasks individually:

    python 0-stream_users.py
    python 1-batch_processing.py
    python 2-lazy_paginate.py
    python 4-stream_ages.py
