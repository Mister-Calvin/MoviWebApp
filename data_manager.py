from models import db, User, Movie

class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        return User.query.all()

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            for movie in user.movies:
                db.session.delete(movie)
            db.session.delete(user)
            db.session.commit()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def get_movie(self, movie_id):
        return Movie.query.filter_by(id=movie_id).first()

    def add_movie(self, movie):
        try:
            db.session.add(movie)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def update_movie_title(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            db.session.commit()
            return True
        return False

    def update_movie_rating(self, movie_id, new_rating):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.rating = new_rating
            db.session.commit()
            return True
        return False

    def delete_movie(self, movie_id):
        movie_to_delete = Movie.query.filter_by(id=movie_id).first()
        if movie_to_delete:
            db.session.delete(movie_to_delete)
            db.session.commit()
            return True
        return False


