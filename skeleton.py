#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     fibonacci = ta_backend.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from flask import Flask,json,jsonify,request
from ta_backend.datapreparation.dataTwitter import DataTwitter
from ta_backend.datapreparation.dataTwitterFieldsFilter import DataTwitterFieldsFilter
from ta_backend.communityengagement.communityEngagementCalculation import CommunityEngagement
from ta_backend.communityengagement.replies import Replies
from ta_backend.onlinereputation.onlineReputationCalculation import OnlineReputationCalculation
from ta_backend.onlinereputation.onlineReputationBasedonRelevance import OnlineReputationBasedonRelevance
from ta_backend.onlinereputation.onlineReputationBasedonVolume import OnlineReputationBasedonVolume
from ta_backend.onlinereputation.onlineReputationBasedonDiversity import OnlineReputationBasedonDiversity
from ta_backend.customerneeds.aspectFrequencyCalculation import AspectFrequencyCalculation
from ta_backend.datapreparation.appropriateDataTweetFilter import AppropriateDataTweetFilter
from datetime import datetime
from ta_backend.datacleaning.dataCleaning import DataCleaning

application = Flask(__name__)

@application.route("/api/v1/onlinereputation/get",methods=['GET'])
def getOnlineReputation():
    try:
        sinceDate=request.args.get('time_from')
        untilDate=request.args.get('time_to')

        dataTwitter = DataTwitter()
        listDataTwitterCleaned = dataTwitter.getDataTwitterCleanedFromDatabase(sinceDate, untilDate)

        onlineReputationCalculation = OnlineReputationCalculation()
        onlineReputation = onlineReputationCalculation.onlineReputationCalculation(sinceDate,untilDate, listDataTwitterCleaned)

        return jsonify(onlineReputation)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/customerneeds/overall",methods=['GET'])
