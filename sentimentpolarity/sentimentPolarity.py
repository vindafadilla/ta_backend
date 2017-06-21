from pymongo import MongoClient
from bson.objectid import ObjectId
from ta_backend.datapreprocessing.dataPreprocessing import DataPreprocessing
import nltk

class SentimentPoalrity():

    pos_tweets = [('I love this car', 'positive'),
                  ('This view is amazing', 'positive'),
                  ('I feel great this morning', 'positive'),
                  ('I am so excited about the concert', 'positive'),
                  ('He is my best friend', 'positive'),
                  ('He cars', 'positive')]

    neg_tweets = [('I do not like this car', 'negative'),
                  ('This view is horrible', 'negative'),
                  ('I feel tired this morning', 'negative'),
                  ('I am not looking forward to the concert', 'negative'),
                  ('He is my enemy', 'negative')]

    tweets = []
    for (words, sentiment) in pos_tweets + neg_tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered, sentiment))
    for i in tweets:
        print(i)



    def extract_features(self,tweets,document):
        dataPreprocssing = DataPreprocessing()
        word_features = dataPreprocssing.get_word_features(dataPreprocssing.get_words_in_tweets(tweets))
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

    training_set = nltk.classify.apply_features(extract_features(1,tweets,tweets), tweets)

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("classifier")
    print(classifier)

    tweet1 = 'i love this car'
    tweet2 = "i do not love this car"
    print (classifier.show_most_informative_features(32))
    print(tweet1)
    print (classifier.classify(extract_features(tweet1.split())))
    print(tweet2)
    print (classifier.classify(extract_features(tweet2.split())))
