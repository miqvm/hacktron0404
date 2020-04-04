import tweepy,time
import getImgReddit as reddit

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

 # api.update_status("This is just a test.") How to publish a tweet.

# MAIN
while True:
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
            print("ID tweet: " + str(m.id))
            print("ID usuario: " +str(user))
            print("Nombre usuario: " + x.screen_name)
            image = reddit.getImage()
            api.update_with_media("img/" + str(image),status = "@" + str(x.screen_name),in_reply_to_status_id = m.id)
    print("Sleeping...")
    time.sleep(60) #Pause to avoid rate limits.
