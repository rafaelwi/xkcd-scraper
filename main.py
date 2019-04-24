# xkcd comic scraper
# github: rafaelwi

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

"""
    Main Program
"""
searchStr = 'Image URL'

# Check if the number of args entered is correct
if len(sys.argv) != 2:
    print ("Usage: python3 main.py <xkcd url>")
    sys.exit()
else: 
    raw_url = sys.argv[1]
    log_message ("Got URL: " + raw_url)

    # TODO: Validate that a URL entered is in the valid format of
    # "https://xkcd.com/wxyz/"

# Get the page and place into Beautiful Soup Object
raw_html = get_page(raw_url)
bs4_html = BeautifulSoup(raw_html, 'html.parser')
log_message ("Got page")

# Get only the text from raw_html and then find the image URL
bs4_text = bs4_html.get_text()
start = bs4_text.index(searchStr)
bs4_text = bs4_text[start:]
bs4_text_list = bs4_text.splitlines() # index 0 will be the line containing the image URL
img_url_line = bs4_text_list[0]
img_url = img_url_line.split(' ')[4] # now have the image url

# Create the filename
filename = "imgs/" + raw_url.split('/')[3] + ".png"

# Download the image
urllib.request.urlretrieve(img_url, filename)
log_message ("Saved image from URL <" + raw_url + "> as " + filename)
