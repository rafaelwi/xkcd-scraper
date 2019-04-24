# xkcd comic scraper
# github: rafaelwi

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib.request

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

"""
    Main Program
"""
searchStr = 'Image URL'

# Get the page and place into Beautiful Soup Object
raw_html = get_page('https://xkcd.com/2139/')
bs4_html = BeautifulSoup(raw_html, 'html.parser')

# Get only the text from raw_html and then find the image URL
bs4_text = bs4_html.get_text()
start = bs4_text.index(searchStr)
bs4_text = bs4_text[start:]
bs4_text_list = bs4_text.splitlines() # index 0 will be the line containing the image URL
img_url_line = bs4_text_list[0]
img_url = img_url_line.split(' ')[4] # now have the image url
#eop