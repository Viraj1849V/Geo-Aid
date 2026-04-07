import os
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret")

USERS_FILE = os.path.join(app.root_path, "users.json")


def load_users():
    """Load users from JSON storage, safely handling first-run and malformed files."""
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return {}
            data = json.loads(content)
            return data if isinstance(data, dict) else {}
    except FileNotFoundError:
        # Ensure first-run compatibility by creating the file lazily.
        save_users({})
        return {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_users(users):
    """Persist users dictionary to JSON storage."""
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=2)
    except OSError:
        # Keep app flow safe even if storage is temporarily unavailable.
        pass

users = load_users()

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/resource')
def resource():
    return render_template('resource.html')

@app.route('/live-news')
def live_news():
    return render_template('live_news.html')

@app.route('/geolocation')
def geolocation():
    return render_template('geolocation.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/donation')
def donation():
    return render_template('Donation.html')

@app.route('/donation-alt')
def donation_alt():
    return render_template('Donationnn.html')

@app.route('/volunteering')
def volunteering():
    return render_template('volunteering.html')

@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'])

@app.route('/edit-profile')
def edit_profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('edit-profile.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Username and password are required', 'danger')
            return render_template('login.html')

        current_users = load_users()
        
        if username in current_users and check_password_hash(current_users[username].get('password', ''), password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        name = request.form.get('name', username)  # Optional name field
        current_users = load_users()
        
        # Validation checks
        if not username or not password:
            flash('Username and password are required', 'danger')
        elif username in current_users:
            flash('Username already exists', 'danger')
        elif len(username) < 4:
            flash('Username must be at least 4 characters', 'danger')
        elif len(password) < 6:
            flash('Password must be at least 6 characters', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match', 'danger')
        else:
            # Create new user
            current_users[username] = {
                "password": generate_password_hash(password),
                "name": name
            }
            save_users(current_users)

            # Keep in-memory cache aligned for current process.
            global users
            users = current_users

            flash('Registration successful! Please login', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route("/get-news")
def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?q=disaster&apiKey={api_key}"
    
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)