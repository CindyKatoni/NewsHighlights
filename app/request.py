from app import app
import urllib.request,json
from .models.news import Sources, Articles

# News = news.News

# Getting api key
apiKey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources(source):
    """
    Function to retrieve news sources list from the News API
    """
    get_sources_url = base_url+source+'?apiKey='+apiKey
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """Function that process the results list and transforms them into a list of objects
    Args: sources_list: A list of dictionaries that contains news sources details
    Returns:
    sources_results: a list of news sources objects"""

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        source_object = Sources(id, name, description, url)
        sources_results.append(source_object)

    return sources_results



def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/sources?&apiKey={}&language=en'.format(apiKey, id)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)


    return articles_results

def process_articles(article_list):
    '''
    Function that processes the article results and transform them to a list of objects
    '''
    articles_results = []

    for article_item in article_list:
        source = article_item.get('source')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')

        article_object = Articles(source, title, description, url, urlToImage)
        article_results.append(article_object)

    return articles_results

