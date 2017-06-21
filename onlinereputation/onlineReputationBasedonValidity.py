from ta_backend.sentimentpolarity.sentimentAnalysis import SentimentAnalysis
from ta_backend.dummydata import dummyData
class OnlineReputationBasedonValidity:
    def onlineReputationbasdeonValidityCalculation(self):
        validity={
            'positive' : 10,
            'negative' : 1000000
        }

        return validity

    def getOnlineReputationBasedOnValidity(self,fromDate,toDate,listAspects):
        sa = SentimentAnalysis()
        res, pos, neg, wordList,costumerNeed = sa.aspectPolarity(listAspects)
        return res,pos,neg,wordList,costumerNeed