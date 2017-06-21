from pymongo import MongoClient

__author__ = "Hanna Hafifah"
__copyright__ = "Hanna Hafifah"

class Mentions(object):

    def __init__(self):
        self.mention_count = 0
        self.mention_list = []

    def serialize(self):
        return {
            'replies_count' : self.mention_count,
            'replies_list' : self.mention_list
        }

    def countmention(self, datefrom, dateto):
        conn = MongoClient('localhost', 27017)
        db = conn.twitteranalytics.Tweet
        tweets = db.find({"$text" : {"$search" : "@starbucks \"@Starbucks\"" }, "date" : {"$gte" : datefrom, "$lte" : dateto } } )
        conn.close()

        for tweet in tweets:
            if tweet["in_reply_to_status_id_str"] == None:
                tweet_object = {
                    'date': tweet["date"],
                    'id_str': tweet["id_str"],
                    'retweet_count': tweet["retweet_count"],
                    'favorite_count': tweet["favorite_count"],
                    'text': tweet['text'],
                    'in_reply_to_status_id_str': tweet["in_reply_to_status_id_str"],
                    'user_name': tweet["user_name"],
                    'user_id_str': tweet["user_id_str"],
                    'followers_count': tweet["followers_count"],
                    'statuses_count': tweet["statuses_count"]

                }
                self.mention_list.append(tweet_object)
                self.mention_count = self.mention_count+1

        mentionlist = {
            'mention_count' : self.mention_count,
            'mentions' : self.mention_list
        }

        return mentionlist