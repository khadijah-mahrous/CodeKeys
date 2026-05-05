from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps
import json
import difflib
import os
from utils.text_normalizer import calculate_accuracy, normalize_code
from database import get_db, init_db, save_user, get_user, get_user_by_id, get_user_progress, update_user_progress, get_lesson_score, save_lesson_score, get_all_scores
from database import *

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this_12345'
app.permanent_session_lifetime = 3600  # Session lasts 1 hour

# Initialize database
init_db()

# Import lessons from separate files
from lessons.basics_lessons import BASICS_LESSONS
from lessons.python_lessons import PYTHON_LESSONS
from lessons.javascript_lessons import JAVASCRIPT_LESSONS
from lessons.java_lessons import JAVA_LESSONS

def calculate_stars(accuracy):
    """Returns float from 0-5 with 0.5 increments for half-star support"""
    return round(accuracy / 20, 1)

# Lesson database
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
    lines = [line.rstrip() for line in lines]
    return "\n".join(lines)

def calculate_accuracy_fixed(user_input, target):
    """Calculate exact character-by-character accuracy"""
    from database import calculate_accuracy_exact, normalize_code_for_comparison
    
    user_input = normalize_code_for_comparison(user_input.strip())
    target = normalize_code_for_comparison(target.strip())
    
    accuracy, mistakes, correct = calculate_accuracy_exact(user_input, target)
    return accuracy

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email').lower().strip()
    password = request.form.get('password')
    
    if not name or not email or not password:
        return jsonify({"success": False, "message": "All fields required!"}), 400
    
    result = save_user(email, name, password)
    
    if result["success"]:
        user = get_user(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session.permanent = True
            return jsonify({"success": True, "message": "Signup successful!"})
    
    return jsonify({"success": False, "message": result.get("message", "Signup failed")}), 400

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email').lower().strip()
    password = request.form.get('password')
    
    user = get_user(email, password)
    
    if user:
        session['user_id'] = user['id']
        session['user_name'] = user['name']
        session.permanent = True
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid email or password!"}), 400

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('last_results', None)
    return redirect(url_for('index'))

@app.route('/check_auth')
def check_auth():
    if 'user_id' in session:
        user = get_user_by_id(session['user_id'])
        if user:
            return jsonify({"logged_in": True, "name": user['name']})
    return jsonify({"logged_in": False})

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='dashboard'))
    
    user = get_user_by_id(session['user_id'])
    progress = get_user_progress(session['user_id'])
    
    # Get best accuracy and which language
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT language, MAX(score) as best_score 
        FROM lesson_scores 
        WHERE user_id = ?
        GROUP BY language
        ORDER BY best_score DESC
        LIMIT 1
    ''', (session['user_id'],))
    
    result = cursor.fetchone()
    conn.close()
    
    if result and result['best_score']:
        best_accuracy = result['best_score']
        best_lang_key = result['language']
        best_language = LANGUAGE_INFO.get(best_lang_key, {}).get('name', best_lang_key.capitalize())
        best_language_icon = LANGUAGE_INFO.get(best_lang_key, {}).get('icon', '🏆')
        best_language_display = f"{best_language_icon} {best_language}"
    else:
        best_accuracy = 0
        best_language_display = "No data yet"
    
    # Get total lesson counts for each language
    lesson_counts = {
        "basics": len(lessons_db.get("basics", [])),
        "python": len(lessons_db.get("python", [])),
        "javascript": len(lessons_db.get("javascript", [])),
        "java": len(lessons_db.get("java", []))
    }
    
    user_data = {
        "username": user['name'],
        "level": progress.get('basics_level', 1),
        "best_accuracy": best_accuracy,
        "best_language": best_language_display,
        "basics_level": progress.get('basics_level', 1),
        "python_level": progress.get('python_level', 1),
        "javascript_level": progress.get('javascript_level', 1),
        "java_level": progress.get('java_level', 1)
    }
    
    return render_template('dashboard.html', 
                         data=user_data, 
                         languages=LANGUAGE_INFO, 
                         lesson_counts=lesson_counts)
@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGE_INFO)

@app.route('/courses/<language>')
def courses(language):
    if language not in lessons_db:
        return "Language not found", 404
    
    user_id = session.get('user_id')
    data = {}
    
    if user_id:
        progress = get_user_progress(user_id)
        data = {
            f"{language}_level": progress.get(f'{language}_level', 1),
            f"{language}_scores": get_all_scores(user_id, language)
        }
    
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
    
    lang_info = LANGUAGE_INFO.get(language, {})
    return render_template('intro.html', lang=language, lang_info=lang_info)

@app.route('/lesson/<language>/<int:lesson_id>')
def lesson(language, lesson_id):
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='lesson'))
    
    if language not in lessons_db:
        return "Language not found", 404
    
    track_lessons = lessons_db.get(language, [])
    current_lesson = next((l for l in track_lessons if l['id'] == lesson_id), None)
    
    if not current_lesson:
        return "Lesson not found", 404
    
    # If it's an exam, redirect to exam page
    if current_lesson.get('is_exam'):
        return redirect(url_for('exam', language=language, lesson_id=lesson_id))
    
    return render_template('lesson.html', lang=language, lesson=current_lesson, lang_info=LANGUAGE_INFO.get(language, {}))

@app.route('/exam/<language>/<int:lesson_id>')
def exam(language, lesson_id):
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='exam'))
    
    if language not in lessons_db:
        return "Language not found", 404
    
    track_lessons = lessons_db.get(language, [])
    current_lesson = next((l for l in track_lessons if l['id'] == lesson_id), None)
    
    if not current_lesson or not current_lesson.get('is_exam'):
        return redirect(url_for('lesson', language=language, lesson_id=lesson_id))
    
    # Check exam type
    if current_lesson.get('exam_type') == 'question':
        # Must have questions
        if not current_lesson.get('questions'):
            return "Exam has no questions", 400
        return render_template('exam_question.html', 
                             lang=language, 
                             lesson=current_lesson,
                             lang_info=LANGUAGE_INFO.get(language, {}))
    else:
        # Regular typing exam (for Basics, etc.)
        return render_template('lesson.html', 
                             lang=language, 
                             lesson=current_lesson,
                             lang_info=LANGUAGE_INFO.get(language, {}))
@app.route('/get_next_lesson/<language>')
def get_next_lesson(language):
    if 'user_id' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    if language not in lessons_db:
        return jsonify({"error": "Language not found"}), 404
    
    user_id = session['user_id']
    progress = get_user_progress(user_id)
    current_level = progress.get(f"{language}_level", 1)
    total_lessons = len(lessons_db.get(language, []))
    
    if current_level > total_lessons:
        current_level = total_lessons
    
    return jsonify({"next_lesson_id": current_level, "total_lessons": total_lessons})

@app.route('/process_stats', methods=['POST'])
def process_stats():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"status": "error", "message": "User not logged in"}), 401
    
    data = request.get_json()
    print("📥 Received data:", data)
    
    lang = data.get('lang', 'basics')
    lesson_id = int(data.get('lesson_id'))
    
    typed_text = data.get('typed_text', '')
    
    # Get target text
    lessons_list = lessons_db.get(lang, [])
    if lesson_id <= len(lessons_list):
        target_text = lessons_list[lesson_id - 1]['target']
    else:
        target_text = ""
    
    # Calculate accuracy using exact method
    from database import calculate_accuracy_exact, normalize_code_for_comparison
    
    typed_normalized = normalize_code_for_comparison(typed_text)
    target_normalized = normalize_code_for_comparison(target_text)
    
    # Get detailed stats
    accuracy, calculated_mistakes, correct_chars = calculate_accuracy_exact(typed_normalized, target_normalized)
    
    # Use provided values or calculated ones
    wpm = int(data.get('wpm', 0))
    mistakes = int(data.get('mistakes', 0))
    total_chars = int(data.get('total_chars', len(target_text)))
    
    # If mistakes weren't provided, use calculated ones
    if mistakes == 0 and calculated_mistakes > 0:
        mistakes = calculated_mistakes
    
    print(f"📊 Calculated accuracy: {accuracy}%, Mistakes: {mistakes}, Correct: {correct_chars}")
    
    # Store results in session
    session['last_results'] = {
        "accuracy": accuracy,
        "wpm": wpm,
        "mistakes": mistakes,
        "total_chars": total_chars,
        "correct_chars": correct_chars,
        "lesson_id": lesson_id,
        "lang": lang
    }
    
    # Save score to database (only if better than previous)
    old_score = get_lesson_score(user_id, lang, lesson_id)
    if accuracy > old_score:
        save_lesson_score(user_id, lang, lesson_id, accuracy, wpm, mistakes)
        print(f"🏆 New best score: {accuracy}% (was {old_score}%)")
    
    # Update level if needed
    lessons_list = lessons_db.get(lang, [])
    lesson_data = lessons_list[lesson_id - 1] if lesson_id <= len(lessons_list) else None
    
    if lesson_data and lesson_data.get("is_exam"):
        required_pass = lesson_data.get("pass_score", 70)
        if accuracy >= required_pass:
            progress = get_user_progress(user_id)
            current_level = progress.get(f"{lang}_level", 1)
            if lesson_id == current_level:
                total_lessons = len(lessons_list)
                if current_level < total_lessons:
                    update_user_progress(user_id, lang, current_level + 1)
                    print(f"⬆️ Level updated to: {current_level + 1} (exam passed)")
    else:
        required_pass = 65
        progress = get_user_progress(user_id)
        current_level = progress.get(f"{lang}_level", 1)
        if accuracy >= required_pass and lesson_id == current_level:
            total_lessons = len(lessons_list)
            if current_level < total_lessons:
                update_user_progress(user_id, lang, current_level + 1)
                print(f"⬆️ Level updated to: {current_level + 1}")
    
    session.modified = True
    return jsonify({"status": "success", "accuracy": accuracy, "wpm": wpm, "mistakes": mistakes})

@app.route('/process_exam_stats', methods=['POST'])
def process_exam_stats():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"status": "error", "message": "User not logged in"}), 401
    
    data = request.get_json()
    print("📥 Received exam data:", data)
    
    lang = data.get('lang', 'javascript')
    lesson_id = int(data.get('lesson_id'))
    accuracy = int(data.get('accuracy', 0))
    wpm = int(data.get('wpm', 0))  # الحصول على WPM من البيانات
    mistakes = int(data.get('mistakes', 0))
    total_chars = int(data.get('total_chars', 0))
    
    print(f"📊 Storing results: accuracy={accuracy}%, wpm={wpm}, mistakes={mistakes}")
    
    # Store results in session
    session['last_results'] = {
        "accuracy": accuracy,
        "wpm": wpm,
        "mistakes": mistakes,
        "total_chars": total_chars,
        "lesson_id": lesson_id,
        "lang": lang
    }
    
    # Save score to database
    old_score = get_lesson_score(user_id, lang, lesson_id)
    if accuracy > old_score:
        save_lesson_score(user_id, lang, lesson_id, accuracy, wpm, mistakes)
        print(f"🏆 New best exam score: {accuracy}% (was {old_score}%)")
    
    # Update level if exam passed
    lessons_list = lessons_db.get(lang, [])
    if lesson_id <= len(lessons_list):
        lesson_data = lessons_list[lesson_id - 1]
        required_pass = lesson_data.get("pass_score", 70)
        
        if accuracy >= required_pass:
            progress = get_user_progress(user_id)
            current_level = progress.get(f"{lang}_level", 1)
            if lesson_id == current_level:
                total_lessons = len(lessons_list)
                if current_level < total_lessons:
                    update_user_progress(user_id, lang, current_level + 1)
                    print(f"⬆️ Level updated to: {current_level + 1} (exam passed)")
    
    session.modified = True
    return jsonify({"status": "success", "accuracy": accuracy, "wpm": wpm})
@app.route('/results/<language>/<int:lesson_id>')
def results(language, lesson_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('index'))
    
    # Get results from session
    res = session.get('last_results', {})
    
    # Get accuracy from session or from URL parameter
    accuracy = res.get('accuracy', 0)
    if accuracy == 0 and request.args.get('accuracy'):
        accuracy = int(request.args.get('accuracy'))
    
    wpm = res.get('wpm', 0)
    mistakes = res.get('mistakes', 0)
    total_chars = res.get('total_chars', 0)
    
    # If still no accuracy, get from database
    if accuracy == 0:
        accuracy = get_lesson_score(user_id, language, lesson_id)
    
    stars = calculate_stars(accuracy)
    
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
    
    if current_lesson and current_lesson.get("is_exam"):
        required_pass = current_lesson.get("pass_score", 70)
        passed = accuracy >= required_pass
    else:
        passed = accuracy >= 70
    
    return render_template('result.html',
                           accuracy=accuracy,
                           total_chars=total_chars,
                           mistakes=mistakes,
                           wpm=wpm,
                           lang=language,
                           lesson_id=lesson_id,
                           lesson_title=current_lesson['title'] if current_lesson else "Lesson Complete",
                           lesson=current_lesson,
                           stars=stars,
                           star_message=messages.get(int(stars), "Keep going!"),
                           passed=passed,
                           total_lessons=len(track_lessons))

@app.route('/achievements')
def achievements():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='achievements'))
    
    user_id = session['user_id']
    user = get_user_by_id(user_id)
    
    # Collect exams from all languages
    all_exams = []
    
    # Languages to process
    languages = ['basics', 'python', 'javascript', 'java']
    
    for lang in languages:
        lessons = lessons_db.get(lang, [])
        lang_info = LANGUAGE_INFO.get(lang, {})
        
        for lesson in lessons:
            if lesson.get('is_exam'):
                best_score = get_lesson_score(user_id, lang, lesson['id'])
                passed = best_score >= lesson.get('pass_score', 70)
                stars = calculate_stars(best_score)
                
                all_exams.append({
                    'language': lang,
                    'language_name': lang_info.get('name', lang.capitalize()),
                    'language_icon': lang_info.get('icon', '📚'),
                    'exam_id': lesson['id'],
                    'exam_number': lesson.get('exam_number', 1),
                    'title': lesson['title'],
                    'pass_score': lesson.get('pass_score', 70),
                    'best_score': best_score,
                    'passed': passed,
                    'stars': stars,
                    'covers': lesson.get('covers_lessons', 'N/A')
                })
    
    # Calculate statistics
    total_exams = len(all_exams)
    passed_exams = sum(1 for ex in all_exams if ex['passed'])
    completion_rate = (passed_exams / total_exams * 100) if total_exams > 0 else 0
    
    # Group exams by language
    exams_by_language = {}
    for exam in all_exams:
        if exam['language'] not in exams_by_language:
            exams_by_language[exam['language']] = {
                'name': exam['language_name'],
                'icon': exam['language_icon'],
                'exams': []
            }
        exams_by_language[exam['language']]['exams'].append(exam)
    
    return render_template('achievements.html',
                         exams_by_language=exams_by_language,
                         total_exams=total_exams,
                         passed_exams=passed_exams,
                         completion_rate=completion_rate,
                         username=user['name'] if user else 'User')

@app.route('/statistics')
def statistics():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='statistics'))
    
    user_id = session['user_id']
    user = get_user_by_id(user_id)
    
    # Get statistics for all languages
    all_stats = get_all_languages_stats(user_id)
    
    # Get weekly data for each language
    languages_data = {}
    for lang in ['basics', 'python', 'javascript', 'java']:
        lang_info = LANGUAGE_INFO.get(lang, {})
        weekly = get_weekly_summary(user_id, lang)
        daily = get_daily_stats(user_id, lang, 7)
        
        # Get lesson history
        lesson_history = get_lesson_history(user_id, lang)
        
        # Calculate averages
        if daily:
            avg_wpm = sum(d['avg_wpm'] for d in daily) / len(daily)
            avg_accuracy = sum(d['avg_accuracy'] for d in daily) / len(daily)
        else:
            avg_wpm = 0
            avg_accuracy = 0
        
        languages_data[lang] = {
            'name': lang_info.get('name', lang.capitalize()),
            'icon': lang_info.get('icon', '📚'),
            'color': lang_info.get('color', '#8b5cf6'),
            'weekly': weekly,
            'daily': daily,
            'avg_wpm': round(avg_wpm, 1),
            'avg_accuracy': round(avg_accuracy, 1),
            'lesson_history': lesson_history[:5]  # Last 5 lessons
        }
    
    # Get overall weekly progress
    all_weekly = []
    for day in range(7):
        date = datetime.now().strftime('%Y-%m-%d')
        # Simplified for demo
        all_weekly.append({'day': day, 'wpm': 0, 'accuracy': 0})
    
    return render_template('statistics.html',
                         username=user['name'] if user else 'User',
                         languages_data=languages_data,
                         all_stats=all_stats)

@app.route('/save_typing_stats', methods=['POST'])
def save_typing_stats_route():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"status": "error", "message": "Not logged in"}), 401
    
    data = request.get_json()
    print(f"📥 Received stats data: {data}")
    
    lang = data.get('language', 'basics')
    wpm = int(data.get('wpm', 0))
    accuracy = int(data.get('accuracy', 0))
    mistakes = int(data.get('mistakes', 0))
    chars_typed = int(data.get('chars_typed', 0))
    
    save_typing_stats(user_id, lang, wpm, accuracy, mistakes, chars_typed)
    
    print(f"✅ Saved typing stats: {lang} - WPM: {wpm}, Accuracy: {accuracy}%")
    
    return jsonify({"status": "success"})
@app.route('/get_wpm_history/<language>')
def get_wpm_history(language):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"history": []})
    
    history = get_typing_history(user_id, language, limit=30)
    
    # Format history for display
    result = []
    for item in history:
        result.append({
            'date': item['date'],
            'avg_wpm': item['avg_wpm'],
            'avg_accuracy': item['avg_accuracy'],
            'total_chars': item['total_chars']
        })
    
    return jsonify({"history": result})
@app.route('/settings')
def settings():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='settings'))
    
    user = get_user_by_id(session['user_id'])
    if not user:
        return redirect(url_for('index'))
    
    user_data = {
        'name': user['name'],
        'email': user['email']
    }
    
    return render_template('settings.html', user=user_data)
@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    
    name = data.get('name', '').strip()
    current_password = data.get('current_password', '')
    new_password = data.get('new_password', '')
    confirm_password = data.get('confirm_password', '')
    
    # Get current user
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    
    if not user:
        conn.close()
        return jsonify({"success": False, "message": "User not found"}), 404
    
    # Verify current password
    if user['password'] != current_password:
        conn.close()
        return jsonify({"success": False, "message": "Current password is incorrect"}), 400
    
    updates = []
    params = []
    
    # Update name if provided
    if name and name != data.get('old_name'):
        updates.append('name = ?')
        params.append(name)
        session['user_name'] = name
    
    # Update password if provided
    if new_password and new_password == confirm_password:
        updates.append('password = ?')
        params.append(new_password)
    
    if not updates:
        conn.close()
        return jsonify({"success": False, "message": "No changes to update"}), 400
    
    params.append(user_id)
    query = f'UPDATE users SET {", ".join(updates)} WHERE id = ?'
    
    cursor.execute(query, params)
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Profile updated successfully!"})
@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    
    user_id = session['user_id']
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Delete all user data (cascade will handle related tables if foreign keys are set)
        cursor.execute('DELETE FROM lesson_scores WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM typing_stats WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM user_progress WHERE user_id = ?', (user_id,))
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        
        # Clear session
        session.clear()
        
        return jsonify({"success": True, "message": "Account deleted successfully"})
    except Exception as e:
        print(f"Error deleting account: {e}")
        return jsonify({"success": False, "message": "An error occurred"}), 500
    finally:
        conn.close()

@app.route('/get_user_best_accuracy')
def get_user_best_accuracy():
    if 'user_id' not in session:
        return jsonify({"best_accuracy": 0})
    
    user_id = session['user_id']
    best_accuracy = 0
    
    for lang in ['basics', 'python', 'javascript', 'java']:
        scores = get_all_scores(user_id, lang)
        if scores:
            lang_best = max(scores.values())
            if lang_best > best_accuracy:
                best_accuracy = lang_best
    
    return jsonify({"best_accuracy": best_accuracy})
@app.route('/change_name', methods=['POST'])
def change_name():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    
    data = request.get_json()
    new_name = data.get('new_name', '').strip()
    password = data.get('password', '')
    
    if not new_name or len(new_name) < 2:
        return jsonify({"success": False, "message": "Name must be at least 2 characters"}), 400
    
    # Verify password
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()
    
    if not user or user['password'] != password:
        conn.close()
        return jsonify({"success": False, "message": "Incorrect password"}), 400
    
    # Update name
    cursor.execute('UPDATE users SET name = ? WHERE id = ?', (new_name, session['user_id']))
    conn.commit()
    conn.close()
    
    session['user_name'] = new_name
    
    return jsonify({"success": True, "message": "Name changed successfully"})


@app.route('/change_password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    
    data = request.get_json()
    current_password = data.get('current_password', '')
    new_password = data.get('new_password', '')
    
    if not new_password or len(new_password) < 4:
        return jsonify({"success": False, "message": "Password must be at least 4 characters"}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()
    
    if not user or user['password'] != current_password:
        conn.close()
        return jsonify({"success": False, "message": "Current password is incorrect"}), 400
    
    cursor.execute('UPDATE users SET password = ? WHERE id = ?', (new_password, session['user_id']))
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Password changed successfully"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
