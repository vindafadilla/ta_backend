import os
from ta_backend.datapreparation.dataTwitter import DataTwitter
from ta_backend.datapreprocessing.tokenization import Tokenization
from ta_backend.datapreprocessing.posTagger import PosTagger
from  ta_backend.datapreprocessing.aspectExtraction import AspectExtraction
from ta_backend.onlinereputation.onlineReputationBasedonValidity import OnlineReputationBasedonValidity
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
# from nltk.parse.stanford import StanfordDependencyParser
from stanfordcorenlp import StanfordCoreNLP
# from ta_backend.datacleaning.dataCleaning import DataCleaning
from ta_backend.dateandtime.converterDateandTime import ConverterDateandTime
from ta_backend.dummydata import dummyData

def getDataTwitter():
    try:
        filename = 'datajson/data170518.json'
        sinceDate = '2017-04-18'
        untilDate = '2017-04-18'

        #---Instance class
        dataTwitter = DataTwitter()
        tokenization = Tokenization()
        posTagger = PosTagger()
        aspectExtraction= AspectExtraction()

        #---Library
        nlp = StanfordCoreNLP(r'C:/Users/Family/Downloads/OneDrive/TA KECE/Implementasi/corpus/stanford-corenlp-full-2017-06-09/stanford-corenlp-full-2017-06-09/')

        #---Get cleaned data
        listDataTwitterCleaned = dataTwitter.getDataTwitterCleanedFromDatabase(sinceDate, untilDate)
        # print(listDataTwitterCleaned["tweetList"][4]["text"])
        print(listDataTwitterCleaned["tweetList"][4]["text_processed"])

        #---Sentence segmented
        # listSentence = sent_tokenize(listDataTwitterCleaned["tweetList"][4]["text_processed"])
        listSentence = sent_tokenize("I love starbucks, their coffee is amazing. But their staff is really ugly")
        totalSentence= len(listSentence)
        print(listSentence[0], totalSentence)

        #---Tokenization
        listSentenceToken= []
        for index in range(len(listSentence)):
            sentenceToken = tokenization.tokenizing(listSentence[index])
            listSentenceToken.append(sentenceToken)
        # print(listSentenceToken[0])

        #---Lematization
        listSentenceLemmatized=[]
        for index in range(len(listSentenceToken)):
            lemma = tokenization.lemmatization(listSentenceToken[index])
            listSentenceLemmatized.append(lemma)
        # print(listSentenceLemmatized)

        #---POS Tagging
        listPOSTagged = []
        for index in range(len(listSentenceLemmatized)):
            posTagged = posTagger.postagging(listSentenceLemmatized[index])
            listPOSTagged.append(posTagged)
        print(listPOSTagged)

        #---Extracting Aspect
        listSentenceAspect=[]
        for index in range(len(listSentence)):
            aspectExtracted=aspectExtraction.aspectExtraction(listSentence[index], listSentenceToken[index])
            # print(aspectExtracted)
            for index2 in range(len(aspectExtracted["aspects"])):
                aspect=aspectExtracted["aspects"][index2]["aspect"]
                sentimentExtracted = aspectExtraction.sentimentExtraction2(listPOSTagged[index])
                print(aspect)
                aspectDict={
                    "entity": "starbucks",
                    "aspect"    : aspect,
                    "sentiment" : sentimentExtracted,
                    "polarity"  :""
                }

                listSentenceAspect.append(aspectDict)
        datetime= ConverterDateandTime()
        print(listSentenceAspect)
        aspectsList =[]
        print(listSentence[0])
        print(listDataTwitterCleaned["tweetList"][4]["date"])
        created_at = datetime.date_to_str(listDataTwitterCleaned["tweetList"][4]["date"])
        print(created_at)
        aspects={
            "sentence"      : listSentence[0],
            "created_at"    : created_at,
            "user_id"       : listDataTwitterCleaned["tweetList"][4]["user_id"],
            "tweet_id"      : listDataTwitterCleaned["tweetList"][4]["id_str"],
            "aspects"       : listSentenceAspect
        }
        aspectsList.append(aspects)
        # print(aspects)

        # print(aspectsList)
        # print(dummyData.tesTweetsAspectBase1)
        orValidity = OnlineReputationBasedonValidity()
        res, pos, neg, word_list, costumerNeed = orValidity.getOnlineReputationBasedOnValidity("s", "h", aspectsList)
        data = {
            'validity':
                {
                    'total_sentiment_pos': pos,
                    'total_sentiment_neg': neg

                },

            'relevance': word_list,
            'customerNeed': costumerNeed
        }
        print(data)


        # sentimentExtracted = aspectExtraction.sentimentExtraction(listPOSTagged)
        # print(sentimentExtracted)
    except Exception as e:
        print(str(e))


        # return jsonify(status='ERROR',message=str(e))

def main():
    getDataTwitter()

def run():
    """Entry point for console_scripts
    """
    main()

if __name__ == "__main__":
    run()

