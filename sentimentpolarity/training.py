from pymongo import MongoClient
from bson.objectid import ObjectId
from nltk.corpus import brown
from nltk.corpus import stopwords
from ta_backend.datapreprocessing.dataPreprocessing import DataPreprocessing
import nltk

class Training:


    def saveTweetTraining(self, twitterTrainingSet):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.tweetTrainingSet
        try:
            # use drop for update database
            db.drop()
            db.insert(twitterTrainingSet)
        except Exception as e:
            print(str(e) + "error")

    def saveListAspectPolarity(self,aspects):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.aspectPolarity
        try:
            # use drop for update database
            db.drop()
            db.insert(aspects)
        except Exception as e:
            print(str(e) + "error")

    def getTweetTraining(self):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)
        listTweetTraining = []
        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.tweetTrainingSet
        try:
            # use drop for update database
            result = db.find()
            for i in result:
                listTweetTraining.append(i)
            return listTweetTraining
        except Exception as e:
            print(str(e) + "error")

    # filter field aspect and sentiment from a data tweet
    # the result like dummy all tweet
    def convertAspectToListTuple(self, tweet):
        list_aspect = []
        aspect_training = ()
        for i in tweet['aspects']:
            aspect_training = (i['sentiment'], i['polarity'])
            list_aspect.append(aspect_training)
        return list_aspect

    def convertListTweetToToListAspectTuple(self, tweets):
        list_aspect = []
        aspect_training = ()
        for i in tweets:
            for j in i['aspects']:
                aspect_training = (j['sentiment'], j['polarity'])
                list_aspect.append(aspect_training)
        return list_aspect

    # def aspectPolarity(self,listTweet):
    #     listAspect = []
    #     pos=0
    #     neg=0
    #     for i in listTweet:
    #         for j in i['aspects']:
    #             polarity = sentimentPolarityModul.polarity(j['sentiment'])
    #             if (polarity == "positive"):
    #                 pos += 1
    #             elif (polarity == "negative"):
    #                 neg += 1
    #             aspect = j['aspect']
    #             sentiment = j['sentiment']
    #             dataAspect={
    #                 'aspect':aspect,
    #                 'sentiment':sentiment,
    #                 'polarity':polarity
    #             }
    #             listAspect.append(dataAspect)
    #     return listAspect,pos,neg

    # example of fata dummy
    all_tweets = [('very sweet', 'positive'),
                  ('very beautiful', 'positive'),
                  ('a', 'positive'),
                  ('like', 'positive'),
                  ('love', 'positive'),
                  ('great', 'positive'),
                  ('the coffee is warm', 'positive'),
                  ('ugly', 'negative'),
                  ('not like', 'negative'),
                  ('not love', 'negative'),
                  ('not', 'negative'),
                  ('cup small', 'negative'),
                  ('dirty', 'negative'),
                  ('the weather is warm', 'negative')]

    # print (all_tweets)

    # fetch pola data training from database
    def loadPatternTraining(self):
        conn = MongoClient('localhost', 27017)
        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.patternTrainingSet
        result = db.find_one()
        #convert list to tuple
        a = result['data_training']
        tupleTrainingSet = []
        for i in a:
            tupleTrainingSet.append(tuple(i))
        result_training_set = tupleTrainingSet
        return result_training_set

    # save pola data training
    # use for retrain to update data training
    def savePatternTraining(self,trainingSet):
        # connect to the MongoDB.
        conn = MongoClient('localhost', 27017)

        # Access the testdb/exampledb database name and the emp collection.
        db = conn.twitteranalytics.patternTrainingSet
        try:
            datatraingset = {}
            datatraingset['data_training'] = list(trainingSet)
            #use drop for update database
            db.drop()
            db.insert(datatraingset)
        except Exception as e:
            print(str(e) + "error")

    def convertDataTraining(self):
        print("load data training")
        ab = self.loadPatternTraining()
        print("ini datatraining")
        print(ab)

        print (ab['data_training'])
        a = ab['data_training']
        tupleTrainingSet = []
        for i in a:
            tupleTrainingSet.append(tuple(i))
        print("ini tuple")
        result_training_set = tupleTrainingSet
        return result_training_set

    #for tokenize text tweet
    def tokenizeTermTraining(self,all_tweets):
        tweets = []
        stopword=['and','or']
        for (words, polarity) in all_tweets:
            words_filtered = [e.lower() for e in words.split() if e not in stopword]
            tweets.append((words_filtered, polarity))
        return tweets

    #for tokenize text tweet
    def tokenize1(self,all_tweets):
        tweets = []
        stopwords = ['is','the']
        for (words, polarity) in all_tweets:
            words_filtered = [e.lower() for e in nltk.word_tokenize(words) if e in brown.words(categories='reviews') and e not in stopwords]
            tweets.append((words_filtered, polarity))
        return tweets

