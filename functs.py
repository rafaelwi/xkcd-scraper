# xkcd comic scraper
# github: rafaelwi

# Imports
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib.request
import sys

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
log_message(m): Prints out the message passed in. Used for debugging
In
    m: A message
Out: The message
"""
def log_message(m):
    print (m)


def get_url(args):
    # Check number of args passed in
    # If there are not 2 args, then exit
    if len(args) != 2:
        log_message ("Usage: python3 main.py <xkcd url>")
        sys.exit()
    # Otherwise, take the 2nd arg as the url
    else:
        raw_url = args[1]

    # Verify that the URL is valid
    if (raw_url.split('/')[2] != "xkcd.com") |  (not (raw_url.split('/')[3]).isdecimal()):
        log_message ("Error: URL is formatted incorrectly")
        sys.exit()

    log_message ("Got URL: " + raw_url)
    return raw_url
