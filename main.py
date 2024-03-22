
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lipaksha.db'
db = SQLAlchemy(app)

# Define the Language model
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    proficiency = db.Column(db.Integer)

# Define the Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    title = db.Column(db.String(50))
    content = db.Column(db.Text)

# Define the Exercise model
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    question = db.Column(db.String(50))
    answer = db.Column(db.String(50))

# Create the database tables
db.create_all()

# Define the main route
@app.route('/')
def index():
    # Get all languages
    languages = Language.query.all()
    return render_template('index.html', languages=languages)

# Define the language route
@app.route('/language/<language_id>')
def language(language_id):
    # Get the language
    language = Language.query.get(language_id)
    # Get all lessons for the language
    lessons = Lesson.query.filter_by(language_id=language_id).all()
    # Get all exercises for the language
    exercises = Exercise.query.filter_by(language_id=language_id).all()
    return render_template('language.html', language=language, lessons=lessons, exercises=exercises)

# Define the lesson route
@app.route('/language/<language_id>/lesson/<lesson_id>')
def lesson(language_id, lesson_id):
    # Get the lesson
    lesson = Lesson.query.get(lesson_id)
    return render_template('lesson.html', lesson=lesson)

# Define the exercise route
@app.route('/language/<language_id>/exercise/<exercise_id>')
def exercise(language_id, exercise_id):
    # Get the exercise
    exercise = Exercise.query.get(exercise_id)
    return render_template('exercise.html', exercise=exercise)

# Define the progress route
@app.route('/progress')
def progress():
    return render_template('progress.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
