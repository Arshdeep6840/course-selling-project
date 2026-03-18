import os
import sys
import random

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from main import app
from extensions import db
from courses.models import Course, Video

def create_demo_courses():
    """Create 20 demo courses and add them to the database."""
    with app.app_context():
        # Truncate the tables
        db.session.query(Video).delete()
        db.session.query(Course).delete()

        course_titles = [
            "Python for Beginners", "Flask Web Development", "Advanced Python",
            "Data Science with Python", "Machine Learning Fundamentals", "Introduction to SQL",
            "JavaScript for Web Developers", "React Crash Course", "Node.js Essentials",
            "Cybersecurity Basics", "Ethical Hacking", "Cloud Computing with AWS",
            "Docker for DevOps", "Kubernetes Explained", "iOS App Development with Swift",
            "Android App Development with Kotlin", "Game Development with Unity", "Unreal Engine 5 for Beginners",
            "Blender 3D Modeling", "UI/UX Design Fundamentals"
        ]

        courses = []
        for title in course_titles:
            description = f"A comprehensive course on {title}."
            price = round(random.uniform(29.99, 199.99), 2)
            image_file = f"https://placeimg.com/640/480/tech?{random.randint(1, 100)}"
            course = Course(title=title, description=description, price=price, image_file=image_file)
            courses.append(course)

            # Create 5 demo videos for each course
            videos = []
            for i in range(1, 6):
                video_title = f"Chapter {i}: Introduction to {title}"
                video_url = f"https://www.youtube.com/embed/dQw4w9WgXcQ"  # Placeholder URL
                videos.append(Video(title=video_title, video_url=video_url, course=course))
            db.session.add_all(videos)

        db.session.add_all(courses)
        db.session.commit()
        print("Successfully added 20 demo courses and 100 demo videos to the database.")

if __name__ == '__main__':
    create_demo_courses()