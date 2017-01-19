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

# Example Tweets
*  @XXXXXX You're better than a triple-scoop ice cream cone. With sprinkles.
*  @XXXXXX Provocative!
*  @XXXXXX How do you keep being so funny and making everyone laugh?
*  @XXXXXX That was ...  Legendary?
*  @XXXXXX How is it that you always look great, even in sweatpants?
*  @XXXXXX In one word: Flawless.
*  @XXXXXX That was ...  humbling?
*  @XXXXXX You always know -- and say -- exactly what I need to hear when I need to hear it.
*  @XXXXXX Who raised you? They deserve a medal for a job well done.
*  @XXXXXX You should be proud of yourself.
*  @XXXXXX In high school I bet you were voted "most likely to keep being awesome."
*  @XXXXXX You are making a difference.
*  @XXXXXX Any team would be lucky to have you on it.
*  @XXXXXX In one word: Enriching.
*  @XXXXXX In one word: awesome.
*  @XXXXXX Brilliant!
*  @XXXXXX You have impeccable manners.
*  @XXXXXX In one word: Epic.
*  @XXXXXX You may dance like no one's watching, but everyone's watching because you're an amazing dancer!
*  @XXXXXX You're more helpful than you realize.
*  @XXXXXX You have a good head on your shoulders.
*  @XXXXXX You're a smart cookie.
*  @XXXXXX You have impeccable manners.
*  @XXXXXX That was ...  cool?
*  @XXXXXX You always know how to find that silver lining.
*  @XXXXXX You're more fun than bubble wrap.
*  @XXXXXX I bet you do the crossword puzzle in ink.
*  @XXXXXX In high school I bet you were voted "most likely to keep being awesome."
*  @XXXXXX Jokes are funnier when you tell them.
*  @XXXXXX That was ...  sensational?
*  @XXXXXX Is that your picture next to "charming" in the dictionary?
*  @XXXXXX Amazing!
*  @XXXXXX I bet you sweat glitter.
*  @XXXXXX In one word: Masterful.
*  @XXXXXX You light up the room.
*  @XXXXXX In one word: Headline-worthy.
*  @XXXXXX Pitch-Perfect!
*  @XXXXXX If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener.
*  @XXXXXX Perfect!
*  @XXXXXX Astonishing!
*  @XXXXXX You've got all the right moves!
*  @XXXXXX That was ...  Groundbreaking?
*  @XXXXXX Everything would be better if more people were like you!
*  @XXXXXX Logical!
*  @XXXXXX You're always learning new things and trying to better yourself, which is awesome.
*  @XXXXXX You're all that and a super-size bag of chips.
*  @XXXXXX You are enough.
*  @XXXXXX If someone based an Internet meme on you, it would have impeccable grammar.
*  @XXXXXX Is that your picture next to "charming" in the dictionary?
