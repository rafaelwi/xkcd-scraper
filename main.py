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
#searchStr = 'Image URL'

# Get raw URL
raw_url = xkcd.get_raw_url(sys.argv)

# Get image URL
img_url = xkcd.get_img_url(raw_url)

# Create the filename
filename = "imgs/" + raw_url.split('/')[3] + ".png"

# Download the image
urllib.request.urlretrieve(img_url, filename)
xkcd.log_message ("Saved image from URL <" + raw_url + "> as " + filename)
