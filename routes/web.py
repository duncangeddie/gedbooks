from flask import Flask, send_from_directory, session, redirect, url_for
from controllers.page_controller import welcome_controller, dashboard_controller, logout_controller
from controllers.auth_controller import login_controller, register_controller
from views.render import render_view
from database.migration import init_db

app = Flask(__name__, template_folder="../views")
app.secret_key = "your_secret_key"

init_db()

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    data = welcome_controller()
    return render_view('welcome.html', data)

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

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

if __name__ == '__main__':
    app.run(debug=True)
