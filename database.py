import sqlite3
import json
from datetime import datetime

DATABASE = 'codekeys.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with tables"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # User progress table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            basics_level INTEGER DEFAULT 1,
            python_level INTEGER DEFAULT 1,
            javascript_level INTEGER DEFAULT 1,
            java_level INTEGER DEFAULT 1,
            total_words INTEGER DEFAULT 0,
            accuracy INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(user_id)
        )
    ''')
    
    # Lesson scores table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lesson_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            language TEXT NOT NULL,
            lesson_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            wpm INTEGER DEFAULT 0,
            mistakes INTEGER DEFAULT 0,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(user_id, language, lesson_id)
        )
    ''')
    
    # Typing statistics table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS typing_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            language TEXT NOT NULL,
            date TEXT NOT NULL,
            total_time INTEGER DEFAULT 0,
            total_chars INTEGER DEFAULT 0,
            total_wpm_sum INTEGER DEFAULT 0,
            total_accuracy_sum INTEGER DEFAULT 0,
            total_mistakes INTEGER DEFAULT 0,
            avg_wpm REAL DEFAULT 0,
            avg_accuracy REAL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(user_id, language, date)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

def save_user(email, name, password):
    """Save a new user to database"""
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (email, name, password) VALUES (?, ?, ?)',
            (email, name, password)
        )
        user_id = cursor.lastrowid
        
        # Create initial progress for user
        cursor.execute(
            'INSERT INTO user_progress (user_id) VALUES (?)',
            (user_id,)
        )
        
        conn.commit()
        return {"success": True, "user_id": user_id}
    except sqlite3.IntegrityError:
        return {"success": False, "message": "Email already exists"}
    finally:
        conn.close()

def get_user(email, password):
    """Get user by email and password"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id, email, name FROM users WHERE email = ? AND password = ?',
        (email, password)
    )
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

def get_user_by_id(user_id):
    """Get user by ID"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, email, name FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

def get_user_progress(user_id):
    """Get user progress for all languages"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT basics_level, python_level, javascript_level, java_level, 
                  total_words, accuracy 
           FROM user_progress WHERE user_id = ?''',
        (user_id,)
    )
    progress = cursor.fetchone()
    conn.close()
    return dict(progress) if progress else {}

def update_user_progress(user_id, language, level):
    """Update user level for a specific language"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        f'UPDATE user_progress SET {language}_level = ?, updated_at = CURRENT_TIMESTAMP WHERE user_id = ?',
        (level, user_id)
    )
    conn.commit()
    conn.close()

def get_lesson_score(user_id, language, lesson_id):
    """Get the best score for a lesson"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT score FROM lesson_scores WHERE user_id = ? AND language = ? AND lesson_id = ?',
        (user_id, language, lesson_id)
    )
    score = cursor.fetchone()
    conn.close()
    return score['score'] if score else 0

def save_lesson_score(user_id, language, lesson_id, score, wpm, mistakes):
    """Save or update lesson score"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if exists
    cursor.execute(
        'SELECT score FROM lesson_scores WHERE user_id = ? AND language = ? AND lesson_id = ?',
        (user_id, language, lesson_id)
    )
    existing = cursor.fetchone()
    
    if existing:
        # Update only if new score is higher
        if score > existing['score']:
            cursor.execute(
                '''UPDATE lesson_scores 
                   SET score = ?, wpm = ?, mistakes = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE user_id = ? AND language = ? AND lesson_id = ?''',
                (score, wpm, mistakes, user_id, language, lesson_id)
            )
    else:
        # Insert new record
        cursor.execute(
            '''INSERT INTO lesson_scores (user_id, language, lesson_id, score, wpm, mistakes) 
               VALUES (?, ?, ?, ?, ?, ?)''',
            (user_id, language, lesson_id, score, wpm, mistakes)
        )
    
    conn.commit()
    conn.close()

