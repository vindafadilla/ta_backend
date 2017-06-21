class OnlineReputationBasedonDiversity:
    def onlineReputationBasedonDiversityCalculation(self, listTweet):
        totalPhoto = 0
        totalText = 0
        totalVideo = 0
        totalTweet = len(listTweet["tweetList"])
        for index in range(len(listTweet["tweetList"])):
            try:
                if (listTweet["tweetList"][index]["typeMedia"]=='photo'):
                    totalPhoto = totalPhoto + 1
                    # print("Photo")
                elif (listTweet["tweetList"][index]["typeMedia"]=='text'):
                    totalText = totalText + 1
                    # print("Photo")
                else:
                    totalVideo = totalVideo + 1
                    # print("Photo")
            except Exception as e :
                return e
        print(totalVideo,totalPhoto, totalText, totalTweet)
        totalDiversity = {
            'totalText'     : totalText,
            'totalPhoto'    : totalPhoto,
            'totalVideo'    : totalVideo
        }

        return totalDiversity
