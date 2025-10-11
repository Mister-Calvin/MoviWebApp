from models import db, User, Movie

class DataManager():
    """Handles all database operations for users and movies.

    The DataManager class serves as an interface between the Flask routes (app.py)
    and the SQLAlchemy models (models.py). It provides methods for creating, reading,
    updating, and deleting (CRUD) records while ensuring proper error handling and
    transaction safety.

    Each method manages its own database session lifecycle using try/except/finally
    blocks to maintain database stability. Rollbacks are performed automatically
    in case of errors, and sessions are closed after each operation.

    Responsibilities:
    - Manage user and movie records in the SQLite database.
    - Provide reusable, isolated database access methods.
    - Ensure robust exception handling and consistent commit/rollback logic.
    - Maintain a clean separation between application logic and persistence layer."""

    def create_user(self, name):
        """Creates a new user in the database.
            Args:
                name (str): The name of the new user to be created.
            Returns:
                bool: True if the user was successfully created, False if an error occurred."""
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
        """Retrieves all users from the database.
           Returns:
               list[User]: A list containing all User objects stored in the database."""
        return User.query.all()


    def delete_user(self, user_id):
        """Deletes a user and all their associated movies from the database.
           Args:
               user_id (int): The unique ID of the user to delete.
           Returns:
               bool: True if the user and their movies were successfully deleted,
                     False if an error occurred during deletion."""
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
        """Retrieves all movies belonging to a specific user.
           Args:
               user_id (int): The ID of the user whose movies should be fetched.
           Returns:
               list[Movie]: A list of Movie objects associated with the given user."""
        return Movie.query.filter_by(user_id=user_id).all()


    def get_movie(self, movie_id):
        """Fetches a single movie from the database by its ID.
            Args:
                movie_id (int): The ID of the movie to retrieve.
            Returns:
                Movie | None: The Movie object if found, otherwise None."""
        return Movie.query.filter_by(id=movie_id).first()


    def add_movie(self, movie):
        """Adds a new movie to the database.
            Args:
                movie (Movie): A Movie object to be added to the database.
            Returns:
                bool: True if the movie was successfully added, False if an error occurred."""
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
        """Updates the title of an existing movie in the database.
        Args:
            movie_id (int): The ID of the movie to update.
            new_title (str): The new title to assign to the movie.
        Returns:
            bool: True if the movie title was successfully updated, False otherwise."""
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
        """Updates the rating value of a movie in the database.
            Args:
                movie_id (int): The ID of the movie whose rating should be updated.
                new_rating (float): The new rating value (expected range: 0–10).
            Returns:
                bool: True if the rating was successfully updated, False otherwise."""
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
        """Deletes a specific movie from the database.
            Args:
                movie_id (int): The unique ID of the movie to delete.
            Returns:
                bool: True if the movie was successfully deleted, False otherwise."""
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


