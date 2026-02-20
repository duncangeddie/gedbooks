from flask import request, redirect, url_for, session
import mysql.connector
from views.render import render_view

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
    cursor = conn.cursor()

    sql = "DELETE FROM chart_of_accounts WHERE ref=%s AND user_id=%s"
    values = (ref, session['user_id'])

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('chart_of_accounts'))
