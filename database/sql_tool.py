#imports
import mysql.connector
from tabulate import tabulate

#functions
def view_customers():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()

        if rows:
            # Use headers="keys" when rows is a list of dicts
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        else:
            print("No customers found.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

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

def view_chart_of_accounts():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",   # your MySQL root password
            database="user_data"
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM chart_of_accounts")
        rows = cursor.fetchall()

        if rows:
            # Correct usage: headers="keys" for list of dicts
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        else:
            print("No accounts found.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def clear_all_tables():
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
        cursor.execute("TRUNCATE TABLE chart_of_accounts")

        conn.commit()
        cursor.close()
        conn.close()

        print("All tables cleared.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

#app loop
while True:
    #commands list
    commands = {"view_customers":"View customers table in user_data.sql",
                "view_suppliers":"View suppliers table in user_data.sql",
                "view_chart_of_accounts":"View chart of accounts table in user_data.sql",
                "clear_all_tables":"Clears all tables in user_data.sql",
                }
    #user inputs command
    command_input = str(input("sql_tool/"))
    command = command_input.lower()

    #run command
    if command == "help":
        print("-"*70)
        print("Commands")
        print("-"*70)
        for key, value in commands.items():
            print(f"{key} - {value}")
        print("-"*70)

    elif command == "exit":
        exit()

    elif command == "view_customers":
        view_customers()

    elif command == "view_suppliers":
        view_suppliers()

    elif command == "view_chart_of_accounts":
        view_chart_of_accounts()

    elif command == "clear_all_tables":
        clear_all_tables()

    else:
        print("Unknown command")

