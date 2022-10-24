import logging as logger
import re
from collections import Counter
from itertools import chain
from string import punctuation

logger.basicConfig(level=logger.INFO)


class WordCount:
    """
    WordCount class is used to count the number of times a word appears in a file.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def _get_word_count(self):
        """
            # Explanation of code
            1. Open file
            2. Read line by line
            3. Find all words in line without punctuation
            4. For each word
            5. If word is empty, continue
            6. Make word lowercase
            7. If word is in word_count, add 1 to count
            8. Else, add word to word_count with count 1

            The space complexity is O(n) where n is the number of words in the file. This is because the
            word_count dictionary is storing the words and their counts.

            The running time is O(n) where n is the number of words in the file.

        :return: word_count dictionary
        """
        word_count = {}
        try:
            logger.info(f'Opening file: {self.file_path}')
            with open(self.file_path, 'r') as f:
                for line in f:
                    words = re.findall(r'\w+', line)
                    for word in words:
                        if word == '':
                            continue
                        word = word.lower()
                        word_count[word] = word_count.get(word, 0) + 1
            return word_count
        except FileNotFoundError as ex:
            logger.error(f'File not found: {self.file_path}')
            raise ex

    # space complexity: O(n*m) where n is the number of words and m is the length of the longest word
    # running time: O(n) where n is the number of words in the dictionary

    def _get_word_count_improved(self):
        """
            # Explanation of code
            1. Open file
            2. Read line by line
            3. remove punctuation from line and make it lowercase
            4. Split line into words
            5. Chain all words into one list of words
            6. Use Counter to count words in list lazily

            Down the line counter works much faster than the previous method because it uses a hash table
            to store the words and their counts. This means that it doesn't have to iterate through the
            entire list of words to find the count of a word. It can just look up the word in the hash table
            and return the count.

            The space complexity is O(n) where n is the number of words in the file. This is because the
            Counter object is storing the words and their counts in a hash table.

            The running time is O(n) where n is the number of words in the file. This is because the Counter
            object is storing the words and their counts in a hash table. This means that it doesn't have to
            iterate through the entire list of words to find the count of a word. It can just look up the word
            in the hash table and return the count.

        :return: word_count dictionary
        """
        try:
            logger.info(f'Opening file: {self.file_path}')
            with open(self.file_path, 'r') as f:
                word_count = Counter(chain.from_iterable(
                    line.lower().translate(str.maketrans('', '', punctuation)).split() for line in f))
            return word_count
        except FileNotFoundError as ex:
            logger.error(f'File not found: {self.file_path}')
            raise ex

    def get_highest_count(self):
        """
            # Explanation of code
            1. Get word count
            2. Set highest count to 0
            3. Set highest count word to empty string
            4. For each word, count in word count
            5. If count is greater than highest count
            6. Set highest count to count
            7. Set highest count word to word
            8. Return highest count word and highest count

            The space complexity is O(n) where n is iterating through the dictionary of words and their counts.

            The running time is O(1) because it is just iterating through the dictionary and comparing
            the counts to find the highest count.

        :return: highest count word and highest count i.e. ('non', 12)
        """
        try:
            word_count = self._get_word_count_improved()
            highest_count = 0
            highest_count_word = ''
            for word, count in word_count.items():
                if count > highest_count:
                    highest_count = count
                    highest_count_word = word
            return highest_count_word, highest_count
        except FileNotFoundError as ex:
            logger.error(f'File not found: {self.file_path}')
            raise ex
