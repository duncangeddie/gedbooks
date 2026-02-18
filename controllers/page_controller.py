from flask import request, redirect, url_for, session
from views.render import render_view

def welcome_controller():
    page_title = "Welcome"
    heading = "Welcome to GedBooks"
    message = "Your accounting app is ready to go!"
    return {
        "page_title": page_title,
        "heading": heading,
        "message": message
    }

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
    # For GET requests, render the logout confirmation page
    return render_view('logout.html', {})

