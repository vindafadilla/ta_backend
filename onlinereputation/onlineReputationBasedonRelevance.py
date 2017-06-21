from ta_backend.dateandtime.converterDateandTime import ConverterDateandTime

class OnlineReputationBasedonRelevance:
    def calculateAspectFrequency(self, listTweetSentimentClassification, sinceFrom, untilTo):
        # totalSentimentNegative = len(listTweetSentimentClassification["negative"])
        # totalSentimentPositive = len(listTweetSentimentClassification["positive"])

        converter = ConverterDateandTime()

        totalSentiment = len(listTweetSentimentClassification)
        # sinceDateSentiment = converter.str_to_date(listTweetSentimentClassification[0]["date"])
        # untilToSentiment = converter.str_to_date(listTweetSentimentClassification[0]["date"])
        #
        listTweetAspect=[
            {
                'aspect': "general",
                'sentiment': ["love", "suck", "great"],
                'polarity': 1,
                'frequency': 1.5,
                'user_id': ["2244994945", "2244994943"],
                'tweet_id': ["2244994945", "2244994943"]
            },
            {
                'aspect': "staff",
                'sentiment': ["ugly", "yell", "great"],
                'polarity': 1,
                'frequency': 1.7,
                'user_id': ["2244994945", "2244994943"],
                'tweet_id': ["2244994945", "2244994943"]
            }
        ]

        # # Menampung Aspect dengan Polarity Positive atau Negative
        # for index in range(len(listTweetSentimentClassification)):
        #     for indexSentiment in range(len(listTweetSentimentClassification[index]["aspect"])):
        #         try:
        #             if (listTweetSentimentClassification[index]["aspect"][indexSentiment]["polarity"]=="positive"):
        #                 listTweetPositiveSentiment= listTweetSentimentClassification[index]["aspect"]
        #             else:
        #                 listTweetNegativeSentiment = listTweetSentimentClassification[index]["aspect"]
        #         except Exception as e:
        #             print(str(e))
        #
        # for index in range(len(listTweetPositiveSentiment)):
        #     #Menghitung Frequencynya
        #
        # for index in range(len(listTweetNegativeSentiment)):
        #     # Menghitung Frequencynya

        tweet = {
            "sinceFrom"         : sinceFrom,
            "untilTo"           : untilTo,
            "aspect"            : listTweetAspect
        }

        return tweet