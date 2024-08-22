from flask import Flask, request, jsonify, render_template
import json
import bcrypt

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

# # Function to save user login information
# def save_user_info(username, password, file_path='user_data.json'):
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#     user_info = {
#         "username": username,
#         "password": hashed_password.decode('utf-8')
#     }

#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = []

#     data.append(user_info)

#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     save_user_info(username, password)

#     return jsonify({"message": "User login information saved."})

if __name__ == '__main__':
    app.run(debug=True)