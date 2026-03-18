from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"  # Replace with a real secret key

    # Register blueprints
    from .users.routes import users_bp
    from .courses.routes import courses_bp
    # from .payments.routes import payments_bp
    # from .admin.routes import admin_bp

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(courses_bp, url_prefix="/courses")
    # app.register_blueprint(payments_bp, url_prefix="/payments")
    # app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
