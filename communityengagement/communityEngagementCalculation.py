from pymongo import MongoClient
from ta_backend.communityengagement.engagements import Engagements
from ta_backend.communityengagement.mentions import Mentions

__author__ = "Hanna Hafifah"
__copyright__ = "Hanna Hafifah"


class CommunityEngagement:

    def __init__(self):
        self.date = '0000-00-00 00:00:00'
        self.engagement_result = []
        self.tweet_list = []

    def serialize(self):
        return {
            'date' : self.date,
            'tweet_list' : self.tweet_list,
            'engagement_result': self.engagement_result
        }

    def getengagement(self, datefrom, dateto):
        conn = MongoClient('localhost', 27017)
        db = conn.twitteranalytics.communityEngagement
        a = db.find({"date" : {"$gte" : datefrom, "$lte" : dateto } })

        conn.close()

        engagements = {}

        for i in a:
            engagements = {
                'date' : i["date"],
                'tweet_list' : i["tweet_list"],
                'engagement_result' : i["engagement_result"]
            }

        return engagements


    def filtermytweet(self, datefrom, dateto):
        starbucksUserId = "30973"
        conn = MongoClient('localhost', 27017)
        db = conn.twitteranalytics.companiesTweet

        tweets = db.find({'date': {'$gte': datefrom, '$lte': dateto}, 'user_id_str' : starbucksUserId})

        db = conn.twitteranalytics.companiesTweet
        db.insert(tweets)
        conn.close()

    def countcommunityengagement(self, datefrom, dateto):
        conn = MongoClient('localhost', 27017)
        db = conn.twitteranalytics.companiesTweet

        tweets = db.find({'date' : {'$gte' : datefrom, '$lte' : dateto}})
        conn.close()
        self.date = datefrom
        followers = 0
        statuses = 0
        total_retweet = 0
        total_likes = 0
        total_replies = 0

        engagement = Engagements()

        for tweet in tweets:

            output = engagement.countengagement(tweet["id_str"], datefrom, dateto)

            total_retweet = total_retweet + int(output["retweets_count"])
            total_likes = total_likes + int(output["likes_count"])
            total_replies = total_replies + int(output["replies"]["replies_count"])
            followers = tweet["followers_count"]
            statuses = tweet["statuses_count"]

            b = {
                'tweet_text' : tweet["text"],
                'engagement' : output
            }
            self.tweet_list.append(b)

        mention = Mentions()
        mentions = mention.countmention(datefrom, dateto)
        engagements = dict(date=self.date, tweet_list=self.tweet_list, engagement_result=dict(userData={
            "followers_count": followers,
            "statuses_count": statuses
        }, retweets_count=total_retweet, likes_count=total_likes, replies_count=total_replies, mention_list=mentions))

        db = conn.twitteranalytics.communityTest
        db.insert(engagements)
        conn.close()
        print("finish inserting")

        # return engagements

#Ini nanti perhari kan ya ngitungnya terus insert db? iya kan?
# ce = CommunityEngagement()
# timefrom = '2017-05-20T00:00:00'
# timeto = '2017-05-20T23:59:00'
# test = ce.countcommunityengagement(timefrom, timeto)
# print(test)





