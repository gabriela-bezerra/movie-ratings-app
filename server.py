"""Server for movie ratings app."""

from crypt import methods
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
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


@app.route('/users', methods=['POST'])
def make_user():
    """Create a new user"""

    email = request.form.get('email')
    password = request.form.get('password')

    checking_user = crud.get_user_by_email(email)

    if checking_user:
        flash("This email is already for use by an existing user.")
    else:
        checking_user = crud.create_user(email, password)
        db.session.add(checking_user)
        db.session.commit()
        flash("You have successfully created an account! Please login.")

    return redirect('/')


@app.route('/login', methods=['POST'])
def login_user():

    email = request.form.get('email')
    password = request.form.get('password')

    checking_user = crud.get_user_password_and_user_id(email)

    user_password, user_id = checking_user

    if password == user_password:
        session['user_id'] = user_id
        flash("Logged in!")
        return redirect('/users/<user_id>')
    elif not user_id:
        flash("User does not exist.")
    else:
        flash("Password does not match. Please try again.")


@app.route('/users/<user_id>')
def user_profile(user_id):
    """Show all ratings given by a user."""

    user_id = session['user_id']

    all_user_ratings = crud.filter_ratings_by_user(user_id)

    return render_template('user_profile.html', ratings=all_user_ratings)


#  given_rating = request.form.get('rating-score')
#  new_rating = crud.create_rating(user, movie,score)

# cannot access session and ratings.

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
