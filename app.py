from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie
from api_movies import search_movie_and_get_movies


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


@app.route('/users/<int:user_id>/movies', methods=['GET', 'POST'])
def list_movies(user_id):
    try:
        if request.method == 'POST':
            title = request.form.get('name')
            movie_data = search_movie_and_get_movies(title)

            new_movie = Movie(
                name=title,
                year=movie_data['Year'],
                director=movie_data['Director'],
                poster_url=movie_data['Poster'],
                user_id=user_id

            )
            data_manager.add_movie(new_movie)

        users = data_manager.get_users()
        user = next((u for u in users if u.id == user_id), None)
        if not user:
            return "User not found", 404

        movies = data_manager.get_movies(user_id=user_id)

        return render_template('show_movies.html', users=users, movies=movies, user=user)
    except KeyError:
        return render_template('error_key.html')


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    movie = data_manager.get_movie(movie_id)
    if not movie:
        return "Movie not found", 404
    data_manager.delete_movie(movie_id)
    return redirect(url_for('list_movies', user_id=user_id))

@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    new_name = request.form.get('new_name')

    if new_name:
        data_manager.update_movie_title(movie_id, new_name)

    return redirect(url_for('list_movies', user_id=user_id))

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    data_manager.delete_user(user_id)
    return redirect('/')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error_404.html'), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return render_template('error_405.html'), 405

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error_500.html'), 500

@app.errorhandler(Exception)
def handle_all_exceptions(e):
    return render_template("error_exception.html", error=str(e)), 500





if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run(debug=True, host='0.0.0.0', port=5005)



