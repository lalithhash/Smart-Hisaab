import sqlite3
conn=sqlite3.connect('orders.db')
cursor=conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        item TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
''')
conn.commit()
conn.close()