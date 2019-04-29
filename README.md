# xkcdownloader
xkcd comic scraper script in python3

# Features
- Can download xkcd comics from a link
- Can download random xkcd comics


# Running
1. Clone the repo using `git clone https://github.com/rafaelwi/xkcdownloader.git`
2. Ensure that you have both `requests` and `beautifulsoup4` dependencies installed with `pip3`
3. Run the script
4. Find the images downloaded in the `imgs` folder

## Using the script

To get a specific comic: 
`python3 xkcdownloader.py https://xkcd.com/1234/` or `python3 xkcdownloader.py 1234`

To get a random comic:
`python3 xkcdownloader.py random`

To get the latest comic:
`python3 xkcdownloader.py latest`


# To add
- ~~Ability to download comics from just their number~~
- ~~Ability to get the latest comic~~
- Ability to configure where the images are downloaded
- ~~Update function comments to PEP8 standards~~
- Batch download function
- Ability to display image downloaded in terminal (?)
