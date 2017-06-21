from pymongo import MongoClient
from bson.objectid import ObjectId
from nltk.corpus import stopwords
from ta_backend.datapreprocessing.dataPreprocessing import DataPreprocessing
from ta_backend.sentimentpolarity.naiveBayesClassifier import NaiveBayesClassifier
from ta_backend.sentimentpolarity.training import Training
import nltk

import nltk
# pos_tweets = [('very sweet', 'positive'),
#               ('very beautiful', 'positive'),
#               ('a', 'positive'),
#               ('like', 'positive'),
#               ('love', 'positive'),
#               ('great', 'positive'),
#               ('the coffee is warm', 'positive')]
#
# neg_tweets = [('ugly', 'negative'),
#               ('not like','negative'),
#               ('not love', 'negative'),
#               ('not', 'negative'),
#               ('cup small', 'negative'),
#               ('dirty', 'negative'),
#               ('the weather is warm', 'negative')]

all_tweets = [('i love coffee starbucks because sweet', 'positive'),
              ('i love cup sturbucks because very beautiful', 'positive'),
              ('the cake starbucks smooth', 'positive'),
              ('the place is clean ', 'positive'),
              ('love', 'positive'),
              ('great', 'positive'),
              ('the coffee is smooth', 'positive'),
              ('the cake not good', 'negative'),
              ('i not like', 'negative'),
              ('i not love the coffe', 'negative'),
              ('the staff is ugly', 'negative'),
              ('the cup very small', 'negative'),
              ('the place is dirty', 'negative'),
              ('the weather is warm', 'negative')]

#to extract features

def extractFeatures(document):
    document_words = set(document)
    print("ini document word")
    print(document_words)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

dataPreprocessing = DataPreprocessing()
training = Training()
stop = set(stopwords.words('english'))
print("stup",stop)
tokenTraining = dataPreprocessing.tokenize1(all_tweets)
print("ini hasil tokenize tweet")
print(tokenTraining)


#frequency of term
word_features = dataPreprocessing.get_word_features(dataPreprocessing.get_words_in_tweets(tokenTraining))
print("word features\n")
print(word_features)
print("-----------")

# #test convert aspect to list of tuple with sentiment
# tupleTraining = training.convertAspectToListTuple(tweet_aspect)
# print("iniconvert  tuple training")
# print(tupleTraining)
# print("ini tuple training")
# print(all_tweets)

# print ("call traning set")
patternTraining = training.loadPatternTraining()#use db
# print("ini pattern training")
# print(patternTraining)

#for retraining/use tupleTraining if input aspect tweet
# patternTraining = nltk.classify.apply_features(extractFeatures, tokenTraining)
# training.savePatternTraining(patternTraining) #for save result pattern training

classifier = NaiveBayesClassifier.train(patternTraining)
print("classifier")
print(classifier)

#to classify aspect_tweet
def polarity(token):

    # print(classifier.classify(extract_features(nltk.word_tokenize(aspect_tweet))))
    # token_aspect = nltk.word_tokenize(aspect_tweet)
    return classifier.classify(extractFeatures(token))

print (classifier.show_most_informative_features(32))

