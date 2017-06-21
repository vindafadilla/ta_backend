from ta_backend.datapreparation.dataTwitter import DataTwitter
from ta_backend.datapreparation.appropriateDataTweetFilter import AppropriateDataTweetFilter
from ta_backend.datacleaning.normalization import Normalization

class DataCleaning:
    def dataCleaningProcess(self, listTweet):
        try:
            normalization = Normalization()
            print(listTweet["tweetList"][1]["text"])
            listDataTweetNormalized = []

            for index in range(len(listTweet["tweetList"])):
                dataTweetWithoutHTMLChar = normalization.escapingHTMLChar(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTweetWithoutHTMLChar
                dataTwitterURLRemoved = normalization.urlRemoval(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTwitterURLRemoved
                dataTweetWhitespacesNormalized = normalization.whitespace(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTweetWhitespacesNormalized
                dataTweetAbbreviationNormalized = normalization.abbreviations(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTweetAbbreviationNormalized
                dataTweetContractionNormalized = normalization.contractions(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTweetContractionNormalized
                dataTweetSpellfixNormalized = normalization.spellfix(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTweetSpellfixNormalized
                dataTweetAttachedWordsSplitted = normalization.splitAttachedWords(listTweet["tweetList"][index]["text_processed"])
                listTweet["tweetList"][index]["text_processed"] = dataTweetAttachedWordsSplitted
                listDataTweetNormalized.append(listTweet["tweetList"][index])

            tweetperDay = {
                'datePeriod': listTweet["datePeriod"],
                'tweetList': listDataTweetNormalized
            }
            return tweetperDay
        except Exception as e:
            return e

    # def insertToDatabase(self, listTweet):