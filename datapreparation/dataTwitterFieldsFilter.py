import sys
import tweepy, jsonpickle
from pymongo import MongoClient
from ta_backend.dateandtime.converterDateandTime import ConverterDateandTime
from datetime import datetime
# import json

class DataTwitterFieldsFilter:
    def filteringDataTwitterFields1(self, listTweet):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.tweet

        converter = ConverterDateandTime()

        listFilteredTweet = []
        totalList =len(listTweet)
        dateTweetConvertedAll = converter.str_to_date(listTweet[1]["created_at"])

        print(totalList)
        print(dateTweetConvertedAll)

        for index in range(len(listTweet)):
            try:
                try:
                    typeMedia = "text"
                    if (listTweet[index]["entities"]["media"][0]["type"] is None):
                        typeMedia = "text"
                    else:
                        typeMedia = listTweet[index]["entities"]["media"][0]["type"]
                except Exception as e:
                    print(str(e) + "error")

                dateTweetConverted = converter.str_to_date(listTweet[index]["created_at"])
                tweet = {
                    'date': dateTweetConverted,
                    'favorite_count': listTweet[index]["favorite_count"],
                    'favorited': listTweet[index]["favorited"],
                    'in_reply_to_status_id_str': listTweet[index]["in_reply_to_status_id_str"],
                    'in_reply_to_user_id_str': listTweet[index]["in_reply_to_user_id_str"],
                    'retweet_count': listTweet[index]["retweet_count"],
                    'id_str': listTweet[index]["id_str"],
                    'text': listTweet[index]["text"],
                    'text_processed': listTweet[index]["text"],
                    'truncated': listTweet[index]['truncated'],
                    'user_name': listTweet[index]["user"]["name"],
                    'user_favourites_count': listTweet[index]["user"]["favourites_count"],
                    'user_followers_count': listTweet[index]["user"]["followers_count"],
                    'user_following': listTweet[index]["user"]["following"],
                    'user_friends_count': listTweet[index]["user"]["friends_count"],
                    'user_statuses_count': listTweet[index]["user"]["statuses_count"],
                    'user_verified': listTweet[index]["user"]["verified"],
                    # user_id
                    'user_id': listTweet[index]["user"]["id_str"],
                    'typeMedia': typeMedia

                }

                listFilteredTweet.append(tweet)
            except Exception as e:
                print(str(e))
        tweetperDay = {
            'datePeriod': dateTweetConvertedAll,
            'tweetList': listFilteredTweet
        }

        db.insert(tweetperDay)
        tweetperDay1= tweetperDay

        success = "Your tweet is successfully inserted to Database"
        conn.close()
        totalTweetList = len(tweetperDay["tweetList"])
        return tweetperDay1, totalTweetList

    def filteringDataTwitterFields(self, listTweet, sinceFrom, untilTo):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.tweet

        converter = ConverterDateandTime()

        listFilteredTweet = []
        dateTweetConvertedAll = converter.str_to_date_tweet(sinceFrom)

        print(dateTweetConvertedAll)

        for index in range(len(listTweet)):
            try:
                try:
                    typeMedia = "text"
                    if (listTweet[index]["entities"]["media"][0]["type"] is None):
                        typeMedia = "text"
                    else:
                        typeMedia = listTweet[index]["entities"]["media"][0]["type"]
                except Exception as e:
                    print(str(e) + "error")

                dateTweetConverted = converter.str_to_date(listTweet[index]["created_at"])
                tweet = {
                    'date': dateTweetConverted,
                    'favorite_count': listTweet[index]["favorite_count"],
                    'favorited': listTweet[index]["favorited"],
                    'in_reply_to_status_id_str': listTweet[index]["in_reply_to_status_id_str"],
                    'in_reply_to_user_id_str': listTweet[index]["in_reply_to_user_id_str"],
                    'retweet_count': listTweet[index]["retweet_count"],
                    'id_str': listTweet[index]["id_str"],
                    'text': listTweet[index]["text"],
                    'text_processed': listTweet[index]["text"],
                    'truncated': listTweet[index]['truncated'],
                    'user_name': listTweet[index]["user"]["name"],
                    'user_favourites_count': listTweet[index]["user"]["favourites_count"],
                    'user_followers_count': listTweet[index]["user"]["followers_count"],
                    'user_following': listTweet[index]["user"]["following"],
                    'user_friends_count': listTweet[index]["user"]["friends_count"],
                    'user_statuses_count': listTweet[index]["user"]["statuses_count"],
                    'user_verified': listTweet[index]["user"]["verified"],
                    # user_id
                    'user_id': listTweet[index]["user"]["id_str"],
                    'typeMedia': typeMedia

                }

                listFilteredTweet.append(tweet)
            except Exception as e:
                print(str(e))
        tweetperDay = {
            'datePeriod': dateTweetConvertedAll,
            'tweetList': listFilteredTweet
        }

        # success = "Your tweet is successfully inserted to Database"
        conn.close()
        # totalTweetList = len(tweetperDay["tweetList"])
        return tweetperDay

    def insertToDatabase(self, listTweet):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.tweet
        db.insert(listTweet)

        success = "Your tweet is successfully inserted to Database"
        conn.close()
        return success

    def cobaTweet(self):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.tweet.coba_tweet

        listTweet = []
        dateTweetConverted = self.convert("Thu Mar 02 09:39:12 +0000 2017")
        tweet = {
            'date': dateTweetConverted,
            'user': "teguhcf",
            'tweet': "i love starbucks y",
            'lable': ""
        }
        # push srray
        listTweet.append(tweet)

        # insert the record.
        #db.insert(listTweet)
        # datetime

        # find all documents.
        ret = db.find({'date':{'$gte':self.convert("Thu Mar 01 07:39:12 +0000 2017"), '$lte':self.convert("Thu Mar 02 08:39:13 +0000 2017")}})
        #ret = db.find()
        print("hgdhdh")
        for record in ret:
            # print out the document.
            print(record['date'],record['user'] + ',', record['tweet'])


        # print()
        # print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

        # close the conn to MongoDB
        conn.close()

    def convert(self,stringDate):
        d = datetime.strptime(stringDate,'%a %b %d %H:%M:%S %z %Y')
        a = d

        return a

    def find_tweet(self,strFrom,strTo):
        conn = MongoClient('localhost', 27017)
        # Access the testdb/exampledb database name and the emp collection.
        db = conn.tweet.coba_tweet_v1
        # find all documents.
        #dateStrFrom = datetime.strptime('2017-03-08T00:41:00','%Y-%m-%dT%H:%M:%S')
        #dateStrTo = datetime.strptime('2017-03-08T00:41:07','%Y-%m-%dT%H:%M:%S')
        dateStrFrom = datetime.strptime(strFrom, '%Y-%m-%dT%H:%M:%S')
        dateStrTo = datetime.strptime(strTo,'%Y-%m-%dT%H:%M:%S')
        print(dateStrFrom.isoformat())
        ret = db.find({'date':{'$gte':dateStrFrom, '$lte':dateStrTo}})#kalo di print objectnya jadi rusak, gabisa direturn null value
        conn.close()
        return ret



    dateTweetConverted=convert(1,"Thu Mar 02 06:39:12 +0000 2017")
    print(dateTweetConverted)
    print("dh")
    #saveTweet(1)
    #find_tweet(1,"2017-03-08T00:30:00","2017-03-08T00:41:07")
    #findTweet(1)
    #cobaTweet()