def get_all_scores(user_id, language):
    """Get all scores for a language"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT lesson_id, score, wpm, mistakes FROM lesson_scores WHERE user_id = ? AND language = ?',
        (user_id, language)
    )
    scores = cursor.fetchall()
    conn.close()
    return {str(s['lesson_id']): s['score'] for s in scores}

def save_typing_stats(user_id, language, wpm, accuracy, mistakes, chars_typed):
    """Save daily typing statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    print(f"💾 Saving typing stats for {today}: {language} - WPM: {wpm}, Acc: {accuracy}%")
    
    # Check if entry exists for today
    cursor.execute('''
        SELECT id, total_time, total_chars, total_wpm_sum, total_accuracy_sum, total_mistakes
        FROM typing_stats 
        WHERE user_id = ? AND language = ? AND date = ?
    ''', (user_id, language, today))
    
    existing = cursor.fetchone()
    
    if existing:
        # Update existing record
        new_total_chars = existing['total_chars'] + chars_typed
        new_wpm_sum = existing['total_wpm_sum'] + wpm
        new_accuracy_sum = existing['total_accuracy_sum'] + accuracy
        new_mistakes = existing['total_mistakes'] + mistakes
        new_total_time = existing['total_time'] + 1
        
        cursor.execute('''
            UPDATE typing_stats 
            SET total_chars = ?, total_wpm_sum = ?, total_accuracy_sum = ?, 
                total_mistakes = ?, total_time = ?, avg_wpm = ?, avg_accuracy = ?
            WHERE user_id = ? AND language = ? AND date = ?
        ''', (
            new_total_chars, new_wpm_sum, new_accuracy_sum, 
            new_mistakes, new_total_time,
            new_wpm_sum / new_total_time, new_accuracy_sum / new_total_time,
            user_id, language, today
        ))
        print(f"📊 Updated existing record for {today}")
    else:
        # Insert new record
        cursor.execute('''
            INSERT INTO typing_stats 
            (user_id, language, date, total_time, total_chars, 
             total_wpm_sum, total_accuracy_sum, total_mistakes, avg_wpm, avg_accuracy)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id, language, today, 1, chars_typed,
            wpm, accuracy, mistakes, wpm, accuracy
        ))
        print(f"📊 Created new record for {today}")
    
    conn.commit()
    conn.close()

def get_daily_stats(user_id, language, days=7):
    """Get daily statistics for last N days"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT date, avg_wpm, avg_accuracy, total_chars, total_mistakes, total_time
        FROM typing_stats 
        WHERE user_id = ? AND language = ? 
        ORDER BY date DESC LIMIT ?
    ''', (user_id, language, days))
    
    stats = cursor.fetchall()
    conn.close()
    return [dict(s) for s in stats]

def get_weekly_summary(user_id, language):
    """Get weekly summary of progress (last 7 days only)"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Get last 7 days stats
    cursor.execute('''
        SELECT date, avg_wpm, avg_accuracy, total_chars, total_mistakes, total_time
        FROM typing_stats 
        WHERE user_id = ? AND language = ? 
        AND date >= date('now', '-7 days')
        ORDER BY date ASC
    ''', (user_id, language))
    
    weekly = cursor.fetchall()
    conn.close()
    
    if weekly and len(weekly) > 0:
        # Calculate improvement
        first_day = weekly[0]
        last_day = weekly[-1]
        
        wpm_improvement = last_day['avg_wpm'] - first_day['avg_wpm']
        accuracy_improvement = last_day['avg_accuracy'] - first_day['avg_accuracy']
        
        # Calculate totals
        total_chars = sum(s['total_chars'] for s in weekly)
        total_mistakes = sum(s['total_mistakes'] for s in weekly)
        
        return {
            'weekly_data': [dict(s) for s in weekly],
            'wpm_improvement': wpm_improvement,
            'accuracy_improvement': accuracy_improvement,
            'total_chars': total_chars,
            'total_mistakes': total_mistakes,
            'best_wpm': max(s['avg_wpm'] for s in weekly),
            'best_accuracy': max(s['avg_accuracy'] for s in weekly)
        }
    
    return None

def get_all_languages_stats(user_id):
    """Get statistics for all languages"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT language, 
               AVG(avg_wpm) as avg_wpm,
               AVG(avg_accuracy) as avg_accuracy,
               SUM(total_chars) as total_chars,
               SUM(total_mistakes) as total_mistakes,
               MAX(avg_wpm) as best_wpm,
               MAX(avg_accuracy) as best_accuracy
        FROM typing_stats 
        WHERE user_id = ?
        GROUP BY language
    ''', (user_id,))
    
    stats = cursor.fetchall()
    conn.close()
    return [dict(s) for s in stats]

def get_lesson_history(user_id, language):
    """Get lesson completion history for progress tracking"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT lesson_id, score, wpm, mistakes, completed_at
        FROM lesson_scores 
        WHERE user_id = ? AND language = ?
        ORDER BY completed_at DESC LIMIT 20
    ''', (user_id, language))
    
    history = cursor.fetchall()
    conn.close()
    return [dict(h) for h in history]

