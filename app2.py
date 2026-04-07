import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret")  # Change this to a random secret key

# User storage (in a real app, use a database like SQLAlchemy)
users = {
    "admin": {
        "password": generate_password_hash("geoaid"),
        "name": "Admin"
    }
}

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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        name = request.form.get('name', username)  # Optional name field
        
        # Validation checks
        if username in users:
            flash('Username already exists', 'danger')
        elif len(username) < 4:
            flash('Username must be at least 4 characters', 'danger')
        elif len(password) < 6:
            flash('Password must be at least 6 characters', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match', 'danger')
        else:
            # Create new user
            users[username] = {
                "password": generate_password_hash(password),
                "name": name
            }
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