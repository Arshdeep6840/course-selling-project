from flask import Blueprint, render_template

courses_bp = Blueprint("courses", __name__, template_folder="templates")

@courses_bp.route("/")
def course_list():
    return render_template("courses/course_list.html")

@courses_bp.route("/<course_id>")
def course_detail(course_id):
    return render_template("courses/course_detail.html", course_id=course_id)
