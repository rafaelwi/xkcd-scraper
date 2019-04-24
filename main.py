# xkcd comic scraper
# github: rafaelwi

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

"""
get_page(url): Gets the page source of a requested website
In
    url: The URL of the page that the source will be taken from
Out: Returns the source code of the URL passed in
"""
def get_page(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


"""
is_good_response(resp): Checks if the response from the URL is good
In
    resp: Respond from website of connection status
Out: Returns true if a successful connection has been made and false otherwise
"""
def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

"""
log_error(e): Prints an error from exception
In
    e: An exception
Out: Prints the expception that has occured
"""
def log_error(e):
    print(e)

searchStr = 'embedding'
got_page = get_page('https://xkcd.com/2139/')
wp = BeautifulSoup(got_page, 'html.parser')
print (wp.prettify())

