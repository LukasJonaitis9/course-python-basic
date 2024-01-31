import sqlite3

connector = sqlite3.connect('zmones.db')
cursor = connector.cursor()

def create_table(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS friends (
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR (250),
)
'''
    cursor.execute(query)
    connector.commit()

if __name__ == '__main__':
    create_table(connector, cursor)
    connector.close()