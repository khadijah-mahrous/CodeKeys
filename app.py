from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps
import json
import difflib

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
    """Returns float from 0-5 with 0.5 increments for half-star support"""
    return round(accuracy / 20, 1)  # 100% = 5.0, 85% = 4.25, 70% = 3.5

# Lesson database - references to imported lesson arrays
lessons_db = {
    "basics": BASICS_LESSONS,
    "python": PYTHON_LESSONS,
    "javascript": JAVASCRIPT_LESSONS,
    "java": JAVA_LESSONS
}

# Language metadata
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

def normalize_text(text):
    """Normalize quotes, spaces, and line endings for fair comparison"""
    text = text.replace("'", "'").replace('"', '"').replace('"', '"')
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    lines = [line.rstrip() for line in lines]  # Remove trailing spaces only
    return "\n".join(lines)

def calculate_accuracy_fixed(user_input, target):
    """Smart accuracy that handles shifts, missing chars, extra chars"""
    user_input = normalize_text(user_input.strip())
    target = normalize_text(target.strip())
    
    matcher = difflib.SequenceMatcher(None, user_input, target)
    return int(matcher.ratio() * 100)

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email').lower().strip()
    password = request.form.get('password')
    
    if not name or not email or not password:
        return jsonify({"success": False, "message": "All fields required!"}), 400
    
    if email in users_db:
        return jsonify({"success": False, "message": "Email already exists!"}), 400
    
    users_db[email] = {"name": name, "email": email, "password": password}
    user_progress[email] = {
        "username": name, "email": email, "level": 1, "total_words": 0, "accuracy": 0,
        "problem_keys": [], "basics_level": 1, "python_level": 1, "javascript_level": 1,
        "java_level": 1, "basics_scores": {}, "python_scores": {}, "javascript_scores": {}, "java_scores": {}
    }
    session['user_id'] = email
    session['user_name'] = name
    return jsonify({"success": True, "message": "Signup successful!"})

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email').lower().strip()
    password = request.form.get('password')
    
    if email in users_db and users_db[email]['password'] == password:
        session['user_id'] = email
        session['user_name'] = users_db[email]['name']
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid email or password!"}), 400

@app.route('/start_basics')
def start_basics():
    """Redirect to Basics intro page first, then to lesson 1"""
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='basics'))
    return redirect(url_for('language_intro', language='basics'))

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
    total_basics_lessons = len(lessons_db.get("basics", []))
    return render_template('dashboard.html', data=user_data, languages=LANGUAGE_INFO, total_basics_lessons=total_basics_lessons)

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
    if 'user_id' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    if language not in lessons_db:
        return jsonify({"error": "Language not found"}), 404
    
    user_email = session['user_id']
    user_data = user_progress.get(user_email, {})
    current_level = user_data.get(f"{language}_level", 1)
    total_lessons = len(lessons_db.get(language, []))
    
    if current_level > total_lessons:
        current_level = total_lessons
    
    return jsonify({"next_lesson_id": current_level, "total_lessons": total_lessons})

@app.route('/process_stats', methods=['POST'])
def process_stats():
    data = request.get_json()
    email = session.get('user_id')
    if not email or email not in user_progress:
        return jsonify({"status": "error"}), 404
    
    lang = data.get('lang', 'basics')
    lesson_id = int(data.get('lesson_id'))
    
    typed_text = data.get('typed_text', '')
    target_text = lessons_db.get(lang, [])[lesson_id - 1]['target'] if lesson_id <= len(lessons_db.get(lang, [])) else ""
    
    if typed_text and target_text:
        new_acc = calculate_accuracy_fixed(typed_text, target_text)
    else:
        new_acc = int(data.get('accuracy', 0))
    
    wpm = int(data.get('wpm', 0))
    mistakes = int(data.get('mistakes', 0))
    total_chars = int(data.get('total_chars', 0))
    
    session['last_results'] = {
        "accuracy": new_acc,
        "wpm": wpm,
        "mistakes": mistakes,
        "total_chars": total_chars,
        "lesson_id": lesson_id,
        "lang": lang
    }
    
    score_key = f"{lang}_scores"
    if score_key not in user_progress[email]:
        user_progress[email][score_key] = {}
    
    old_acc = user_progress[email][score_key].get(str(lesson_id), 0)
    if new_acc > old_acc:
        user_progress[email][score_key][str(lesson_id)] = new_acc
    
    level_key = f"{lang}_level"
    current_level = user_progress[email].get(level_key, 1)
    
    if lang == "basics":
        lesson_data = lessons_db["basics"][lesson_id - 1]
        required_pass = lesson_data.get("pass_score", 65) if lesson_data.get("is_exam") else 65
        if new_acc >= required_pass and lesson_id == current_level:
            total_lessons = len(lessons_db.get(lang, []))
            if current_level < total_lessons:
                user_progress[email][level_key] = current_level + 1
    else:
        if new_acc >= 1 and lesson_id == current_level:
            total_lessons = len(lessons_db.get(lang, []))
            if current_level < total_lessons:
                user_progress[email][level_key] = current_level + 1
    
    session.modified = True
    return jsonify({"status": "success"})

@app.route('/results/<language>/<int:lesson_id>')
def results(language, lesson_id):
    email = session.get('user_id')
    if not email or email not in user_progress:
        return redirect(url_for('index'))
    
    res = session.get('last_results', {})
    score_dict = user_progress[email].get(f"{language}_scores", {})
    best_accuracy = score_dict.get(str(lesson_id), 0)
    
    current_accuracy = res.get('accuracy', 0)
    stars = calculate_stars(current_accuracy)
    
    messages = {
        5: "Perfect! 🌟🌟🌟🌟🌟",
        4: "Great! 🌟🌟🌟🌟",
        3: "Good! 🌟🌟🌟",
        2: "Keep practicing! 🌟🌟",
        1: "Try again! 🌟",
        0: "Need more practice!"
    }
    
    track_lessons = lessons_db.get(language, [])
    current_lesson = next((l for l in track_lessons if l['id'] == lesson_id), None)
    
    return render_template('result.html',
                           accuracy=current_accuracy,
                           total_chars=res.get('total_chars', 0),
                           mistakes=res.get('mistakes', 0),
                           wpm=res.get('wpm', 0),
                           lang=language,
                           lesson_id=lesson_id,
                           lesson_title=current_lesson['title'] if current_lesson else "Lesson Complete",
                           lesson=current_lesson,
                           stars=stars,
                           star_message=messages.get(int(stars), "Keep going!"),
                           passed=current_accuracy >= 70,
                           total_lessons=len(track_lessons))

if __name__ == '__main__':
    app.run(debug=True)