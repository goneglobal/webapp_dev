from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # In production, use environment variable

# Simple user store (in production, use a database)
USERS = {
    'admin': 'password123',
    'user': 'userpass',
    'demo': 'demo'
}

@app.route('/')
def index():
    """Home page - redirects to dashboard if logged in, otherwise shows login"""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page with HTMX form handling"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if this is an HTMX request
        if request.headers.get('HX-Request'):
            # Validate credentials
            if username in USERS and USERS[username] == password:
                session['username'] = username
                # Return success response for HTMX
                return '''
                <div class="alert alert-success" role="alert">
                    Login successful! Redirecting...
                </div>
                <script>
                    setTimeout(() => { window.location.href = '/dashboard'; }, 1000);
                </script>
                '''
            else:
                # Return error message for HTMX
                return '''
                <div class="alert alert-danger" role="alert">
                    Invalid username or password. Please try again.
                </div>
                '''
        else:
            # Handle non-HTMX form submission
            if username in USERS and USERS[username] == password:
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password')
                return render_template('login.html')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Protected dashboard page"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.pop('username', None)
    flash('You have been logged out')
    return redirect(url_for('login'))

@app.route('/status')
def status():
    """HTMX endpoint to check login status"""
    if 'username' in session:
        return f'<span class="text-success">Logged in as: {session["username"]}</span>'
    else:
        return '<span class="text-muted">Not logged in</span>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)