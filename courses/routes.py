from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from courses.models import Course

courses = Blueprint('courses', __name__)

@courses.route("/courses")
def all_courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@courses.route("/course/<int:course_id>")
def course(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course.html', course=course)

@courses.route("/enroll/<int:course_id>", methods=['GET', 'POST'])
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        return redirect(url_for('payments.payment', course_id=course.id))
    return render_template('enroll.html', course=course)
