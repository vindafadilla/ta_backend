from _overlapped import NULL
from pymongo import MongoClient

import tweepy,sys,jsonpickle
from pymongo import MongoClient
import json

from ta_backend.dateandtime.converterDateandTime import ConverterDateandTime

class DataTwitter:
    def getDataTwitter(self, sinceDate, untilDate, filename):
        consumer_key = 'CLPWkBrmsFe1JrZ3PO87OK9vf'
        consumer_secret = 'zDPiFDpr20DaE5usa5ynhjUR2FifPydzbaNKzXhjyp73N6nrSz'

        qry ='starbucks OR @Starbucks OR #starbucks'

        maxTweets = 100000  # Isi sembarang nilai sesuai kebutuhan anda
        tweetsPerQry = 100  # Jangan isi lebih dari 100, ndak boleh oleh Twitter
        fName = filename  # Nama File hasil Crawling

        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        if (not api):
            sys.exit('Autentikasi gagal, mohon cek "Consumer Key" & "Consumer Secret" Twitter anda')

        sinceId = None;max_id = -1;tweetCount = 0
        print("Mulai mengunduh maksimum {0} tweets".format(maxTweets))
        listTweet=[]
        with open(fName, 'w') as f:
            while tweetCount < maxTweets:
                try:
                    if (max_id <= 0):
                        if (not sinceId):
                            new_tweets = api.search(q=qry, count=tweetsPerQry, lang="en", since=sinceDate, until=untilDate,include_entities=True)
                        else:
                            new_tweets = api.search(q=qry, count=tweetsPerQry, since_id=sinceId, lang="en", since=sinceDate, until=untilDate,include_entities=True)
                    else:
                        if (not sinceId):
                            new_tweets = api.search(q=qry, count=tweetsPerQry, max_id=str(max_id - 1), lang="en", since=sinceDate, until=untilDate,include_entities=True)
                        else:
                            new_tweets = api.search(q=qry, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId, lang="en", since=sinceDate, until=untilDate,include_entities=True)
                    if not new_tweets:
                        print('Tidak ada lagi Tweet ditemukan dengan Query="{0}"'.format(qry));break
                    for tweet in new_tweets:
                        tweetTemp=tweet._json
                        # listTweet.append(tweetTemp)
                        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + ',\n')
                    tweetCount += len(new_tweets)
                    sys.stdout.write("\r");sys.stdout.write("Jumlah Tweets telah tersimpan: %.0f" % tweetCount);sys.stdout.flush()
                    max_id=new_tweets[-1].id
                    # listTweet.append(tweet._json)
                    # return listTweet
                    success="Your Twitter is saved in file JSON"
                except tweepy.TweepError as e:
                    return e;
                    # print("some error : " + str(e));
                    break  # Aya error, keluar
        return success
        # print('\nSelesai! {0} tweets tersimpan di "{1}"'.format(tweetCount, fName))

    def getTwitterFromJSON(self, filename):

        # create a dictionary to hold emp details.
        # load file
        print(filename)
        file = open(filename).read()
        # convert json to object
        json_obj = json.loads(file)
        # inisialisasi
        listTweet = []
        for filters in json_obj:
            # print out the document.

            # dictionary
            # tweet = {
            #     'date': filters["created_at"],
            #     'user': filters["user"]["name"],
            #     'tweet': filters["text"],
            #     'lable': ""
            # }
            tweet=filters
            # push srray
            listTweet.append(tweet)

            # insert the record.
        # db.insert(listTweet)

        # find all documents.
        # ret = db.find()
        return listTweet
        # print()
        # print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
        #
        # # close the conn to MongoDB
        # conn.close()

    def getDataTwitterCleanedFromDatabase(self, strFrom, strTo):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.tweet

        converterDateandTime = ConverterDateandTime()

        dateStrFrom =  converterDateandTime.str_to_date_tweet(strFrom)
        dateStrTo = converterDateandTime.str_to_date_tweet(strTo)
        print(dateStrFrom.isoformat())
        ret = db.find({'datePeriod': {'$gte': dateStrFrom, '$lte': dateStrTo}})
        listDataTwitterCleaned=[]
        for record in ret:
            # print out the document.
            datePeriod = record["datePeriod"]
            listDataTwitterCleaned = record["tweetList"]

        tweetperDay={
            'datePeriod': datePeriod,
            'tweetList' : listDataTwitterCleaned
        }

        conn.close()
        return tweetperDay