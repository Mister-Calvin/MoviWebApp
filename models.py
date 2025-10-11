from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #DATENBANK
#STRUKTUR

class User(db.Model):
    """Represents a user in the movie database.
        This model stores basic user information and establishes a one-to-many
        relationship with the Movie model, allowing each user to have multiple movies.
        Attributes:
            id (int): Primary key, unique identifier for each user.
            name (str): The username; cannot be null.
            movies (list[Movie]): A list of Movie objects associated with this user."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    movies = db.relationship('Movie', backref='user', lazy=True)

    def __str__(self):
        """Returns a human-readable string representation of the User instance.
            Returns:
                str: A formatted string containing the username and user ID."""
        return f"Username: {self.name} - ID: {self.id}"


class Movie(db.Model):
    """Represents a movie in the database.
        This model stores movie details, including name, director, release year,
        poster URL, and rating. Each movie is linked to a user via a foreign key.
        Attributes:
            id (int): Primary key, unique identifier for each movie.
            name (str): Title of the movie; cannot be null.
            director (str): Name of the movie's director; cannot be null.
            year (int): The release year of the movie; cannot be null.
            poster_url (str): Optional URL for the movie's poster image.
            rating (int): The user's rating for the movie (0–10).
            user_id (int): Foreign key linking this movie to its owner (User)."""
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String, nullable=True)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __str__(self):
        """Returns a human-readable string representation of the Movie instance.
           Returns:
               str: A formatted string containing the movie's name, ID, year, director, and poster URL."""
        return f"Movie: {self.name} - ID: {self.id}, Year: {self.year}, director: {self.director}, Poster URL: {self.poster_url}"

