# 🐍 Getting started with python generators

## 📌 Objective

Create a **Python generator** that streams rows from a CSV file and inserts them into a MySQL database one by one — using safe connection handling, duplicate checking, and proper schema setup.

---

## 🧱 Database Schema – `user_data`

| Field   | Type           | Constraints       |
| ------- | -------------- | ----------------- |
| user_id | `VARCHAR(36)`  | Primary Key, UUID |
| name    | `VARCHAR(100)` | NOT NULL          |
| email   | `VARCHAR(100)` | NOT NULL          |
| age     | `DECIMAL`      | NOT NULL          |

> 💡 `user_id` is generated using Python’s `uuid.uuid4()`.

---

## 🐍 Function Prototypes

| Function Name         | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `connect_db()`        | Connects to the MySQL server (without selecting a DB)  |
| `create_database()`   | Creates the `ALX_prodev` database if it does not exist |
| `connect_to_prodev()` | Connects to the `ALX_prodev` database                  |
| `create_table()`      | Creates the `user_data` table with required fields     |
| `csv_generator()`     | Python generator that streams rows from a CSV file     |
| `insert_data()`       | Inserts unique rows into the table, skips duplicates   |

---

## 🛠️ Prerequisites

- MySQL server running on `localhost`
- A MySQL user with:
  - Username: `sewalew`
  - Password: `Sew@bunna123` (replace or configure securely)
- Python 3.x installed
- `mysql-connector-python` installed

Install it via pip:

```bash
pip install mysql-connector-python
```