def getCustomerNeedsOverall():
    try:
        time_from=request.args.get('time_from')
        time_to=request.args.get('time_to')
        filename = 'datajson/data170518.json'

        aspectFrequencyCalculation = AspectFrequencyCalculation()
        dataTwitter = DataTwitter()
        listTweet = dataTwitter.getTwitterFromJSON(filename)
        aspectFrequencyDataTweetCalculated = aspectFrequencyCalculation.calculateAspectFrequency(listTweet, time_from, time_to)

        return jsonify(aspectFrequencyDataTweetCalculated,time_from,time_to)
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/customerneeds/sentimentwordsperaspect",methods=['GET'])
def getCustomerNeedsSentimentWordsperAspect():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        aspect=request.args.get('aspect')
        sentiment=request.args.get('sentiment')
        page=request.args.get('page')
        machineDetail = {
                'starbucks':["good","delicious"]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

#ini tambahin -hanna
@application.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response

@application.route("/api/v1/communityengagement/engagement/get",methods=['GET'])
def getCommunityEngagemnetEngagement():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')

        engagement = CommunityEngagement()

        machineDetail = engagement.getengagement(time_from, time_to)

        return jsonify(machineDetail,time_from,time_to)

    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

#aku sampe sini ngubahnya - hanna

@application.route("/api/v1/datatwitter/get",methods=['GET'])
def getDataTwitter():
    try:
        sinceDate=request.args.get('since')
        untilDate=request.args.get('until')
        filename = request.args.get('filename')

        dataTwitter = DataTwitter()
        listTweet = dataTwitter.getDataTwitter(sinceDate, untilDate, filename)

        # return jsonify(message,sinceDate,untilDate,filename)
        return jsonify(sinceDate, untilDate, filename)
        # return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/datacleaningandpreprocessing",methods=['GET'])
def getDataCleaningandPreprocessing():
    try:
        sinceDate = request.args.get('since')
        untilDate = request.args.get('until')
        filename = request.args.get('filename')
        dataTwitter = DataTwitter()
        listTweet = dataTwitter.getTwitterFromJSON(filename)

        dataTwitterFieldsFilter = DataTwitterFieldsFilter()
        dataTwitterFiltered, totalTweetList = dataTwitterFieldsFilter.filteringDataTwitterFields1(listTweet)
        # print(dataTwitterFieldsFilter["tweetList"][2])
        # listInsertedData = dataTwitterFieldsFilter.insertToDatabase(dataTwitterFiltered)
        # insertedData = listInsertedData["tweetList"][2]

        jsonData={
            'totalTweet': totalTweetList,
            # 'message'   : li,
            'sinceDate' : sinceDate,
            'untilDate' : untilDate,
            'filename'  : filename
        }

        return jsonify(jsonData)
    except Exception as e:

        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/test/find_tweet/get",methods=['GET'])
def getTestFindTweet():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        tweet_id=request.args.get('tweet_id')
        dataTweet =  DataTwitter()
        ret = dataTweet.find_tweet(time_from,time_to)
        if __name__ == '__main__':
            machineDetail = list(ret)
            i=1
            for record in machineDetail:
                # print out the document.
                #print(i, record['date'], record['user_name'], record['text'], record["favorite_count"],
                #record["user_followers_count"])
                i = i + 1
                #serialized_result = [json.dumps(ret, default=json.util.default, separators=(',', ':')) for a in machineDetail]
                #return serialized_result
        # return dumps(machineDetail)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/test/volume/get",methods=['GET'])
def getTestVolumeTweet():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        tweet_id=request.args.get('tweet_id')
        onlineReputationCalculation =  OnlineReputationCalculation()
        ret = onlineReputationCalculation.getVolume(time_from,time_to)
        if __name__ == '__main__':
            machineDetail = ret
            print(machineDetail)
        machineDetail = {
            'total': machineDetail
        }
        return jsonify(machineDetail, time_from, time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/datacleaning/get",methods=['GET'])
def performDataCleaning():
    try:
        sinceDate=request.args.get('since')
        untilDate=request.args.get('until')
        filename = request.args.get('filename')

        dataTwitter = DataTwitter()
        listTweet = dataTwitter.getTwitterFromJSON(filename)
        print(listTweet[101]["text"])
        print(len(listTweet))

        appropriateDataTweetFilter = AppropriateDataTweetFilter()
        dataTwitterFieldsFilter = DataTwitterFieldsFilter()
        dataCleaning = DataCleaning()

        listAppropriateDataTweetChoosed = appropriateDataTweetFilter.choosingAppropriateDataTweet(listTweet)
        listDataTwitterFieldsFiltered = dataTwitterFieldsFilter.filteringDataTwitterFields(listAppropriateDataTweetChoosed, sinceDate, untilDate)
        print(listDataTwitterFieldsFiltered["tweetList"][2])
        print(len(listDataTwitterFieldsFiltered["tweetList"]))
        listDataTweetNormalized = dataCleaning.dataCleaningProcess(listDataTwitterFieldsFiltered)
        print(listDataTweetNormalized["tweetList"][2])
        print(len(listDataTweetNormalized["tweetList"]))
        print(listDataTweetNormalized["tweetList"][2]["text"])
        print(listDataTweetNormalized["tweetList"][2]["text_processed"])
        dataTwitterFieldsFilter.insertToDatabase(listDataTweetNormalized)

        return jsonify(listDataTweetNormalized["tweetList"][2])
        # return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/datapreprocessing/get",methods=['GET'])
def performDataPreprocessing():
    try:
        sinceDate = request.args.get('since')
        untilDate = request.args.get('until')

        dataTwitter = DataTwitter()

        listDataTwitterCleaned = dataTwitter.getDataTwitterCleanedFromDatabase(sinceDate, untilDate)

        print(listDataTwitterCleaned["tweetList"][2]["text_processed"])

        return jsonify(listDataTwitterCleaned["tweetList"])
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))

@application.route("/api/v1/onlinereputation/volume/get",methods=['GET'])
def getOnlineReputationbasedonVolume():
    try:
        sinceDate=request.args.get('time_from')
        untilDate=request.args.get('time_to')

        dataTwitter = DataTwitter()
        listDataTwitterCleaned = dataTwitter.getDataTwitterCleanedFromDatabase(sinceDate, untilDate)

        onlineReputationBasedonVolume = OnlineReputationBasedonVolume()
        totalVolume = onlineReputationBasedonVolume.getVolume(listDataTwitterCleaned)

        return jsonify(totalVolume,sinceDate,untilDate)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

if __name__ == "__main__":
    application.run(host='0.0.0.0')

