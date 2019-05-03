# xkcdownloader
xkcd comic scraper script in python3

# Features
- Can download xkcd comics from a link
- Can download random xkcd comics
- Can batch download xkcd comics


# Running
1. Clone the repo using `git clone https://github.com/rafaelwi/xkcdownloader.git`
2. Ensure that you have `requests`, `lxml`, and `beautifulsoup4` dependencies installed with `pip3`
3. Run the script
4. Find the images downloaded in the `imgs` folder

## Using the script

To get a specific comic: 
`python3 xkcdownloader.py https://xkcd.com/1234/`  or  `python3 xkcdownloader.py 1234`

To get a random comic:
`python3 xkcdownloader.py random`

To get the latest comic:
`python3 xkcdownloader.py latest`

#### Batch Downloading

Batch download all comics:
`python3 xkcdownloader.py batch all`

Batch download the first 100 comics:
`python3 xkcdownloader.py batch 1 100`

Batch download from the 2000th comic to the most recent:
 `python3 xkcdownloader.py batch 2000`


# To add
- ~~Ability to download comics from just their number~~
- ~~Ability to get the latest comic~~
- ~~Update function comments to PEP8 standards~~
- ~~Batch download function~~
- ~~Batch download starting from a specific comic to the newest one~~
- Ability to configure where the images are downloaded
- Speed optimizations with getting the webpage
- Ability to display image downloaded in terminal (?)
