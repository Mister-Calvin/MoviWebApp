from flask import Flask, render_template, request, redirect
from data_manager import DataManager
from models import db, Movie


app = Flask(__name__)

import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager() # Create an object of your DataManager class



@app.route('/')
def home():
    users = data_manager.get_users()
    return render_template('index.html', users=users)

@app.route('/users', methods=['POST'])
def list_users():
    name = request.form.get('name') #gib namen ein
    existing_users = data_manager.get_users()
    if any(user.name == name for user in existing_users):
        return render_template('index.html', message='User with that name already exists', users=existing_users)
    if name:
        data_manager.create_user(name) # erstelle datensatz
    return redirect ('/')


if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run(debug=True, host='0.0.0.0', port=5005)



