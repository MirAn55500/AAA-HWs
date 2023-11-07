from typing import List
from count_vectorizer import CountVectorizer
from tfidftransformer import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf_ = TfidfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_.fit_transform(count_matrix)


def test():
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vect = TfidfVectorizer()
    tfidf_matrix = vect.fit_transform(corpus)

    assert vect.get_feature_names() == \
           ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
            'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    assert tfidf_matrix == \
           [[0.201, 0.201, 0.286, 0.201, 0.201, 0.201,
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.201, 0.201,
             0.201, 0.201, 0.201, 0.201]]

    vect = TfidfVectorizer()
    assert vect.get_feature_names() == [], 'Имён быть не должно'
    print('Well done!')


if __name__ == '__main__':
    test()
