from flask import request, redirect, url_for, session
from views.render import render_view
import mysql.connector

def welcome_controller():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    page_title = "Welcome"
    heading = "Welcome to GedBooks"
    message = "Your accounting app is ready to go!"
    return render_view('welcome.html', {
        "page_title": page_title,
        "heading": heading,
        "message": message
    })

def dashboard_controller():
    page_title = "Dashboard"
    heading = "GedBooks Dashboard"
    message = "Here you can manage your accounting data."
    return {
        "page_title": page_title,
        "heading": heading,
        "message": message
    }

def logout_controller():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'accept':
            session.pop('user_id', None)
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('dashboard'))
    return render_view('logout.html', {})

def customer_controller():
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
        SELECT id, name, email_address, tax_number, phone_number, address, status, created
        FROM customers
        WHERE user_id = %s
    """, (session['user_id'],))
    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    page_title = "Customers"
    heading = "Customers"
    message = "Manage your customer records here."

    return render_view('customers.html', {
        "page_title": page_title,
        "heading": heading,
        "message": message,
        "customers": customers
    })
