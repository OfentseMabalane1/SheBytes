from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import bcrypt

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('signup.html')

# Function to handle user signup
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password = request.form['password']
    fnb_user = request.form.get('fnb_user')  # Capture checkbox value

    # Save the user info and then redirect to login page
    save_user_info(name, surname, email, password, fnb_user)

    return render_template('index.html')

# Function to handle user login
@app.route('/login')
def login_page():
    return render_template('login.html')

def save_user_info(name, surname, email, password, fnb_user,city, file_path='user_data.json'):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user_info = {
        "name": name,
        "surname": surname,
        "email": email,
        "password": hashed_password.decode('utf-8'),
        "fnb_user": True if fnb_user else False,  # Save checkbox state as boolean
        "city": city
    }

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(user_info)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True, port=80)