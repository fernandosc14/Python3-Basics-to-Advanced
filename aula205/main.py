import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Insert data
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (?, ?)'
)

# cursor.execute(sql, ['Fernando', 59.5])
cursor.executemany(sql, [['Fernando', 59.5], ['Maria', 65.0], ['João', 78.3]])
connection.commit()

cursor.close()
connection.close()
