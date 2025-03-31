import sqlite3

def create_db():
    try:
        # Connect to the SQLite database (it will create the file if it doesn't exist)
        conn = sqlite3.connect('login_data.db')
        c = conn.cursor()
        
        # Create the table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS login_details (
                USER_ID TEXT PRIMARY KEY NOT NULL,
                PASSWORD TEXT NOT NULL
            )
        ''')
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()

        print("Database and table created successfully!")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

if __name__ == '__main__':
    create_db()
