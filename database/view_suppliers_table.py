import mysql.connector
from tabulate import tabulate

def view_suppliers():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",   # your MySQL root password
            database="user_data"
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM suppliers")
        rows = cursor.fetchall()

        if rows:
            # Use headers="keys" when rows is a list of dicts
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        else:
            print("No suppliers found.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    view_suppliers()
