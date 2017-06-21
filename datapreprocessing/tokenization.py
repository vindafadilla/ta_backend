import nltk
from nltk.stem import WordNetLemmatizer
class Tokenization:
    def tokenizing(self,raw):
        tokens = nltk.word_tokenize(raw)
        return tokens
    def stemmer(self,tokens):
        porter = nltk.PorterStemmer()
        liststem = []
        for t in tokens:
            liststem.append(porter.stem(t))
        return liststem

    def lemmatization(self,tokens):
        wordnet_lemmatizer = WordNetLemmatizer()
        liststem = []
        for t in tokens:
            liststem.append(wordnet_lemmatizer.lemmatize(t))
        return liststem

    def get_sentences(review):
        """
        INPUT: full text of a review
        OUTPUT: a list of sentences
        Given the text of a review, return a list of sentences. 
        """

        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

        if isinstance(review, str):
            return sent_detector.tokenize(review)
        else:
            raise TypeError('Sentence tokenizer got type %s, expected string' % type(review))

    def tokenize(sentence):
        """
        INPUT: string (full sentence)
        OUTPUT: list of strings
        Given a sentence in string form, return 
        a tokenized list of lowercased words. 
        """

        # pt = MyPottsTokenizer(preserve_case=False)
        # return pt.tokenize(sentence)