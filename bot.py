import tweepy,time,os
import getImgReddit as reddit
import datetime

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

 # api.update_status("This is just a test.") How to publish a tweet.

# MAIN
now = datetime.datetime.now()
mnt = int(now.minute)
while True:
    print(mnt);
    if mnt == 0:
        correct = 0
        while(correct == 0):
            
            image = reddit.getImage()
            ext = image[-3] + image[-2] + image[-1]
            if(ext == "png" or ext == "jpg"):
                print("Normal upload: " + image)
                api.update_with_media("img/" + str(image))
                os.system("rm img/" +str(image))
                correct = 1
                
    mentions = api.mentions_timeline();
    txt = open("test.txt","r+")
    last_id = int(txt.readline())
    for m in mentions:
        if m.id > last_id:
            txt = open("test.txt","w")
            txt.write(str(m.id))
            txt.close()
            user = m.user.id
            x = api.get_user(user)
            print("tweet ID: " + str(m.id))
            print("user ID: " +str(user))
            print("User name: " + x.screen_name)
            
            correct = 0
            while(correct == 0):
                            
                image = reddit.getImage()
                ext = image[-3] + image[-2] + image[-1]
                if(ext == "png" or ext == "jpg"):
                    print(image)
                    api.update_with_media("img/" + str(image),status = "@" + str(x.screen_name),in_reply_to_status_id = m.id)
                    os.system("rm img/" +str(image))
                    correct = 1
    print("Sleeping...")
    mnt = mnt + 1
    if mnt >= 120:
        mnt = 0
    time.sleep(60) #Pause to avoid rate limits.
