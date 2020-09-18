from flask import render_template, url_for, request, redirect
from app import app
from .request import get_sources, get_articles

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


@app.route('/articles/<source_id>')    
def articles(source_id):
    articles = get_articles(source_id)
    return render_template('articles.html', title = f"{source_id} page", articles = articles)    