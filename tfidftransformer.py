from typing import List
import math


class TfidfTransformer:

    @staticmethod
    def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        return [[round(word / sum(row), 3) for word in row]
                for row in count_matrix]

    @staticmethod
    def idf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        idfs = []
        total_docs = len(count_matrix)
        total_words = len(count_matrix[0])
        for i in range(total_words):
            word_num = 0
            for doc in count_matrix:
                if doc[i] > 0:
                    word_num += 1
            idfs.append(round(math.log((total_docs + 1) / (word_num + 1))
                              + 1, 3))
        return idfs

    def fit_transform(self, count_matrix: List[List[int]]) -> \
            List[List[float]]:
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        res = []
        for doc in tf:
            res.append([round(doc[i] * idf[i], 3) for i in range(len(idf))])
        return res
