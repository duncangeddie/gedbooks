import mysql.connector

def list_tables():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        # Run SHOW TABLES
        cursor.execute("SHOW TABLES")

        print("Tables in 'user_data' database:")
        for (table_name,) in cursor.fetchall():
            print(f"- {table_name}")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    list_tables()
