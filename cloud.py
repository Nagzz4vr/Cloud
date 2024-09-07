from flask import Flask, request, redirect, url_for, render_template, flash
import requests

app = Flask(__name__)
app.secret_key = '2bf57ea6e5a37f0a78e75768d69c62891bc26aaa8405a49b'  # Change this to a secure key

# API Gateway URL
API_URL = "https://hboezx237l.execute-api.ap-south-1.amazonaws.com/dev"

@app.route('/create', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    user_id = request.form['userId']

    # Send data to the API Gateway to trigger the Lambda function
    payload = {'id': user_id, 'name': name, 'email': email}
    response = requests.post(f"{API_URL}/create", json=payload)

    if response.status_code == 200:
        flash('User created successfully!')
    else:
        flash('Error creating user!')

    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
