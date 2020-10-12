import os
import tweepy as tw
import pandas as import pdb; pd

consumer_key = 'DTEvipU4vxQiMBFu3qKobqunL'
consumer_secret = 'mHlVzlBBY0fuydkcvi9VMT8pVMpIY66eSpxxA5MIadK4l1zmsJ'
access_token = '1313302374149169154-Eg2fIo3zcc0gBbfazabswDXdZzyW8B'
access_token_secret = 'FlSKI0SXGrqzdgRAiDXz3EcfGDXZ6paKf0nzPbWgumtay'

search_word = "#coronavirus"
date_since = "2020-01-01"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since)

tweet_text = pd.DataFrame(data = time_locs, 
                    columns=['time', "location"])
tweet_text