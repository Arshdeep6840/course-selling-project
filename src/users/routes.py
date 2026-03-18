from flask import Blueprint, render_template

users_bp = Blueprint("users", __name__, template_folder="templates")

@users_bp.route("/login")
def login():
    return render_template("users/login.html")

@users_bp.route("/register")
def register():
    return render_template("users/register.html")

@users_bp.route("/dashboard")
def dashboard():
    return render_template("users/dashboard.html")

@users_bp.route("/profile")
def profile():
    return render_template("users/profile.html")
