from models import db, User, Movie

class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        try:
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f'Failed to create new user: {e}')
            return False
        finally:
            db.session.close()


    def get_users(self):
        return User.query.all()

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            for movie in user.movies:
                try:
                    db.session.delete(movie)
                except Exception as e:
                    db.session.rollback()
                    print(f'Failed to delete movie: {e}')
                    return False
            try:
                db.session.delete(user)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(f'Failed to delete user: {e}')
                return False
            finally:
                db.session.close()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def get_movie(self, movie_id):
        return Movie.query.filter_by(id=movie_id).first()

    def add_movie(self, movie):
        try:
            db.session.add(movie)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f'Failed to add movie: {e}')
            return False
        finally:
            db.session.close()

    def update_movie_title(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            try:
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(f'Failed to update movie: {e}')
                return False
            finally:
                db.session.close()

    def update_movie_rating(self, movie_id, new_rating):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.rating = new_rating
            try:
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(f'Failed to update movie: {e}')
                return False
            finally:
                db.session.close()

    def delete_movie(self, movie_id):
        movie_to_delete = Movie.query.filter_by(id=movie_id).first()
        if movie_to_delete:
            try:
                db.session.delete(movie_to_delete)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(f'Failed to delete movie: {e}')
                return False
            finally:
                db.session.close()


