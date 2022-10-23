"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    return User(email=email, password=password)


def get_all_users():
    """Gives all users."""

    return User.query.all()


def get_user_by_email(email):
    """Gives us user by given email."""

    return User.query.filter(User.email == email).first()


def get_user_password_and_user_id(email):
    """Gives us user password and user_id."""

    user = User.query.filter(User.email == email).first()

    if user:
        return [user.password, user.user_id]
    else:
        return [None, None]


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    return Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path
    )


def get_all_movies():
    """Gives all movies."""

    return Movie.query.all()


def get_specific_movie(movie_id):
    """Gives movie of choice."""

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create a rating."""

    return Rating(user=user, movie=movie, score=score)


def filter_ratings_by_user(user_id):
    """Gives all ratings attributed to a user."""

    return Rating.query.filter(Rating.user_id == user_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
