from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://485b4b6c-893b-6:94fd89ef-1884-a@data--capsule-ptzsqp-x:27017/app?authSource=admin&directConnection=true&ssl=tru"#"mongodb://localhost:27017/deepcreate"  # Use your MongoDB connection string here
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
