class CountVectorizer:
    '''class for vectorizing words and making matrixes
     with number of each word of text

     - fit_transform method retuns matrix which shows the number
     of each word
     input: list of strings
     output: list of lists of counts of words in strings

     - get_feature_names method returns list of words
      which were given in the corpus of strings
      input: None
      output: list of words
     '''
    def __init__(self, dictionary={}):
        self.dictionary = dictionary

    def fit_transform(self, text):
        self.dictionary.clear()
        matrix = []
        for sentence in text:
            for word in sentence.lower().split():
                word = word.strip(',.!?:;(){}[]')
                if word not in self.dictionary:
                    self.dictionary[word] = 1
                else:
                    self.dictionary[word] += 1

        for sentence in text:
            sentence_dict = dict.fromkeys(self.dictionary, 0)
            for word in sentence.lower().split():
                word = word.strip(',.!?:;(){}[]')
                sentence_dict[word] += 1
            matrix.append(list(sentence_dict.values()))
        return matrix

    def get_feature_names(self):
        return list(self.dictionary.keys())


def tests():
    corpus1 = [
        'Crock Pot Pasta Never boil pasta again!',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    ans1 = ['crock', 'pot', 'pasta', 'never', 'boil', 'again',
            'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    matrix1 = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    corpus2 = []
    ans2 = []
    matrix2 = []

    corpus3 = ['']
    ans3 = []
    matrix3 = [[]]

    corpus4 = ['Hello, world!', 'My name is Andrey)', 'Hello, Andrey!']
    ans4 = ['hello', 'world', 'my', 'name', 'is', 'andrey']
    matrix4 = [[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1]]

    corpus5 = ['aaaaaaaa']
    ans5 = ['aaaaaaaa']
    matrix5 = [[1]]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus1)
    assert vectorizer.get_feature_names() == ans1, 'Error in names in corpus1'
    assert count_matrix == matrix1, 'Error in matrix in corpus1'

    count_matrix = vectorizer.fit_transform(corpus2)
    assert vectorizer.get_feature_names() == ans2, 'Error in names in corpus2'
    assert count_matrix == matrix2, 'Error in matrix in corpus2'

    count_matrix = vectorizer.fit_transform(corpus3)
    assert vectorizer.get_feature_names() == ans3, 'Error in names in corpus3'
    assert count_matrix == matrix3, 'Error in matrix in corpus3'

    count_matrix = vectorizer.fit_transform(corpus4)
    assert vectorizer.get_feature_names() == ans4, 'Error in names in corpus4'
    assert count_matrix == matrix4, 'Error in matrix in corpus4'

    count_matrix = vectorizer.fit_transform(corpus5)
    assert vectorizer.get_feature_names() == ans5, 'Error in names in corpus5'
    assert count_matrix == matrix5, 'Error in matrix in corpus5'

    print('All tests were passes. Well done!')


if __name__ == '__main__':
    tests()
