from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite Database setup function
def get_db():
    conn = sqlite3.connect('login_data.db')  # Ensure this path is correct
    conn.row_factory = sqlite3.Row
    return conn

# Route for the Homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists in the database
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login_details WHERE USER_ID = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # If the username already exists, pass the error message to the template
            return render_template('register.html', error="Username already exists. Please choose another.")

        # If username does not exist, insert the new user
        cursor.execute("INSERT INTO login_details (USER_ID, PASSWORD) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))  # Redirect to login page after successful register

    return render_template('register.html')

# Route for Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match in the database
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login_details WHERE USER_ID = ? AND PASSWORD = ?", (username, password))
        user = cursor.fetchone()
        
        if user:
            # Successful login
            return f"Login Successful! Welcome {username}"
        else:
            # Invalid credentials
            return "Invalid username or password. Please try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

