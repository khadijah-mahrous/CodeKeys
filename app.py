from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this_12345'

# User database
users_db = {}
user_progress = {}

# Import lessons from separate files
from lessons.basics_lessons import BASICS_LESSONS
from lessons.python_lessons import PYTHON_LESSONS
from lessons.javascript_lessons import JAVASCRIPT_LESSONS
from lessons.java_lessons import JAVA_LESSONS

def calculate_stars(accuracy):
    """Convert accuracy percentage to star rating (1-5)"""
    if accuracy >= 95:
        return 5
    elif accuracy >= 80:
        return 4
    elif accuracy >= 70:
        return 3
    elif accuracy >= 60:
        return 2
    elif accuracy >= 50:
        return 1
    else:
        return 0
    
# Lesson database - references to imported lesson arrays
lessons_db = {
    "basics": BASICS_LESSONS,
    "python": PYTHON_LESSONS,
    "javascript": JAVASCRIPT_LESSONS,
    "java": JAVA_LESSONS
}

# Language metadata - Make sure this is defined BEFORE the routes
LANGUAGE_INFO = {
    "basics": {
        "name": "Typing Basics",
        "description": "Master the fundamentals of touch typing with proper finger placement.",
        "icon": "⌨️",
        "color": "#8b5cf6"
    },
    "python": {
        "name": "Python Programming",
        "description": "Learn Python syntax while building typing speed. Perfect for beginners!",
        "icon": "🐍",
        "color": "#06b6d4"
    },
    "javascript": {
        "name": "JavaScript",
        "description": "Master JavaScript fundamentals and modern ES6+ syntax through typing practice.",
        "icon": "⚡",
        "color": "#fbbf24"
    },
    "java": {
        "name": "Java",
        "description": "Build strong Java programming skills with hands-on typing exercises.",
        "icon": "☕",
        "color": "#ef4444"
    }
}

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email in users_db:
        return jsonify({"success": False, "message": "Email already exists!"}), 400
    
    users_db[email] = {
        "name": name,
        "email": email,
        "password": password
    }
    
    # Initialize progress for all languages
    user_progress[email] = {
        "username": name,
        "email": email,
        "level": 1,
        "total_words": 0,
        "accuracy": 0,
        "problem_keys": [],
        "basics_level": 1,
        "python_level": 1,
        "javascript_level": 1,
        "java_level": 1,
        "basics_scores": {},
        "python_scores": {},
        "javascript_scores": {},
        "java_scores": {}
    }
    
    session['user_id'] = email
    session['user_name'] = name
    
    return jsonify({"success": True, "message": "Signup successful!"})

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email in users_db and users_db[email]['password'] == password:
        session['user_id'] = email
        session['user_name'] = users_db[email]['name']
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid email or password!"}), 400

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))

@app.route('/check_auth')
def check_auth():
    if 'user_id' in session:
        return jsonify({"logged_in": True, "name": session.get('user_name')})
    return jsonify({"logged_in": False})

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='dashboard'))
    
    user_data = user_progress.get(session['user_id'], {
        "username": session.get('user_name', 'User'),
        "level": 1,
        "accuracy": 0
    })
    return render_template('dashboard.html', data=user_data, languages=LANGUAGE_INFO)

@app.route('/')
def index():
    user_id = session.get('user_id')
    user_data = user_progress.get(user_id, {"level": 1}) if user_id else {"level": 1}
    return render_template('index.html', data=user_data, languages=LANGUAGE_INFO)

@app.route('/courses/<language>')
def courses(language):
    if language not in lessons_db:
        return "Language not found", 404
    
    user_id = session.get('user_id')
    data = user_progress.get(user_id, {}) if user_id else {}
    
    lang_lessons = lessons_db.get(language, [])
    
    # Pass the calculate_stars function to the template
    return render_template('courses.html', 
                          lessons=lang_lessons, 
                          lang=language, 
                          data=data, 
                          lang_info=LANGUAGE_INFO.get(language, {}),
                          languages=LANGUAGE_INFO,
                          calculate_stars=calculate_stars)

@app.route('/intro/<language>')
def language_intro(language):
    if language not in LANGUAGE_INFO:
        return "Language not found", 404
    
    user_id = session.get('user_id')
    data = user_progress.get(user_id, {"level": 1}) if user_id else {"level": 1}
    
    lang_info = LANGUAGE_INFO.get(language, {})
    return render_template('intro.html', lang=language, description=lang_info.get('description', ''), data=data, lang_info=lang_info)

@app.route('/lesson/<language>/<int:lesson_id>')
def lesson(language, lesson_id):
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='lesson'))
    
    if language not in lessons_db:
        return "Language not found", 404
        
    user_id = session['user_id']
    data = user_progress.get(user_id, {})
    
    track_lessons = lessons_db.get(language, [])
    current_lesson = next((l for l in track_lessons if l['id'] == lesson_id), None)
    
    if not current_lesson:
        return "Lesson not found", 404
        
    return render_template('lesson.html', lang=language, lesson=current_lesson, data=data, lang_info=LANGUAGE_INFO.get(language, {}))

