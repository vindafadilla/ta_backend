import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist, DictionaryProbDist, ELEProbDist, sum_logs
class DataPreprocessing:
    def get_words_in_tweets(self, tweets):
        self.all_worlds = []
        for (words, sentiment) in tweets:
            self.all_worlds.extend(words)
        return self.all_worlds

    def get_word_features(self, wordlist):
        wordlist = FreqDist(wordlist)
        print("word list")
        print(wordlist.items())
        print(wordlist.freq(2))
        word_features = wordlist.keys()
        print("allworlds")
        print(self.all_worlds)
        return word_features

    # for tokenize text tweet
    def tokenize1(self, all_tweets):
        tweets = []
        stopwords = ['is', 'the']
        for (words, polarity) in all_tweets:
            # words_filtered = [e.lower() for e in nltk.word_tokenize(words) if e in brown.words(categories='reviews') and e not in stopwords]
            words_filtered = [e.lower() for e in nltk.word_tokenize(words) if e not in stopwords]
            tweets.append((words_filtered, polarity))
        return tweets
    # raw = "DENNIS: Listen very cool, strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."
    # tokens = nltk.word_tokenize(raw)
    # def stemmer(self,tokens):
    #
    #     porter = nltk.PorterStemmer()
    #     liststem = []
    #     for t in tokens:
    #         liststem.append(porter.stem(t))
    #     return liststem
    # def postagger(self,tokens):
    #     postag = nltk.pos_tag(tokens);
    #     return postag
    #
    # def aspect_extraction(self,postag):
    #     aspects=[]
    #     grammar = "aspect: {<NN><VBZ><JJ>}"
    #     cp = nltk.RegexpParser(grammar)
    #     result = cp.parse(postag)
    #     print(result)
    #     print("leaves")
    #     a=result.pos()
    #     print(a)
    #     for record in a:
    #         # print out the document.
    #         try:
    #             # print(i,record['date'],record['user_name'] , record['text'], record["favorite_count"], record["user_followers_count"],record["typeMedia"])
    #             if record[1]=="aspect":
    #                 aspect = {
    #                     'word': record[0][0],
    #                     'pos' : record[0][1]
    #                 }
    #                 aspects.append(aspect)
    #         except Exception as e:
    #             # return str(e)
    #             print(str(e))
    #     return aspects
    #
    # def stopwords_removal(self,text):
    #     filter_sw=[]
    #     stop = set(stopwords.words('english'))
    #     print("ini stopwords")
    #     print(stop)
    #     sentence = text
    #     for i in sentence.lower().split():
    #         if i not in stop:
    #             filter_sw.append(i)
    #
    #     return  filter_sw;
    #
    #
    # print("coba panggil stem")
    # hasilstem =stemmer(1,tokens)
    # print(hasilstem)
    # tokens_sbx = nltk.word_tokenize("i love the coffee because the the taste is sweet")
    # print("coba panggil postag")
    # hasilpostag=postagger(1,tokens_sbx)
    # print(hasilpostag)
    # print("coba aspect")
    # hasil_aspect = aspect_extraction(1,hasilpostag)
    # for i in hasil_aspect:
    #     print(i)
    # print("coba panggil stopwords removal")
    # test_stopwords = "i love the coffee because the the taste is very sweet"
    # sw=stopwords_removal(1, test_stopwords)
    # print(sw)
    #
    #
    #
