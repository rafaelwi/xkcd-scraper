# xkcdownloader_functions.py
# github: rafaelwi

# Imports
from requests.exceptions import RequestException
from requests import get
from contextlib import closing
from bs4 import BeautifulSoup
import urllib.request
import random
import sys


"""Prints out the message passed in. Used for debugging

Args:
    m: A message

Returns: 
    the message
"""
def log_message(m):
    print (m)
# end log_message(m)


"""Gets the url and verifies that it is valid

Args:
    args: List of arguements from the command line

Returns: 
    the URL entered
"""
def get_raw_url(args):
    # Check number of args passed in
    # If there is not 2 args passed in
    if len(args) != 2:
        log_message("Usage: python3 xkcdownloader.py <xkcd url> | python3 xkcdownlaoder.py random | python3 xkcdownloader.py <xkcd number>")
        sys.exit()
    # If there are 2 args passed in
    else:
        # Check what was passed in
        # Check if 'rand' or 'random' was passed in
        if args[1].lower() in ('rand', 'random'):
            raw_url = get_random_comic_url()

        # If 'new' or 'newest' or 'latest' is passed in
        elif args[1].lower() in ('new', 'newest', 'latest'):
            raw_url = get_latest_comic_url()
        
        # If just a number is passed in
        elif args[1].isdecimal():
            raw_url = 'https://xkcd.com/' + args[1] + '/'

        # If two arguments are passed in and cannot be split up as a link
        elif (args[1].split('/')[2] != 'xkcd.com') | (not (args[1].split('/')[3].isdecimal())):
            log_message("Error: Ending execution due to invalid input")
            log_message("Usage: python3 xkcdownloader.py <xkcd url> | python3 xkcdownlaoder.py random | python3 xkcdownloader.py <xkcd number>")
            sys.exit()
            
        # Otherwise, whatever arguement that has been passed in will be a valid link
        else:
                raw_url = args[1]
    return raw_url
# end get_raw_url(args)


"""Gets a random comic URL

Returns:
    the URL of a random comic
"""
def get_random_comic_url():
    # Get the latest xkcd value
    latest = get_latest()

    # Randomly generate a number
    random_comic = random.randint(1, int(latest))
    raw_url = 'https://xkcd.com/' + str(random_comic) + '/'
    log_message ("Got URL: random comic")
    return raw_url
# end get_random_comic_url()


"""Gets the URL of the latest comic

Returns:
    the URL of the latest comic
"""
def get_latest_comic_url():
    # Get the latest xkcd value
    latest = get_latest()

    # Create URL
    raw_url = 'https://xkcd.com/' + str(latest) + '/'
    log_message ("Got URL: " + raw_url)
    return raw_url
# end get_latest_comic_url()


"""Validates that the URL passed from the command line is valid

Args:
    url: URL of the page that contains the xkcd comic

Returns:
    nothing if the comic is valid or exits otherwise
"""
def validate_url(url):
    # Get the latest value for the comic
    latest_comic = get_latest()

    # Get the number from the URL
    comic_value = url.split('/')[3]

    if ((int(comic_value) > int(latest_comic)) | (int(comic_value) <= 0)):
        log_message("Error: Ending execution due to comic not being in valid range")
        sys.exit()
    else:
        return
# end validate_url(url)


"""Gets the number of the latest xkcd comic

Returns: 
    the number of the latest xkcd comic
"""
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
# end get_latest()


"""Gets the image URL from the page of the URL passed in

Args:
    raw_url: URL of page that will be searched

Returns: 
    the URL of the image
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
# end get_img_url(raw_url)


"""Gets the page source of a requested website
Args:
    url: The URL of the page that the source will be taken from
Returns: 
    the source code of the URL passed in
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
# end get_page(url)


"""Checks if the response from the URL is good

Args:
    resp: Respond from website of connection status

Returns: 
    true if a successful connection has been made and false otherwise
"""
def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)
# end is_good_response(resp)


"""Downloads the image located at img_url

Args:
    raw_url: Used for determining filename
    img_url: URL of image to be downloaded

Returns: 
    no value; saves the image that is located at the URL passed in by img_url
"""
def download_img(raw_url, img_url):
    # Create filename
    filename = "imgs/" + raw_url.split('/')[3] + ".png"

    # Download the image
    urllib.request.urlretrieve(img_url, filename)
    log_message ("Saved image from URL <" + raw_url + "> as " + filename)
# end download_img(raw_url, img_url)