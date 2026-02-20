import mysql.connector

def clear_tables():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2"
        )
        cursor = conn.cursor()

        # Clear users database
        cursor.execute("USE users")
        cursor.execute("TRUNCATE TABLE users")

        # Clear user_data database
        cursor.execute("USE user_data")
        cursor.execute("TRUNCATE TABLE customers")
        cursor.execute("TRUNCATE TABLE suppliers")

        conn.commit()
        cursor.close()
        conn.close()

        print("All users, customers, and suppliers cleared successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    clear_tables()
