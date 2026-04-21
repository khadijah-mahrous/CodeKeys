from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this_12345'

# User database
users_db = {}
user_progress = {}

# Lesson database
lessons_db = {
    "basics": [
        {"id": 1, "title": "Home Row: F & J", "target": "ffff jjjj", "instr": "Focus on your index fingers."},
        {"id": 2, "title": "Home Row: D & K", "target": "dddd kkkk", "instr": "Focus on your middle fingers."}
    ],
    "python": [
        {"id": 1, "title": "Output", "target": "print('Hello World')", "instr": "The print() function outputs text to the console."},
        {"id": 2, "title": "Variables", "target": "user_val = input()", "instr": "input() captures user data into a variable."}
    ],
    "javascript": [
        {"id": 1, "title": "Output", "target": "console.log('Hello');", "instr": "console.log() is used to print debugging info."},
        {"id": 2, "title": "Variables", "target": "let val = prompt();", "instr": "let declares a variable."}
    ],
    "java": [
        {"id": 1, "title": "Output", "target": "System.out.println();", "instr": "Standard way to print a line in Java."},
        {"id": 2, "title": "Variables", "target": "Scanner in = new Scanner();", "instr": "The Scanner class is used for input."}
    ]
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
    
    user_progress[email] = {
        "username": name,
        "email": email,
        "level": 1,
        "total_words": 0,
        "accuracy": 0,
        "problem_keys": []
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
        # Change jsonify to redirect
        return redirect(url_for('index', login_required='dashboard'))
    
    # Fetch the latest user data, ensuring level defaults to 1 if it's a new user
    user_data = user_progress.get(session['user_id'], {
        "username": session.get('user_name', 'User'),
        "level": 1,
        "accuracy": 0
    })
    return render_template('dashboard.html', data=user_data)

@app.route('/')
def index():
    user_id = session.get('user_id')
    # If logged in, get their level. If not, default to 1.
    user_data = user_progress.get(user_id, {"level": 1}) if user_id else {"level": 1}
    return render_template('index.html', data=user_data)

@app.route('/courses/<language>')
def courses(language):
    user_id = session.get('user_id')
    # Default to level 1 and empty scores if no data exists yet
    data = user_progress.get(user_id, {"level": 1, "lesson_scores": {}}) if user_id else {"level": 1}
    
    lang_lessons = lessons_db.get(language, [])
    return render_template('courses.html', lessons=lang_lessons, lang=language, data=data)

@app.route('/intro/<language>')
def language_intro(language):
    user_id = session.get('user_id')
    data = user_progress.get(user_id, {"level": 1}) if user_id else {"level": 1}
    
    descriptions = {
        "python": "Python is a powerful language used for AI.",
        "javascript": "JavaScript is the language of the web.", 
        "java": "Java is used for enterprise apps."
    }
    desc = descriptions.get(language, "Explore coding.")
    return render_template('intro.html', lang=language, description=desc, data=data)

@app.route('/lesson/<language>/<int:lesson_id>')
def lesson(language, lesson_id):
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='lesson'))
        
    user_id = session['user_id']
    data = user_progress.get(user_id, {"level": 1})
    
    # Use .get(language) so it searches the specific track (python, java, etc.)
    track_lessons = lessons_db.get(language, [])
    current_lesson = next((l for l in track_lessons if l['id'] == lesson_id), None)
    
    if not current_lesson:
        return "Lesson not found", 404
        
    return render_template('lesson.html', lang=language, lesson=current_lesson, data=data)
user_progress = {} 

@app.route('/process_stats', methods=['POST'])
def process_stats():
    data = request.get_json()
    email = session.get('user_id')
    
    lang = data.get('lang', 'basics')
    lesson_id = int(data.get('lesson_id'))
    new_acc = data.get('accuracy', 0)
    wpm = data.get('wpm', 0)
    mistakes = data.get('mistakes', 0)
    total_chars = data.get('total_chars', 0)

    if email in user_progress:
        # Save for Result page
        session['last_results'] = {
            "accuracy": new_acc, 
            "wpm": wpm, 
            "mistakes": mistakes,
            "total_chars": total_chars
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

        # Progression logic
        current_level = user_progress[email].get(level_key, 1)
        if new_acc >= 70 and lesson_id == current_level:
            user_progress[email][level_key] = current_level + 1
            
        session.modified = True
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 404
@app.route('/resume')
def resume_learning():
    if 'user_id' not in session:
        return redirect(url_for('index', login_required='lesson'))
    
    user_data = user_progress.get(session['user_id'], {"level": 1})
    current_level = user_data.get('level', 1)
    
    # This automatically picks up exactly where the user left off
    return redirect(url_for('lesson', language='python', lesson_id=current_level))

@app.route('/results/<language>/<int:lesson_id>')
def results(language, lesson_id):
    res = session.get('last_results', {"accuracy": 0, "total_chars": 0, "mistakes": 0})
    return render_template('result.html', 
                           accuracy=res['accuracy'], 
                           total_chars=res['total_chars'],
                           mistakes=res['mistakes'],
                           lang=language,
                           lesson_id=lesson_id)
if __name__ == '__main__':
    app.run(debug=True)