import re
class AppropriateDataTweetFilter:
    def choosingAppropriateDataTweet(self, listTweet):
        listAppropriateDataTweetChoosed=[]

        for index in range(len(listTweet)):
            # print(listTweetText[index])
            try:
                dataTweetAboutJob = re.search(r'job', listTweet[index]["text"], re.X | re.S | re.M | re.I)
                dataTweetAboutGiveaway = re.search(r'giveaway', listTweet[index]["text"], re.X | re.S | re.M | re.I)
                dataTweetAboutStarbucks = re.search(r'starbucks', listTweet[index]["text"], re.X | re.S | re.M | re.I)
                # dataTweetAboutStarbucks = re.search(r'starbucks', listTweet[index]["text"], re.X | re.S | re.M | re.I)
                if (dataTweetAboutJob is None and dataTweetAboutGiveaway is None and dataTweetAboutStarbucks):
                    print("Nothing found!!")
                    listAppropriateDataTweetChoosed.append(listTweet[index])

                else:
                    print("Ok")

                # return listTweetText
            except Exception as e:
                return e

        return listAppropriateDataTweetChoosed