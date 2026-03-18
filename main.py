import os

from flask import Flask, render_template
from extensions import db, bcrypt, login_manager, migrate
from courses.models import Course
from users.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from users.routes import users
from courses.routes import courses
from payments.routes import payments

app.register_blueprint(users)
app.register_blueprint(courses)
app.register_blueprint(payments)

@app.route("/")
@app.route("/home")
def home():
    all_courses = Course.query.limit(5).all()
    return render_template('home.html', courses=all_courses, title='Courses')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 80)))