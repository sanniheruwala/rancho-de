import logging as logger
import time

from rancho.wordcount_problem import WordCount

logger.basicConfig(level=logger.INFO)

if __name__ == '__main__':
    # we can use argparser to get the file path from the command line
    wc = WordCount('rancho/data/sample_DataEngineering.txt')
    start = time.time()
    logger.info('Word "%s" appears %d times' % wc.get_highest_count())
    logger.info('Time taken: {}'.format(time.time() - start))
