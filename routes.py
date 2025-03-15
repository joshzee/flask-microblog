from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshua'}
    posts = [
        {
            'author': {'username': 'Joey'},
            'body': 'Grand time in Melbourne'
        },
        {
            'author': {'username': 'Bobby'},
            'body': 'A closer look at HTMX'
        },
        {
            'author': {'username': 'Lisa'},
            'body': 'What\'s up with DevOps?'
        }        
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)