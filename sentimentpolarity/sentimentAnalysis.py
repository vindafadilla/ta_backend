from ta_backend.sentimentpolarity import sentimentPolarityModul
from ta_backend.sentimentpolarity import sentimentPolaritySentenceModul
from ta_backend.sentimentpolarity.training import Training
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
import nltk


class SentimentAnalysis:

    #for aspect level
    listPolarity=[]

    # def aspectPolarity(self,aspect):
    #     listPolarity = []
    #     for i in aspect['aspects']:
    #         polarity = sentimentPolarityModul.polarity(i['sentiment'])
    #         listPolarity.append(polarity)
    #     return listPolarity

    def aspectPolarity(self,listTweet):
        listAspect = []
        sentiment = []
        token_aspects=[]
        wordList=[]#to save aspect and sentiment
        dictFreqWordList=[]
        pos=0
        neg=0
        stopword=['and','or']
        senttt=""
        for i in listTweet:
            userId = i['user_id']
            tweetId = i['tweet_id']
            for j in i['aspects']:
                token_aspect = nltk.word_tokenize(j['sentiment'])#tokenize sentiment
                for id_token_aspect in token_aspect:
                    if (id_token_aspect not in stopword):
                        token_aspects.append(id_token_aspect)

                polarity = sentimentPolarityModul.polarity(token_aspects)
                if (polarity == '1'): #positive
                    pos += 1
                elif (polarity == '0'): #negative
                    neg += 1
                aspect = j['aspect']
                idx=0
                while(idx<len(token_aspects)):
                    if(token_aspects[idx]=="not"):
                        senttt="not "+token_aspects[idx+1]
                        idx+=2
                    else:
                        senttt=token_aspects[idx]
                    sentiment.append(senttt)
                    idx+=1
                print("sen",sentiment)
                wordList.append(aspect)
                #aspect
                dataAspect={
                    'aspect':aspect,
                    'sentiment':sentiment,
                    'polarity':polarity,
                    'user_id':userId,
                    'tweet_id':tweetId
                }

                #insert data aspect to list aspect
                listAspect.append(dataAspect)
                sentiment = []  # empty list
                token_aspects= []
        # print("jfjfjf", listAspect)


        #count freq wordlist
        wordListFreq=nltk.FreqDist(wordList)

        dictWordlist=list(wordListFreq.items())
        for i in dictWordlist:
            word={
                'word':i[0],
                'freq':i[1]
            }
            # print(word)
            dictFreqWordList.append(word)
        sort=dictFreqWordList

        #bisi butuh
        # aspectPolarity = listAspect.copy()

        sentimentPolarityModul.saveListAspectPolarity(listAspect)
        print("jfjfjf",listAspect)
        listChecker=[]
        tempListAspect=[]
        dataAspectPos = []
        dataAspectNeg=[]
        tempAspect={}
        for i in listAspect:
            tempAspect={
                'aspect':i['aspect'],
                'sentiment':i['sentiment'],
                'polarity':i['polarity'],
                'user_id':i['user_id'],
                'tweet_id':i['tweet_id']
            }
            if(i['aspect'] not in listChecker):
                # print("get")
                tempp=[]

                #get from db where aspect == i and positif
                resultSentiment,resUserId,resTweetId = sentimentPolarityModul.getListAspectPolarity(i['aspect'],'1')
                print('resuid',resUserId)
                if (resultSentiment!=[]):
                    for index_result in resultSentiment:
                        for idx in index_result:
                            tempp.append(idx)
                            print("idx_res",idx)

                    sentimentPolarity = {
                        'aspect' : i['aspect'],
                        'sentiment' : tempp
                    }
                    # print("listchecker", listChecker)

                    print("tem", sentimentPolarity)

                    dictFreqSp = []
                    sent = []

                    sentimentPolarityFreq = nltk.FreqDist(sentimentPolarity['sentiment'])

                    dictSp = list(sentimentPolarityFreq.items())
                    for inn in dictSp:
                        sent.append(list(inn))
                        print("inn", inn)
                    asp = {
                        'aspect': sentimentPolarity['aspect'],
                        'sentiment': sent,
                        'user_id':resUserId,
                        'tweet_id':resTweetId

                    }

                    dataAspectPos.append(asp)
                tempp = []
                resultSentiment=[]
                resUserId=[]
                resTweetId=[]
                resultSentiment,resUserId,resTweetId = sentimentPolarityModul.getListAspectPolarity(i['aspect'],'0')
                if (resultSentiment!=[]):
                    for index_result in resultSentiment:
                        for idx in index_result:
                            tempp.append(idx)
                            print("idx_res",idx)

                    sentimentPolarity = {
                        'aspect' : i['aspect'],
                        'sentiment' : tempp


                    }
                    # print("listchecker", listChecker)

                    print("temmmmm", sentimentPolarity)
                    dictFreqSp=[]
                    sent=[]

                    sentimentPolarityFreq = nltk.FreqDist(sentimentPolarity['sentiment'])

                    dictSp = list(sentimentPolarityFreq.items())
                    for inn in dictSp:
                        sent.append(list(inn))
                        print("inn",inn)
                    asp={
                        'aspect':sentimentPolarity['aspect'],
                        'sentiment':sent,
                        'user_id': resUserId,
                        'tweet_id':resTweetId
                    }

                    dataAspectNeg.append(asp)


            listChecker.append(i['aspect'])
            tempListAspect.append(tempAspect)
        print("dataaspectposs", dataAspectPos)
        print("dataaspectneg", dataAspectNeg)

        costumerNeed={
            'sinceFrom':"-",
            'untilTo':'',
            'aspectPositive':dataAspectPos,
            'aspectNegative':dataAspectNeg
        }

        #end bisi butuh jika ga butuh dikoment dan return listAspect

        print("endd")
        return tempListAspect,pos,neg,sort,costumerNeed


    # aspect = ['i love this coffe', 'i dislike this coffee', 'this coffe sweet', 'the store is dirty']

    #dummy for classsify
    tweet={
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': "hkhj"
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "do not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "do not love",
                'polarity': ""
            }
        ]
    }
    print ('iniiii loh yg polarity',tweet['aspects'][0]['polarity'])


    # def sentimentAnalysisAspectBase(self, tweet):
    #     aspects=[]
    #     pos=0
    #     neg=0
    #     resultPolarity = self.aspectPolarity(tweet)
    #     index = 0
    #     for i in resultPolarity:
    #         print(i)
    #         tweet['aspects'][index]['polarity'] = i
    #         if(i=="positive"):
    #             pos+=1
    #         elif(i=="negative"):
    #             neg+=1
    #         index = index + 1
    #     return tweet,pos,neg;


    #for sentence level

    tweetsText=["i love the coffee starbucks",
                   "the cake starbucks is sweet",
                   "the staff is ugly",
                    "the place is dirty",
                    "the table clean"
    ]

    def sentencePolarity(self,tweets):
        listPolarity = []
        polarityTweet={}
        pos=0
        neg=0
        for i in tweets:
            token_aspect = nltk.word_tokenize(i)
            #nanti disini diambil yg aspectnya terus dikasih lebel polaritas
            polarity = sentimentPolaritySentenceModul.polarity(token_aspect)
            if(polarity==1):
                pos+=1
            elif (polarity == 0):
                neg += 1
            polarityTweet = {
                'tweet' : i,
                'polarity': polarity
            }
            listPolarity.append(polarityTweet)
            countPolarity = {
                'pos' : pos,
                'neg' : neg
            }
        return listPolarity, countPolarity

    def sentimentAnalysisSentence(self,tweet):
        pos=0
        neg=0
        resultPolarity = self.sentencePolarity(tweet)
        index = 0
        for i in resultPolarity:
            print(i)
            tweet['aspects'][index]['polarity'] = i
            if(i==1): #positive
                pos+=1
            elif(i==0): #negative
                neg+=1
            index = index + 1
        return tweet,pos,neg;

# sa = SentimentAnalysis()
# print("inii panggil san sentence")
# res,polarity = sa.sentencePolarity(sa.tweetsText)
# for a in res:
#     print(a['tweet'],":",a['polarity'])
# print(polarity)

print("asch")
