from flask import request, redirect, url_for, session
import mysql.connector

def add_supplier():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        email_address = request.form.get('email_address')
        tax_number = request.form.get('tax_number')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        status = request.form.get('status')

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",  # your MySQL password
            database="user_data"
        )
        cursor = conn.cursor()

        sql = """
        INSERT INTO suppliers (user_id, name, email_address, tax_number, phone_number, address, status, created)
        VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())
        """
        values = (session['user_id'], name, email_address, tax_number, phone_number, address, status)

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('suppliers'))

    return redirect(url_for('suppliers'))


def edit_supplier(supplier_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name')
        email_address = request.form.get('email_address')
        tax_number = request.form.get('tax_number')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        status = request.form.get('status')

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WEBsprt2",
            database="user_data"
        )
        cursor = conn.cursor()

        sql = """
        UPDATE suppliers
        SET name=%s, email_address=%s, tax_number=%s, phone_number=%s, address=%s, status=%s
        WHERE id=%s AND user_id=%s
        """
        values = (name, email_address, tax_number, phone_number, address, status, supplier_id, session['user_id'])

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('suppliers'))

    return redirect(url_for('suppliers'))


def delete_supplier(supplier_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WEBsprt2",
        database="user_data"
    )
    cursor = conn.cursor()

    sql = "DELETE FROM suppliers WHERE id=%s AND user_id=%s"
    values = (supplier_id, session['user_id'])

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('suppliers'))
