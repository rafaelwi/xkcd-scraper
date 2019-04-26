# xkcd comic scraper
# github: rafaelwi

# Imports
import sys
import random
import functs as xkcd

"""
    Main Program
"""
# Get the latest xkcd value
latest = xkcd.get_latest()

# Randomly generate a number
random_comic = random.randint(1, int(latest))
random_comic_url = "https://xkcd.com/" + str(random_comic) + "/"

# Get image URL
img_url = xkcd.get_img_url(random_comic_url)

# Download image URL
xkcd.download_img(random_comic_url, img_url)