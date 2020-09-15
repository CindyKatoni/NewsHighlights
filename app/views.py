from flask import render_template, url_for
from app import app
from .request import get_sources

# Create put index page view function
# Views
@app.route('/')
@app.route('/home')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting News Sources
    news_sources = get_sources('sources')
    return render_template('index.html', sources = news_sources)


@app.route("/article")    
def article():
    return render_template('article.html', title='Articles')    