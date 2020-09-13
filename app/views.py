from flask import render_template, url_for
from app import app

# Create put index page view function
# Views
@app.route('/')
@app.route('/home')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route("/article")    
def article():
    return render_template('article.html', title='Articles')    