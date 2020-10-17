from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home, welcome to my News app, created by your\'s truly'
    return render_template('index.html', title = title)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    It views the page of the news and returns the details of the news and the data
    '''

    return render_template('news.html', id = news_id)