from flask import render_template, request, redirect, url_for, session
from models.user import User
from views.render import render_view
from database.migration import init_db, get_db_connection

def login_controller():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
        else:
            return render_view('login.html', {"error": "Invalid credentials"})
    return render_view('login.html')

def register_controller():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))
    return render_view('register.html')
