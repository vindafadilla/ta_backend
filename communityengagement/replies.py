from pymongo import MongoClient

__author__ = "Hanna Hafifah"
__copyright__ = "Hanna Hafifah"

class Replies(object):

    def __init__(self):
        self.replies_count = 0
        self.replies_list = []

    def serialize(self):
        return {
            'replies_count' : self.replies_count,
            'replies_list' : self.replies_list
        }

    def countreplies(self,tweet_id, datefrom, dateto):
        conn = MongoClient('localhost', 27017)
        db = conn.twitteranalytics.Tweet
        tweets = db.find({"$text": {"$search": "@starbucks \"@Starbucks\""}, "date": {"$gte": datefrom, "$lte": dateto}})
        conn.close()

        for tweet in tweets:
            if tweet["in_reply_to_status_id_str"] == tweet_id:
                tweet_object = {
                    'date' : tweet["date"],
                    'id_str' : tweet["id_str"],
                    'retweet_count' : tweet["retweet_count"],
                    'favorite_count' : tweet["favorite_count"],
                    'text' : tweet['text'],
                    'in_reply_to_status_id_str' : tweet["in_reply_to_status_id_str"],
                    'user_name' : tweet["user_name"],
                    'user_id_str' : tweet["user_id_str"],
                    'followers_count' : tweet["followers_count"],
                    'statuses_count' : tweet["statuses_count"]

                }
                self.replies_list.append(tweet_object)
                self.replies_count = self.replies_count+1

        replylist= {
            'replies_count' : self.replies_count,
            'replies_list' : self.replies_list
        }

        return replylist

reply = Replies()