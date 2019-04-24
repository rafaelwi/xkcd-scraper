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
            log_message('Error during requests to {0} : {1}'.format(url, str(e)))
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
log_message(m): Prints out the message passed in. Used for debugging
In
    m: A message
Out: The message
"""
def log_message(m):
    print (m)


"""
    get_raw_url(args): Gets the url and verifies that it is valid
In
    args: List of arguements
Out: Returns the URL entered
"""
def get_raw_url(args):
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


"""
get_img_url: Gets the image URL from the page of the URL passed in
In
    raw_url: URL of page that will be searched
Out: Returns the URL of the image
"""
def get_img_url(raw_url):
    # Get the page and place into BeautifulSoup object
    raw_html = get_page(raw_url)
    bs4_html = BeautifulSoup(raw_html, 'html.parser')
    log_message("Got page from URL <" + raw_url + ">")

    # Get only the text from bs4_html
    bs4_text = bs4_html.get_text()
    img_url_location = bs4_text.index('Image URL') # 'Image URL is what we are searching for in the text
    bs4_text = bs4_text[img_url_location:]
    bs4_text_list = bs4_text.splitlines()

    # Get line that has the image URL and return it
    img_url_line = bs4_text_list[0]
    img_url = img_url_line.split(' ')[4]

    return img_url


"""
download_img(raw_url, img_url): Downloads the image located at img_url
In:
    raw_url: Used for determining filename
    img_url: URL of image to be downloaded
Out: None
"""
def download_img(raw_url, img_url):
    # Create filename
    filename = "imgs/" + raw_url.split('/')[3] + ".png"

    # Download the image
    urllib.request.urlretrieve(img_url, filename)
    log_message ("Saved image from URL <" + raw_url + "> as " + filename)


def get_latest():
    # Get the page and place into BeautifulSoup object
    raw_html = get_page("https://xkcd.com/")
    bs4_html = BeautifulSoup(raw_html, 'html.parser')

    # Get only the text from bs4_html
    bs4_text = bs4_html.get_text()
    latest_url_location = bs4_text.index('Permanent')
    bs4_text = bs4_text[latest_url_location:]
    bs4_text_list = bs4_text.splitlines()

    # Get the line that has the image URL and return it
    latest_url_line = bs4_text_list[0]
    latest_value = latest_url_line.split('/')[3]


    # Return the value
    return latest_value
