from typing import List


class CountVectorizer:
    '''class for vectorizing words and making matrixes
     with number of each word of text
     '''
    def __init__(self, dictionary=None):
        self.dictionary = dictionary

    @staticmethod
    def tokenize(text):
        '''method for tokenization of text'''
        new_text = []
        for sentence in text:
            new_sentence = []
            for word in sentence.lower().split():
                word = word.strip(',.!?:;(){}[]')
                new_sentence.append(word)
            new_text.append(new_sentence)
        return new_text

    def fit_transform(self, text: List[str]) -> List[List[int]]:
        ''' fit_transform method retuns matrix which shows the number
        of each word
        input: list of strings
        output: list of lists of counts of words in strings'''
        self.dictionary = dict()
        matrix = []
        text = CountVectorizer.tokenize(text)
        for sentence in text:
            for word in sentence:
                if word not in self.dictionary:
                    self.dictionary[word] = 1
                else:
                    self.dictionary[word] += 1

        for sentence in text:
            sentence_dict = dict.fromkeys(self.dictionary, 0)
            for word in sentence:
                sentence_dict[word] += 1
            matrix.append(list(sentence_dict.values()))
        return matrix

    def get_feature_names(self):
        '''
        get_feature_names method returns list of words
        which were given in the corpus of strings
        input: None
        output: list of words'''
        if self.dictionary is None:
            return []
        return list(self.dictionary.keys())
