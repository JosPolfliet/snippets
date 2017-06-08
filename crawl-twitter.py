
# coding: utf-8

# In[18]:

import csv, codecs, cStringIO

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# In[38]:

import tweepy
import csv

consumer_key = ''
consumer_secret = ''

access_token_key = ''
access_token_secret = ''

# Bounding boxes for geolocations
# Online-Tool to create boxes (c+p as raw CSV): http://boundingbox.klokantech.com/
GEOBOX_WORLD = [-180,-90,180,90]
GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
GEOBOX_BELGIUM = [2.5214, 49.4753, 6.3776, 51.5087]
GEOCIRCLE_BELGIUM="50.56928286558243,4.7021484375,125km"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

with open('tweets{}.csv'.format(time.strftime("%Y%m%d%H%M%S")), 'wb') as csvFile:
  
    csvWriter = UnicodeWriter(csvFile)
    csvWriter.writerow(["tweet_id","created_at","text","user_name",
                        "user_id",'user_screen_name','user_followers_count', 
                        "favorite_count", "retweet_count", "is_quote_status", 'geo', 'lang'])

    for tweet in tweepy.Cursor(api.search,q="*",geocode=GEOCIRCLE_BELGIUM).items(10):
        csvWriter.writerow([tweet.id_str, str(tweet.created_at), 
                            tweet.text, #.encode("utf-8"), 
                            tweet.user.name, 
                            str(tweet.user.id), 
                            tweet.user.screen_name, 
                            str(tweet.user.followers_count), 
                            str(tweet.favorite_count),
                            str(tweet.retweet_count), 
                            str(tweet.is_quote_status), 
                            str(tweet.geo),
                            tweet.lang])
