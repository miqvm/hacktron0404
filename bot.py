import tweepy,time,os
import datetime from datetime
import getImgReddit as reddit

auth = tweepy.OAuthHandler("rpHOqNQI8PIDj8AaSMKlB417K", "cgQaYKW6tcYn8Dn245FWayjrDAEoi32OhhVOHFayylbaQsKEaj")
auth.set_access_token("1246387201610518528-8yvIpEjWKScPpjod9sCqOig8y7PHV2", "X6mdi2HLdvKM3NjYNeaCBJTeiakatajPQaTlPtk0KfMHk")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

 # api.update_status("This is just a test.") How to publish a tweet.

# MAIN
min = int(datetime.datetime.now().minute)

while True:
    try:
        if min == 0:
            image = reddit.getImage()
            api.update_with_media("img/" + str(image))

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
                image = reddit.getImage()
                api.update_with_media("img/" + str(image),status = "@" + str(x.screen_name),in_reply_to_status_id = m.id)
                os.system("rm img/" +str(image))
        print("Sleeping...")
        ++min
        if min < 120:
            min = 0
        time.sleep(60) #Pause to avoid rate limits.

    except Exception as e:
        print(e)
