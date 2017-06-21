from pymongo import MongoClient
from bson.objectid import ObjectId
from ta_backend.datapreprocessing.dataPreprocessing import DataPreprocessing
from ta_backend.sentimentpolarity.naiveBayesClassifier import NaiveBayesClassifier
from ta_backend.sentimentpolarity.training import Training
from ta_backend.dummydata import dummyData
import nltk

#to extract features
def extractFeatures(document):
    document_words = set(document)
    print("ini document word")
    print(document_words)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def saveListAspectPolarity(aspects):
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

def getListAspectPolarity(strAspect,strPolarity):
    # connect to the MongoDB.
    conn = MongoClient('localhost', 27017)
    listSentiment=[]
    listUserId=[]
    listTweetId=[]
    # Access the testdb/exampledb database name and the emp collection.
    db = conn.twitteranalytics.aspectPolarity
    try:
        # use drop for update database
        # db.users.find({gender: "M"}, {user_name: 1, _id: 0})
        result = db.find({'aspect':strAspect, 'polarity':strPolarity})
        for i in result:
            listSentiment.append(i['sentiment'])
            listUserId.append(i['user_id'])
            listTweetId.append(i['tweet_id'])
        return listSentiment,listUserId,listTweetId
    except Exception as e:
        print(str(e) + "error")

#instance class Training
training = Training()
#save tweet training to db
training.saveTweetTraining(dummyData.tweetTraining)

#get tweet training from db and convert to list python
tweeTraining = training.getTweetTraining()
print("ini tweet training dr db")
#test convert aspect to list of tuple with sentiment for training
tupleTweetTraining = training.convertListTweetToToListAspectTuple(tweeTraining)
print("iniconvert  tuple training")
print(tupleTweetTraining)
print("ini tuple training")
# print(all_tweets)

#tokenize term from sentiment aspect
tokenTraining = training.tokenizeTermTraining(tupleTweetTraining)
print("ini hasil tokenize tweet aspect yoo")
print(tokenTraining)

dataPreprocessing = DataPreprocessing()
#frequency of term
word_features = dataPreprocessing.get_word_features(dataPreprocessing.get_words_in_tweets(tokenTraining))
print("word features\n")
print(word_features)
print("-----------")

# print ("call traning set")

# print("ini pattern training")
# print(patternTraining)

#for retraining/use tupleTraining if input aspect tweet
patternTraining = nltk.classify.apply_features(extractFeatures, tokenTraining)
training.savePatternTraining(patternTraining) #for save result pattern training
patternTraining = training.loadPatternTraining()#use db

classifier = NaiveBayesClassifier.train(patternTraining)
print("classifierggg")
print(classifier)

#to classify aspect_tweet
def polarity(token_aspect):
    # print("inii twit aslinya",aspect_tweet)
    # print(classifier.classify(extract_features(nltk.word_tokenize(aspect_tweet))))
    # token_aspect = nltk.word_tokenize(aspect_tweet)
    return classifier.classify(extractFeatures(token_aspect))

print (classifier.show_most_informative_features(32))

# tweet_aspect = {
#     'sentence': "I love starbucks but starbucks staff is ugly",
#     'created_at': "2017-03-08",
#     'user_id': "2244994945",
#     'aspects': [
#         {
#             'entity': "starbucks",
#             'aspect': "general",
#             'sentiment': "love",
#             'polarity': "positive"
#         },
#         {
#             'entity': "starbucks",
#             'aspect': "staff",
#             'sentiment': "ugly",
#             'polarity': "negative"
#         },
#         {
#             'entity': "starbucks",
#             'aspect': "staff",
#             'sentiment': "do not like",
#             'polarity': "negative"
#         },
#         {
#             'entity': "starbucks",
#             'aspect': "staff",
#             'sentiment': "do not love",
#             'polarity': "negative"
#         }
#     ]
# }