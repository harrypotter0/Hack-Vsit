from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="ZOtLjP8dvEOIp6kiasNj3IT4M"
csecret="lR5cpOfFgkkvpI6MHoeWg0aJPoVAFmS4pROoOnnjoiUOiadc5T"
atoken="756895645512761344-dHrqgocUiWklMhbgyLQR8w7tkais4gj"
asecret="WmtBIlmEETSO5v0G4h9VJsUKml6UeDGYu5m1kIx8g3LP5"

# from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
# open('twitter-out.txt', 'w').close()
# # f = open('twitter-out.txt', 'r+')
# # f.truncate()
