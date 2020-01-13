from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Alex'}
    posts = [
        {
            'author': {'username': 'Mary'},
            'body': "That darn Peter Parker!"
        },
        {
            'author': {'username': 'Jane'},
            'body': "I think Peter Parker's pretty cute."
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts = posts)
