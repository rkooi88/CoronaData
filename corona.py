import os
import tweepy as tw
import pandas as import pdb; pd

search_word = "#coronavirus"
date_since = "2020-01-01"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since)

tweet_text = pd.DataFrame(data = time_locs, 
                    columns=['time', "location"])
tweet_text