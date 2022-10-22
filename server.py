"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """Renders homepage."""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """Displays all movies."""

    all_movies = crud.get_all_movies()

    return render_template("all_movies.html", movies=all_movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show a particular movie."""

    get_movie = crud.get_specific_movie(movie_id)

    return render_template('movie_details.html', movie=get_movie)


@app.route('/users')
def all_users():
    """Show all users."""

    all_users = crud.get_all_users()

    return render_template('all_users.html', users=all_users)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
