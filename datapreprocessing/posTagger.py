import nltk
from nltk.tag.stanford import StanfordPOSTagger
class PosTagger:
    def postagging(self,tokens):
        postag = nltk.pos_tag(tokens);
        return postag

    def pos_tag(self, toked_sentence):
        """
        INPUT: list of strings
        OUTPUT: list of tuples
        Given a tokenized sentence, return 
        a list of tuples of form (token, POS)
        where POS is the part of speech of token
        """
        return nltk.pos_tag(toked_sentence)

    def pos_tag_stanford(self, toked_sentence):
        """
        INPUT: list of strings
        OUTPUT: list of tuples
        Given a tokenized sentence, return 
        a list of tuples of form (token, POS)
        where POS is the part of speech of token
        """


        st = StanfordPOSTagger(
            '/Users/jeff/Zipfian/opinion-mining/references/resources/stanford-pos/stanford-postagger-2014-06-16/models/english-bidirectional-distsim.tagger',
            '/Users/jeff/Zipfian/opinion-mining/references/resources/stanford-pos/stanford-postagger-2014-06-16/stanford-postagger.jar')

        return st.tag(toked_sentence)

    def insertListToDictionary(self, posTagged, originalTweetToken,sentenceDepparseList, listConsparseTree):
        listSentenceDict=[]
        for index in range(len(posTagged)):
            sentence = {
                "index"         : index,
                "parse"         : listConsparseTree[index],
                "token"         : [],
                "dependencies"  : sentenceDepparseList[index]
            }
            for index2 in range(len(posTagged[index])):
                token = {
                    "index" : index2+1,
                    "word"  : originalTweetToken[index][index2],
                    "lemma" : posTagged[index][index2][0],
                    "pos"   : posTagged[index][index2][1]
                }
                sentence["token"].append(token)
            listSentenceDict.append(sentence)

        return listSentenceDict

        #         sentence["token"].append(token)
        #         # print(sentence["token"][index2])
        #
        #     listSentenceToken.append(sentence)
        #     # print(listSentenceToken[index])