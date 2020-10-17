from app import app 
import urllib.request,json
from .models import news

News = news.News

#instance to get the API key

api_key = app.config['NEWS_API_KEY']

#instance to get the base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):

    '''
    This function gets the json response to my url request
    '''

    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    
    '''
    This function processes the results and transforms them to become into a list of objects
    

    Args:
        news_list: A list of dictionaries that contains the news details

    Returns :
        news_results: A list of news objects
    '''

    news_results = []

    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')

    return news_results
