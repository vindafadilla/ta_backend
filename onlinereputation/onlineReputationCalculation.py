import tweepy,sys,jsonpickle
from pymongo import MongoClient
from datetime import datetime
# from datatwitter.Converter import Converter
from ta_backend.dateandtime.converterDateandTime import ConverterDateandTime
from ta_backend.onlinereputation.onlineReputationBasedonDiversity import OnlineReputationBasedonDiversity
from ta_backend.onlinereputation.onlineReputationBasedonVolume import OnlineReputationBasedonVolume
from ta_backend.onlinereputation.onlineReputationBasedonRelevance import OnlineReputationBasedonRelevance
from ta_backend.onlinereputation.onlineReputationBasedonValidity import OnlineReputationBasedonValidity
import json
from bson.json_util import dumps

class OnlineReputationCalculation:
    dateStrTo=0
    dateStrFrom=0

    def onlineReputationCalculation(self, sinceDate, untilDate, listDataTwitterCleaned):
        onlineReputationBasedonVolume = OnlineReputationBasedonVolume()
        totalVolume = onlineReputationBasedonVolume.getVolume(listDataTwitterCleaned)

        onlineReputationBasedonDiversity = OnlineReputationBasedonDiversity()
        totalDiversity = onlineReputationBasedonDiversity.onlineReputationBasedonDiversityCalculation(
            listDataTwitterCleaned)

        onlineReputationBasedonRelevance = OnlineReputationBasedonRelevance()
        aspectFrequencyDataTweetCalculated = onlineReputationBasedonRelevance.calculateAspectFrequency(
            listDataTwitterCleaned,
            sinceDate,
            untilDate)

        onlineReputationBasedonValidity = OnlineReputationBasedonValidity()
        validation = onlineReputationBasedonValidity.onlineReputationbasdeonValidityCalculation()

        onlineReputation = {
            'sinceDate': sinceDate,
            'untilDate': untilDate,
            'reputation': {
                'volume': totalVolume,
                'diversity': totalDiversity,
                'validation': validation,
                'relevance': aspectFrequencyDataTweetCalculated
            }
        }
        return onlineReputation


    # def getVolume(self,strFrom,strTo):
    #     conn = MongoClient('localhost', 27017)
    #     # Access the testdb/exampledb database name and the emp collection.
    #     db = conn.tweet.coba_tweet_v1
    #     # find all documents.
    #     #dateStrFrom = datetime.strptime('2017-03-08T00:41:00','%Y-%m-%dT%H:%M:%S')
    #     #dateStrTo = datetime.strptime('2017-03-08T00:41:07','%Y-%m-%dT%H:%M:%S')
    #     dateStrFrom = datetime.strptime(strFrom, '%Y-%m-%dT%H:%M:%S')
    #     dateStrTo = datetime.strptime(strTo,'%Y-%m-%dT%H:%M:%S')
    #     print(dateStrFrom.isoformat())
    #     ret = db.count({'date':{'$gte':dateStrFrom, '$lte':dateStrTo}})#kalo di print objectnya jadi rusak, gabisa direturn null value
    #     conn.close()
    #     print(ret)
    #     return ret
    # def getDiversity(self,strFrom,strTo):
    #     conn = MongoClient('localhost', 27017)
    #     # Access the testdb/exampledb database name and the emp collection.
    #     db = conn.tweet.coba_tweet_v1
    #     # find all documents.
    #     # dateStrFrom = datetime.strptime('2017-03-08T00:41:00','%Y-%m-%dT%H:%M:%S')
    #     # dateStrTo = datetime.strptime('2017-03-08T00:41:07','%Y-%m-%dT%H:%M:%S')
    #     dateStrFrom = datetime.strptime(strFrom, '%Y-%m-%dT%H:%M:%S')
    #     dateStrTo = datetime.strptime(strTo, '%Y-%m-%dT%H:%M:%S')
    #     print(dateStrFrom.isoformat())
    #     #ret = db.find({"user_name":"Greenly" },{'date':{'$gte':dateStrFrom, '$lte':dateStrTo}}).count() # kalo di print objectnya jadi rusak, gabisa direturn null value
    #     div_photo = db.find({"typeMedia":"photo"}, {'date': {'$gte': dateStrFrom, '$lte': dateStrTo}}).count()  # kalo di print objectnya jadi rusak
    #     div_text = db.find({"typeMedia": "text",'date': {'$gte': dateStrFrom, '$lte': dateStrTo}}).count()  # kalo di print objectnya j
    #     conn.close()
    #     diversity = {
    #         'total_text': div_text,
    #         'total_media': div_photo,
    #     }
    #     print(diversity['total_media'],diversity['total_text'])
    #
    #     return diversity
    # getDiversity(1,"2017-03-08T00:41:00","2017-03-08T00:41:07")


