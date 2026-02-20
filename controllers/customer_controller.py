from flask import request, redirect, url_for, session
import mysql.connector

def add_customer():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        email_address = request.form.get('email_address')
        tax_number = request.form.get('tax_number')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        status = request.form.get('status')

        # Convert blank tax_number to None (SQL NULL)
        if not tax_number:
            tax_number = None

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        sql = """
        INSERT INTO customers (user_id, name, email_address, tax_number, phone_number, address, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (session['user_id'], name, email_address, tax_number, phone_number, address, status)

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('customers'))

    return redirect(url_for('customers'))


def edit_customer(customer_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        email_address = request.form.get('email_address')
        tax_number = request.form.get('tax_number')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        status = request.form.get('status')

        # Convert blank tax_number to None (SQL NULL)
        if not tax_number:
            tax_number = None

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        sql = """
        UPDATE customers
        SET name=%s, email_address=%s, tax_number=%s, phone_number=%s, address=%s, status=%s
        WHERE id=%s AND user_id=%s
        """
        values = (name, email_address, tax_number, phone_number, address, status, customer_id, session['user_id'])

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('customers'))

    return redirect(url_for('customers'))


def delete_customer(customer_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WEBsprt2",
        database="user_data"
    )
    cursor = conn.cursor()

    sql = "DELETE FROM customers WHERE id=%s AND user_id=%s"
    values = (customer_id, session['user_id'])

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('customers'))