@app.route('/get_next_lesson/<language>')
def get_next_lesson(language):
    """Returns the next available lesson ID for a specific language"""
    if 'user_id' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    if language not in lessons_db:
        return jsonify({"error": "Language not found"}), 404
    
    user_email = session['user_id']
    user_data = user_progress.get(user_email, {})
    
    # Get current level for this language (default to 1)
    current_level = user_data.get(f"{language}_level", 1)
    total_lessons = len(lessons_db.get(language, []))
    
    # Don't exceed total lessons
    if current_level > total_lessons:
        current_level = total_lessons
    
    return jsonify({
        "next_lesson_id": current_level,
        "total_lessons": total_lessons
    })

@app.route('/process_stats', methods=['POST'])
def process_stats():
    data = request.get_json()
    email = session.get('user_id')
    
    if not email or email not in user_progress:
        return jsonify({"status": "error"}), 404
    
    lang = data.get('lang', 'basics')
    lesson_id = int(data.get('lesson_id'))
    new_acc = data.get('accuracy', 0)
    wpm = data.get('wpm', 0)
    mistakes = data.get('mistakes', 0)
    total_chars = data.get('total_chars', 0)
    
    # Debug print to see what's coming in
    print(f"Processing stats - Lang: {lang}, Lesson: {lesson_id}")
    print(f"Accuracy: {new_acc}%, WPM: {wpm}, Mistakes: {mistakes}, Total Chars: {total_chars}")

    # Save for Result page
    session['last_results'] = {
        "accuracy": new_acc, 
        "wpm": wpm, 
        "mistakes": mistakes,
        "total_chars": total_chars,
        "lesson_id": lesson_id,
        "lang": lang
    }
    
    # Track progress per language
    score_key = f"{lang}_scores"
    level_key = f"{lang}_level"
    
    if score_key not in user_progress[email]:
        user_progress[email][score_key] = {}
    
    # Save best accuracy
    old_acc = user_progress[email][score_key].get(str(lesson_id), 0)
    if new_acc > old_acc:
        user_progress[email][score_key][str(lesson_id)] = new_acc
        print(f"New best accuracy saved: {new_acc}% (was {old_acc}%)")

    # Progression logic - only progress if accuracy >= 70 and it's the current level
    current_level = user_progress[email].get(level_key, 1)
    total_lessons = len(lessons_db.get(lang, []))
    
    if new_acc >= 70 and lesson_id == current_level and lesson_id < total_lessons:
        user_progress[email][level_key] = current_level + 1
        print(f"Progressed to level {current_level + 1} in {lang}")
        
    session.modified = True
    return jsonify({"status": "success"})

@app.route('/resume')
def resume_learning():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='lesson'))
    
    return redirect(url_for('courses', language='python'))

@app.route('/results/<language>/<int:lesson_id>')
def results(language, lesson_id):
    # Get results from session
    res = session.get('last_results', {})
    
    accuracy = res.get('accuracy', 0)
    total_chars = res.get('total_chars', 0)
    mistakes = res.get('mistakes', 0)
    wpm = res.get('wpm', 0)
    
    # Calculate stars based on accuracy
    if accuracy >= 95:
        stars = 5
        star_message = "Perfect! 🌟🌟🌟🌟🌟"
    elif accuracy >= 80:
        stars = 4
        star_message = "Great! 🌟🌟🌟🌟"
    elif accuracy >= 70:
        stars = 3
        star_message = "Good! 🌟🌟🌟"
    elif accuracy >= 60:
        stars = 2
        star_message = "Keep practicing! 🌟🌟"
    elif accuracy >= 50:
        stars = 1
        star_message = "Try again! 🌟"
    else:
        stars = 0
        star_message = "Need more practice!"
    
    # Get the lesson title
    track_lessons = lessons_db.get(language, [])
    lesson = next((l for l in track_lessons if l['id'] == lesson_id), None)
    lesson_title = lesson['title'] if lesson else f"Lesson {lesson_id}"
    
    # Determine if passed (70% or higher)
    passed = accuracy >= 70
    
    total_lessons = len(track_lessons)
    
    return render_template('result.html', 
                           accuracy=accuracy, 
                           total_chars=total_chars,
                           mistakes=mistakes,
                           wpm=wpm,
                           lang=language,
                           lesson_id=lesson_id,
                           lesson_title=lesson_title,
                           stars=stars,
                           star_message=star_message,
                           passed=passed,
                           total_lessons=total_lessons)

if __name__ == '__main__':
    app.run(debug=True)
