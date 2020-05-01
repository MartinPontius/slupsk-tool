
dict_pl = {}
dict_en = {}

dict_pl['instruction1_part1'] = 'Wir alle lieben Essen.'

dict_en['instruction1_part1'] = 'We all love food. We make sure our children eat healthily. \
                                                We are paying more and more attention to what we eat and what we buy. \
                                                What we eat affects not only us, but also the environment and our immediate surroundings. \
                                                With this application, we will try to provide you with information about food in Słupsk. \
                                                Moreover, by answering some questions in this application you can help us to better understand the food nexus. \
                                                Using the map you can:'

class Dictionary():

    def __init__(self, language):

        if language == 'pl':
            self._dictionary = dict_pl
        else:
            self._dictionary = dict_en

    def get_dict(self):

        return self._dictionary
