import unittest

from rancho.wordcount_problem import WordCount


class TestWordCount(unittest.TestCase):
    def test_null_input(self):
        wc = WordCount(None)
        with self.assertRaises(TypeError):
            wc._get_word_count()
        with self.assertRaises(TypeError):
            wc._get_word_count_improved()
        with self.assertRaises(TypeError):
            wc.get_highest_count()

    def test_empty_input(self):
        wc = WordCount('')
        with self.assertRaises(FileNotFoundError):
            wc._get_word_count()
        with self.assertRaises(FileNotFoundError):
            wc._get_word_count_improved()
        with self.assertRaises(FileNotFoundError):
            wc.get_highest_count()

    def test_invalid_input(self):
        wc = WordCount('data/invalid.txt')
        with self.assertRaises(FileNotFoundError):
            wc._get_word_count()
        with self.assertRaises(FileNotFoundError):
            wc._get_word_count_improved()
        with self.assertRaises(FileNotFoundError):
            wc.get_highest_count()

    def test_valid_input(self):
        wc = WordCount('tests/data/sample_DataEngineering.txt')
        self.assertEqual(wc.get_highest_count(), ('non', 12))
