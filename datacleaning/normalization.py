import os
import re
import html

class Normalization:

    # base = os.path.dirname(os.path.realpath(__file__))
    base = "C:/Users/Family/Downloads/OneDrive/TA KECE/Implementasi/Python/ta_backend_cobaskeleton2/ta_backendv2.2/ta_backend/"
    fabbreviations = open(base + "/kamus/abbreviations.txt", "r")
    # fbritish = open(base + "kamus/british.txt", "r")
    fcontractions = open(base + "kamus/contractions.txt", "r")
    fspellfix = open(base + "kamus/spellfix.txt", "r")
    def initialize_dict(fil):
        data = {}
        for line in fil.readlines():
            data[line.split()[0].lower().replace("_", " ")] = line.split()[1].replace("+", " ")
        return data

    abbreviations_dict = initialize_dict(fabbreviations)
    # british_dict = initialize_dict(fbritish)
    contractions_dict = initialize_dict(fcontractions)
    spellfix_dict = initialize_dict(fspellfix)

    def text_normalization(self, text, data):
        normalization = Normalization()
        text_list = text.split()
        return_text = ""
        for word in text_list:
            change = False
            for key, value in data.items():
                if key.lower() == word.lower():
                    if word.istitle():
                        return_text += value.title() + " "
                    elif word.isupper() and word != "FB":
                        return_text += value.upper() + " "
                    else:
                        return_text += value + " "
                    change = True
                    break
            if not change:
                return_text += word + " "
        return normalization.whitespace(return_text).strip()

    def urlRemoval(self, text):
        urlRemovedText = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
        return urlRemovedText

    def whitespace(self, text):
        text = re.sub('([.,!?()])', r'\1 ', text)
        text = re.sub('\s{2,}', ' ', text)
        return re.sub(r'\s([.,!?()](?:\s|$))', r'\1', text).strip()

    def abbreviations(self, text):
        normalization = Normalization()
        return normalization.text_normalization(text, normalization.abbreviations_dict)

    def spellfix(self, text):
        normalization = Normalization()
        return normalization.text_normalization(text, normalization.spellfix_dict)

    def contractions(self, text):
        normalization = Normalization()
        return normalization.text_normalization(text, normalization.contractions_dict)

    def splitAttachedWords(self, text):
        ans=" "
        for a in re.findall('[A-Z][^A-Z]*',text):
            ans += a.strip() + ' '

        return ans

    def escapingHTMLChar(self, text):
        textWithoutHTMLChar = html.unescape(text)
        return textWithoutHTMLChar