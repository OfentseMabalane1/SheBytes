from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import bcrypt

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

# Function to save user login information
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    fnb_user = request.form.get('fnb_user')  # Capture checkbox value

    save_user_info(username, password, fnb_user)

    return redirect(url_for('landing_page'))

# Function to save user login information
def save_user_info(username, password, fnb_user, file_path='user_data.json'):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user_info = {
        "username": username,
        "password": hashed_password.decode('utf-8'),
        "fnb_user": True if fnb_user else False  # Save checkbox state as boolean
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
    app.run(debug=True)