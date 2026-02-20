from flask import request, redirect, url_for, session
import mysql.connector
from views.render import render_view

# Mandatory accounts list
MANDATORY_ACCOUNTS = [
    ("Cash", "Asset", 2),
    ("Bank Account", "Asset", 2),
    ("Inventory", "Asset", 2),
    ("Accounts Receivable", "Asset", 2),
    ("Prepaid Expenses", "Asset", 2),
    ("Depreciation", "Asset", 2),

    ("Accounts Payable", "Liability", 2),
    ("Payroll Liabilities", "Liability", 2),
    ("Salaries & Wages Payable", "Liability", 2),
    ("Payroll Taxes Payable", "Liability", 2),

    ("Owners Capital", "Equity", 2),
    ("Owners Drawings", "Equity", 2),
    ("Dividends Paid", "Equity", 2),
    ("Retained Earnings", "Equity", 2),

    ("Sales", "Income", 2),
    ("Interest Income", "Income", 2),

    ("Cost of Goods Sold", "Expense", 2),
    ("Accounting Fees", "Expense", 2),
    ("Advertising & Promotion", "Expense", 2),
    ("Bank Charges", "Expense", 2),
    ("Billable Expenses", "Expense", 2),
    ("Computer Equipment/Software", "Expense", 2),
    ("Depreciation Expense", "Expense", 2),
    ("Donations", "Expense", 2),
    ("Electricity & Water", "Expense", 2),
    ("Entertainment", "Expense", 2),
    ("Delivery Expense", "Expense", 2),
    ("Insurance", "Expense", 2),
    ("Interest Paid", "Expense", 2),
    ("Legal Fees", "Expense", 2),
    ("Motor Vehicle Expenses", "Expense", 2),
    ("Office Supplies", "Expense", 2),
    ("Printing & Stationery", "Expense", 2),
    ("Rent", "Expense", 2),
    ("Repairs & Maintenance", "Expense", 2),
    ("Salaries & Wages", "Expense", 2),
    ("Telephone & Internet", "Expense", 2),
    ("Training & Education", "Expense", 2),
    ("Travel & Accommodation", "Expense", 2),
]

def seed_chart_of_accounts(user_id):
    """Insert mandatory accounts for a new user if none exist."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM chart_of_accounts WHERE user_id = %s", (user_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            sql = """
            INSERT INTO chart_of_accounts (user_id, name, type, status, created)
            VALUES (%s, %s, %s, %s, CURDATE())
            """
            for name, type_, status in MANDATORY_ACCOUNTS:
                cursor.execute(sql, (user_id, name, type_, status))
            conn.commit()

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def chart_of_accounts_controller():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WEBsprt2",
        database="user_data"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT ref, name, type, status, created
        FROM chart_of_accounts
        WHERE user_id = %s
    """, (session['user_id'],))
    accounts = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_view('chart_of_accounts.html', {
        "page_title": "Chart of Accounts",
        "heading": "Chart of Accounts",
        "message": "Manage your accounts here.",
        "accounts": accounts
    })

def add_account():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        status = request.form.get('status')

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        sql = """
        INSERT INTO chart_of_accounts (user_id, name, type, status, created)
        VALUES (%s, %s, %s, %s, CURDATE())
        """
        values = (session['user_id'], name, type_, status)

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('chart_of_accounts'))

    return redirect(url_for('chart_of_accounts'))

def edit_account(ref):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        status = request.form.get('status')

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        sql = """
        UPDATE chart_of_accounts
        SET name=%s, type=%s, status=%s
        WHERE ref=%s AND user_id=%s
        """
        values = (name, type_, status, ref, session['user_id'])

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('chart_of_accounts'))

    return redirect(url_for('chart_of_accounts'))

def delete_account(ref):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WEBsprt2",
        database="user_data"
    )
    cursor = conn.cursor(dictionary=True)

    # Prevent deletion of mandatory accounts
    cursor.execute("SELECT status FROM chart_of_accounts WHERE ref=%s AND user_id=%s", (ref, session['user_id']))
    account = cursor.fetchone()

    if account and account['status'] == 2:
        cursor.close()
        conn.close()
        return redirect(url_for('chart_of_accounts'))

    sql = "DELETE FROM chart_of_accounts WHERE ref=%s AND user_id=%s"
    values = (ref, session['user_id'])

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('chart_of_accounts'))
