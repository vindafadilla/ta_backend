import nltk
import ast
import pickle
from nltk.stem.wordnet import WordNetLemmatizer
import re
from nltk.tokenize import  word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
from collections import Counter
from nltk.corpus import stopwords
from aylienapiclient import textapi
# from main import read_data, get_reviews_for_business, extract_aspects

class AspectExtraction:
    def __init__(self):
        self.lem= WordNetLemmatizer()
        # self.contoh ="jkljkl"
        self.sentic=pickle.load(open('./kamus/sentic_dump.p','rb'))
        self.asdict ={}
        self.forpol=[]
        #######################
        # self.point1 = ["VBD", "VB", "VBG", "VBN", "VBP", "VBZ", "JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
        self.point1 = ["VBD", "VB", "VBG", "VBN", "VBP", "JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
        self.point2 = ["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
        self.verb = ["VBD", "VB", "VBG", "VBN", "VBP", "VBZ"]
        self.noun = ["NN", "NNS", "NNP", "NNPS"]
        self.adverb = ["RB", "RBR", "RBS"]
        self.adjective = ["JJ", "JJR", "JJS"]
        self.auxiliary_verb = ["be", "am", "are", "is", "was", "being", "can", "could", "do", "did", "does", "doing", "have",
                          "had",
                          "has", "having", "may", "might", "might", "must", "shall", "should", "will", "'ve", "n't",
                          "were"]
        self.product=["teavana","frappuccino","coffee","Chai Latte","strawberry acai", "macchiato"]
        ######################

    def aspectExtraction(self,words, word):
        client = textapi.Client("9ef244ac", "02879f065869e71001dd6d29a0fe068e")
        sentiment = client.AspectBasedSentiment({'domain': 'restaurants', 'text': words})
        # for index in range(len(word)):
        #     for index2 in range(len(self.product)):
        #         print(word[index], self.product[index2])
        #         if (word[index] in self.product[index2]):
        #             print(word[index])
        #             sentiment = self.product[index2]
        #         else:
        #             print(word[index])
        #             # sentiment = client.AspectBasedSentiment({'domain': 'restaurants', 'text': words})
        # for index in range(len(word)):
        #     if (word[index] in self.product):
        #         print(word[index])
        #         sentiment = self.product
        #     else:
        #         print(word[index])
        #         sentiment = client.AspectBasedSentiment({'domain': 'restaurants', 'text': words})

        # sentiment = client.Sentiment({'text': words, 'domain': 'restaurants'})
        # print(sentiment)
        return sentiment

    def sentimentExtraction(self, listPOSTagged):
        listSentiment=[]
        for index in range(len(listPOSTagged)):
            for index2 in range(len(listPOSTagged[index])):
                for index3 in range(len(self.point1)):
                    if listPOSTagged[index][index2][1]==self.point1[index3]:
                        sentiment = listPOSTagged[index][index2][0]
                        # print(sentiment)
                        listSentiment.append(sentiment)
                # if listPOSTagged[index][index2][1] in self.point1:
                #     listSentiment.append(listPOSTagged[index][0])
        return listSentiment
    def sentimentExtraction2(self, listPOSTagged):
        listSentiment=""
        for index2 in range(len(listPOSTagged)):
            for index3 in range(len(self.point1)):
                if listPOSTagged[index2][1] == self.point1[index3]:
                    sentiment = listPOSTagged[index2][0]
                    # print(sentiment)
                    if(listSentiment==""):
                        listSentiment=sentiment
                    else:
                        listSentiment=listSentiment+" "+sentiment
                    # if listPOSTagged[index][index2][1] in self.point1:
                    #     listSentiment.append(listPOSTagged[index][0])
        return listSentiment