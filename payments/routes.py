from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from courses.models import Course, Enrollment
from extensions import db

payments = Blueprint('payments', __name__)

@payments.route("/payment/<int:course_id>", methods=['GET', 'POST'])
@login_required
def payment(course_id):
    course = Course.query.get_or_404(course_id)

    if request.method == 'POST':
        # Here you would integrate with a real payment gateway
        # For now, we\'ll simulate a successful payment

        # Enroll user in the course
        if not current_user.is_enrolled(course):
            enrollment = Enrollment(user_id=current_user.id, course_id=course.id)
            db.session.add(enrollment)
            db.session.commit()
            flash('Payment successful! You are now enrolled in the course.', 'success')
        else:
            flash('You are already enrolled in this course.', 'info')

        return redirect(url_for('courses.course', course_id=course.id))

    return render_template('payment.html', course=course)