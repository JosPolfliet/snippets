# Content
This script generates random responses that are generic enough to be plausible as replies to a wide range of tweets.

# Motivation and results
Being nice to people works. Compliments work. This script grew out of a hypothesis that haunted me: would complimenting random people on Twitter get me more followers? I ran this for a couple of days and turns it it absolutely does. On average, about 2-3 % of the interactions led to a new follower.

I have stopped running this once the concept was proven. My colleagues and regular followers were getting annoyed with my spamming. Use at your own risk!

# Usage

Follow these steps
* Get a Twitter API key at [Twitter Apps](https://apps.twitter.com/)
* Fill in the following lines with your credentials:
~~~~
consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''
~~~~
* Change the query string to whatever topic you want to respond too
Example: change
~~~~
for tweet in tweepy.Cursor(api.search,q="Machine Learning").items(100):
~~~~
to
~~~~
for tweet in tweepy.Cursor(api.search,q="rollercoaster").items(100):
~~~~
if you only want to respond to tweets about Rollercoasters.
* Run the script. 

WARNING: don't run this too much or Twitter WILL block your account. I got blocked once if I did more than 500 'likes' in an hour. For 100, I experienced no problems with running this every day.
