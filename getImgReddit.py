import random
import shutil
from sys import exit
try:
    import requests
except ImportError:
    print('Requests must be installed. PLease run: pip install requests')
    exit()

SUBREDDITS_TO_MONITOR = ["2meirl4meirl", "BikiniBottomTwitter", "dank_meme", "dankmemes", "DeepFriedMemes", "meirl", "memes",
                        "okbuddyretard", "SquarePosting"]
IMG_DIR = "img/"
URL_SR = "https://www.reddit.com/r/"

# Get a random subreddit from the array
def get_randomSubreddit(arrayOfSubreddits):
    return (random.randrange(0, len(arrayOfSubreddits)-1, 1))
# Convert subreddit URL to be read as a .json
def createUrl(subreddit):
    url = subreddit.split('/.json')[0] + "/.json?after={}".format('')
    return url

# Delete the extension of the file name
def nameImg(imgUrl):
    if 'jpg' or 'webm' or 'mp4' or 'gif' or 'gifv' or 'png' in imgUrl:
            return imgUrl.split('/')[-1]


def downloadImg(imgUrl):
    # Get the filename to be saved as
    rawUrl = nameImg(imgUrl)
    filename = IMG_DIR + rawUrl

    # if nameImg() deleted the extension succesfuly
    if not(filename == IMG_DIR):
        # Download and save the image requested
        req = requests.get(imgUrl, stream=True)
        with open(filename, 'wb') as f:
            shutil.copyfileobj(req.raw, f)
            f.close()
            return rawUrl

def getImage():
    # Get a random subreddit to get an image from
    subreddit = URL_SR + SUBREDDITS_TO_MONITOR[get_randomSubreddit(SUBREDDITS_TO_MONITOR)]
    json = ''
    # Get URL
    url = createUrl(subreddit)
    # Download .json
    json = requests.get(url, headers={'User-Agent': 'MyRedditScrapper'}).json()
    # Get the posts
    post = json['data']['children']
    # Get the image asociated with a random post
    # range starting at 3 because prevents FAQ posts and related to be read
    imageUrl = (post[random.randrange(3, len(post)-1, 1)]['data']['url'])
    return downloadImg(imageUrl)

