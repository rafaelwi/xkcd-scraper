# xkcd comic scraper
# github: rafaelwi

# Imports
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib.request
import sys
import functs as xkcd

"""
    Main Program
"""
## Variables ##
searchStr = 'Image URL'

# Get URL
raw_url = xkcd.get_url(sys.argv)

# Get the page and place into Beautiful Soup Object
raw_html = xkcd.get_page(raw_url)
bs4_html = BeautifulSoup(raw_html, 'html.parser')
xkcd.log_message ("Got page")

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
xkcd.log_message ("Saved image from URL <" + raw_url + "> as " + filename)
