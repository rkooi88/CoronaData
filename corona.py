import os
import tweepy as tw
import numpy as np
import pandas as pd
import credentials

search_word = "#coronavirus" + " -filter:retweets"
date_since = "2020-01-01"

tweets = tw.Cursor(api.search,
              q = search_words,
              lang = "en",
              since = date_since)

tweet_text = pd.DataFrame(data = time_locs, 
                    columns=['date', "location"])
print(tweet_text)