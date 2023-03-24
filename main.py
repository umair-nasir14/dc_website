from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["DATABASE_URL"] #"mongodb://localhost:27017/deepcreate"  # Use your MongoDB connection string here
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    contact_info = {
        'name': name,
        'email': email,
        'message': message
    }

    mongo.db.contacts.insert_one(contact_info)
    return 'Your message has been received. Thank you!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
