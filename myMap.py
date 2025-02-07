# -*- coding: utf-8 -*-
# Map size
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import tweepy
import sys

from authenticate import authentication  # Consumer and access token/key

flag = 0
class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        self.get_tweet(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

    @staticmethod
    def get_tweet(tweet):

        if tweet.coordinates is not None:
            #print(tweet)
            x, y = map(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            map.plot(x, y, 'ro', markersize=1)
            plt.pause(0.01) # little trick to update the map

def press(event):
    print('Exit', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        sys.exit()


if __name__ == '__main__':

    # Size of the map
    fig = plt.figure(figsize=(18, 4), dpi=200)
    
    fig.canvas.mpl_connect('key_press_event', press)
    # Set a title
    plt.title("Terror tweets around the world")
    
    # Declare map projection, size and resolution
    map = Basemap(projection='merc',
                  llcrnrlat=-80,
                  urcrnrlat=80,
                  llcrnrlon=-180,
                  urcrnrlon=180,
                  lat_ts=20,
                  resolution='l')

    map.bluemarble(scale=0.3)
    #fig.canvas.mpl_connect('Close Event', handle_close)
    # Get access and key from another class
    auth = authentication()

    consumer_key = auth.getconsumer_key()
    consumer_secret = auth.getconsumer_secret()

    access_token = auth.getaccess_token()
    access_token_secret = auth.getaccess_token_secret()

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)

    streamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    myStream.filter(locations=[-180, -90, 180, 90], track=['terrorist', 'terror attacks','bomb blasts','hijacking','armed assault','hostage taking','taliban','ISIS','Islamic State','Boko Haram','Al-Shabaab','Shining Path','Al-Qaeda','Irish Republic Army','Liberation Tigers of Tamil EELAM','maoists','New People\'s Army'])
    
    plt.show()