def get_typing_history(user_id, language=None, limit=30):
    """Get typing history for user (all past data for WPM history)"""
    conn = get_db()
    cursor = conn.cursor()
    
    if language:
        cursor.execute('''
            SELECT date, avg_wpm, avg_accuracy, total_chars, total_mistakes
            FROM typing_stats 
            WHERE user_id = ? AND language = ?
            ORDER BY date DESC LIMIT ?
        ''', (user_id, language, limit))
    else:
        cursor.execute('''
            SELECT date, language, avg_wpm, avg_accuracy, total_chars, total_mistakes
            FROM typing_stats 
            WHERE user_id = ?
            ORDER BY date DESC LIMIT ?
        ''', (user_id, limit))
    
    history = cursor.fetchall()
    conn.close()
    return [dict(h) for h in history]

def get_all_typing_history(user_id):
    """Get all typing history grouped by date for dashboard"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT date, language, avg_wpm, avg_accuracy, total_chars, total_mistakes
        FROM typing_stats 
        WHERE user_id = ?
        ORDER BY date DESC
    ''', (user_id,))
    
    history = cursor.fetchall()
    conn.close()
    return [dict(h) for h in history]
def calculate_accuracy_exact(user_text, target_text):
    """
    Calculate exact character-by-character accuracy.
    Returns: (accuracy_percentage, mistakes_count, correct_chars)
    """
    user_text = user_text.rstrip('\n')
    target_text = target_text.rstrip('\n')
    
    # Normalize spaces (but preserve indentation)
    # Convert different newline types to \n
    user_text = user_text.replace('\r\n', '\n').replace('\r', '\n')
    target_text = target_text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Calculate character by character
    mistakes = 0
    correct = 0
    
    max_len = max(len(user_text), len(target_text))
    
    for i in range(max_len):
        user_char = user_text[i] if i < len(user_text) else ''
        target_char = target_text[i] if i < len(target_text) else ''
        
        if user_char == target_char:
            correct += 1
        else:
            mistakes += 1
    
    # Accuracy = correct / target length
    if len(target_text) == 0:
        return 100, 0, 0
    
    accuracy = int((correct / len(target_text)) * 100)
    accuracy = max(0, min(100, accuracy))
    
    return accuracy, mistakes, correct


def normalize_code_for_comparison(code):
    """
    Normalize code for comparison (handles quotes, spaces, newlines)
    """
    # Normalize quotes
    code = code.replace('"', '"').replace('"', '"')
    code = code.replace("'", "'").replace("'", "'")
    
    # Normalize newlines
    lines = code.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    
    # Remove trailing spaces from each line but preserve indentation
    lines = [line.rstrip() for line in lines]
    
    # Remove empty lines at the end
    while lines and lines[-1] == '':
        lines.pop()
    
    return '\n'.join(lines)
def get_user_best_accuracy(user_id):
    """Get the user's best accuracy across all lessons"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT MAX(score) as best_score 
        FROM lesson_scores 
        WHERE user_id = ?
    ''', (user_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    return result['best_score'] if result and result['best_score'] else 0