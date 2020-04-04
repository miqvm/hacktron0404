import random
import shutil
from sys import exit
try:
    import requests
except ImportError:
    print('Requests must be installed. PLease run: pip install requests')
    exit()

SUBREDDITS_TO_MONITOR = ["2meirl4meirl", "absolutelynotme_irl", "absolutelynotmeirl", "BikiniBottomTwitter", "BlackPeopleTwitter", "comedyhomicide", 
                        "comedynecromancy", "dank_meme", "dankmemes", "DeepFriedMemes", "Im15AndThisIsYeet", "me_irl", "meirl", "meme", "memes", 
                        "Memes_Of_The_Dank", "nukedmemes","okbuddyretard", "SquarePosting", "whitePeopleTwitter"]
IMG_DIR = "img/"
URL_SR = "https://www.reddit.com/r/"

def get_randomSubreddit(arrayOfSubreddits):
    return (random.randrange(0, len(arrayOfSubreddits)-1, 1))

def createUrl(subreddit):
    url = subreddit.split('/.json')[0] + "/.json?after={}".format('')
    return url

def nameImg(imgUrl):
    if 'jpg' or 'webm' or 'mp4' or 'gif' or 'gifv' or 'png' in imgUrl:
            return imgUrl.split('/')[-1]

def downloadImg(imgUrl):
    filename = IMG_DIR + nameImg(imgUrl)
    print(filename)
    if filename:
        req = requests.get(imgUrl, stream=True)
        with open(filename, 'wb') as f:
            shutil.copyfileobj(req.raw, f)
            f.close()
    
def main():
    subreddit = URL_SR + SUBREDDITS_TO_MONITOR[get_randomSubreddit(SUBREDDITS_TO_MONITOR)]
    print(subreddit)
    json = ''
    url = createUrl(subreddit)
    json = requests.get(url, headers={'User-Agent': 'MyRedditScrapper'}).json()
    post = json['data']['children']
    imatgeUrl = (post[random.randrange(3, len(post), 1)]['data']['url'])

    downloadImg(imatgeUrl)