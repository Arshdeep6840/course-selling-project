from extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    enrollments = db.relationship('Enrollment', backref='user', lazy=True)

    def is_enrolled(self, course):
        return course in [enrollment.course for enrollment in self.enrollments]

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"