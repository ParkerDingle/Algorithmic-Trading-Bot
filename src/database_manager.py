import sqlite3
import os

DB_PATH = os.path.join('data', 'trading_log.db')

def init_db():
    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the Trades table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            symbol TEXT NOT NULL,
            order_type TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT DEFAULT 'FILLED'
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized and Trades table created.")

if __name__ == "__main__":
    # makes sure the data folder exists
    if not os.path.exists('data'):
        os.makedirs('data')
    init_db()
