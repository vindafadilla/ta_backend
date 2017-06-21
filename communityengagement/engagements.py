from pymongo import MongoClient
from ta_backend.communityengagement.replies import Replies

__author__ = "Hanna Hafifah"
__copyright__ = "Hanna Hafifah"

class Engagements(object):

    def __init__(self):
        self.retweets_count = 0
        self.likes_count = 0
        self.replies = []

    def serialize(self):
        return {
            'retweets_count' : self.retweets_count,
            'likes_count' : self.likes_count,
            'replies' : self.replies
        }

    def countengagement(self, tweet_id, datefrom, dateto):
        conn = MongoClient('localhost', 27017)
        db = conn.twitteranalytics.companiesTweet
        tweets = db.find({"id_str": tweet_id})

        for tweet in tweets:
            self.retweets_count = tweet["retweet_count"]
            self.likes_count = tweet["favorite_count"]

        conn.close()

        reply = Replies()
        self.replies = reply.countreplies(tweet_id, datefrom, dateto)

        engagement = {
            'retweets_count': self.retweets_count,
            'likes_count': self.likes_count,
            'replies': self.replies
        }
        return engagement