from one_hot_encoder import fit_transform
import unittest


class TestEncoder(unittest.TestCase):
    def test_first(self):
        actual = fit_transform(['first sentence', 'second', 'third'])
        expected = [('first sentence', [0, 0, 1]), ('second', [0, 1, 0]),
                    ('third', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_second(self):
        actual = fit_transform(['Lorem ipsum', 'dolor sit',
                                'consectetur', 'elit'])
        expected = [('Lorem ipsum', [0, 0, 0, 1]), ('dolor sit', [0, 0, 1, 0]),
                    ('consectetur', [0, 1, 0, 0]), ('elit', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = fit_transform('')
        expected = [('', [1])]
        self.assertEqual(actual, expected)

    def test_one_word(self):
        actual = fit_transform('oneword')
        expected = 'word'
        self.assertIn(expected, actual[0][0])

    def test_none(self):
        self.assertRaises(TypeError, fit_transform)
