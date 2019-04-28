# xkcdownloader.py: xkcd comic scraper script
# github: rafaelwi

# Imports
import sys
import xkcdownloader_functs as xkcd

"""
    Main Program
"""
# Get raw URL
raw_url = xkcd.get_raw_url(sys.argv)

# Validate URL
xkcd.validate_url (raw_url)

# Get image URL
img_url = xkcd.get_img_url(raw_url)

# Download image
xkcd.download_img(raw_url, img_url)