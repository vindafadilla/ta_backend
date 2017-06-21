from datetime import datetime

class ConverterDateandTime:
    def str_to_date(self,stringDate):
        d = datetime.strptime(stringDate,'%a %b %d %H:%M:%S %z %Y')
        a = d
        return a

    def str_to_date_tweet(self,stringDate):
        d = datetime.strptime(stringDate,'%Y-%m-%d')
        a = d
        return a
    def date_to_str(self, date):
        d = datetime.strftime(date,'%Y-%m-%d')
        a=d
        return a
