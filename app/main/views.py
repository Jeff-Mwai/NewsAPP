from flask import render_template
# from app import app
from . import main
from ..request import get_news_category, get_news


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #method to get the news
    entertainment_news = get_news_category('entertainment')
    business_news = get_news_category('business')
    health_news = get_news_category('health')
    science_news = get_news_category('science')
    technology_news = get_news_category('technology')


    title = 'Home, welcome to my News app, created by your\'s truly'
    return render_template('index.html', title = title, entertainment = entertainment_news, business = business_news, health = health_news, science = science_news, technology = technology_news)


@main.route('/sources/<id>')
def articles(id):

    my_news = get_news(id)
    title = articles
    return render_template('articles.html', myNews = my_news, title = title)


@main.route('/news/<int:news_id>')
def news(news_id):
    '''
    It views the page of the news and returns the details of the news and the data
    '''

    return render_template('news.html', id = news_id)