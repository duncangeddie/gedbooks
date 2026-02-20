import os
from flask import Flask, send_from_directory, session, redirect, url_for
from controllers.page_controller import (
    welcome_controller,
    dashboard_controller,
    logout_controller,
    customer_controller,
    suppliers_controller
)
from controllers.auth_controller import login_controller, register_controller
from controllers.customer_controller import add_customer as add_customer_controller, edit_customer, delete_customer
from controllers.supplier_controller import add_supplier, edit_supplier, delete_supplier
from views.render import render_view
from config.users_database import init_db
from controllers.chart_of_accounts_controller import (
    chart_of_accounts_controller,
    add_account,
    edit_account,
    delete_account
)

app = Flask(__name__, template_folder="../views")
app.secret_key = "your_secret_key"

init_db()

# Base directory = project root (gedbooks/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return welcome_controller()

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    data = dashboard_controller()
    return render_view('dashboard.html', data)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return logout_controller()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_controller()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_controller()

@app.route('/customers')
def customers():
    return customer_controller()

@app.route('/suppliers')
def suppliers():
    return suppliers_controller()

# --- Static file routes ---
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(os.path.join(BASE_DIR, "css"), filename)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.path.join(BASE_DIR, "images"), filename)

# --- Customer routes ---
@app.route('/add_customer', methods=['POST'])
def add_customer():
    return add_customer_controller()

@app.route('/edit_customer/<int:customer_id>', methods=['POST'])
def edit_customer_route(customer_id):
    return edit_customer(customer_id)

@app.route('/delete_customer/<int:customer_id>', methods=['POST'])
def delete_customer_route(customer_id):
    return delete_customer(customer_id)

# --- Supplier routes ---
@app.route('/add_supplier', methods=['POST'])
def add_supplier_route():
    return add_supplier()

@app.route('/edit_supplier/<int:supplier_id>', methods=['POST'])
def edit_supplier_route(supplier_id):
    return edit_supplier(supplier_id)

@app.route('/delete_supplier/<int:supplier_id>', methods=['POST'])
def delete_supplier_route(supplier_id):
    return delete_supplier(supplier_id)

# --- Chart of Accounts routes ---
@app.route('/chart_of_accounts')
def chart_of_accounts():
    return chart_of_accounts_controller()

@app.route('/add_account', methods=['POST'])
def add_account_route():
    return add_account()

@app.route('/edit_account/<int:ref>', methods=['GET', 'POST'])
def edit_account(ref):
    return edit_account(ref)

@app.route('/delete_account/<int:ref>', methods=['POST'])
def delete_account_route(ref):
    return delete_account(ref)

if __name__ == '__main__':
    app.run(debug=True)
