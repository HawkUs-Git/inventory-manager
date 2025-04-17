import sqlite3
DB_NAME = 'inventory.db'
def connect_db():
    return sqlite3.connect(DB_NAME)
def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
def insert_item(name, quantity, price):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()
def get_all_items():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    items = c.fetchall()
    conn.close()
    return items
def update_item(item_id, quantity, price):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE inventory SET quantity = ?, price = ? WHERE id = ?", (quantity, price, item_id))
    conn.commit()
    conn.close()
def delete_item(item_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
