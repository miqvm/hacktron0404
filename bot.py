import tweepy

auth = tweepy.OAuthHandler("rpHOqNQI8PIDj8AaSMKlB417K", "cgQaYKW6tcYn8Dn245FWayjrDAEoi32OhhVOHFayylbaQsKEaj")
auth.set_access_token("1246387201610518528-8yvIpEjWKScPpjod9sCqOig8y7PHV2", "X6mdi2HLdvKM3NjYNeaCBJTeiakatajPQaTlPtk0KfMHk")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
