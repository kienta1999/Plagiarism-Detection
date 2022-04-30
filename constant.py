NUM_SHINGLES = 2

NUM_TOP_JACCARD_SIMILARITY = 10 # how many database text that is similar to the pattern we want from the Jaccard Similarity

NUM_DB_COPIED_TO_PATTERN = 5 # how many file from database we choose to insert into a text to form a pattern

MAX_NUM_SENTENCE = 10 # maximum number of sentence from a file we choose to insert

PATH_SAMPLE = {
    "ROOT": "./data_sample",
    "RAW": "./data_sample/raw_news",
    "DATABASE": './data_sample/news_database',
    "ORIGINAL_PATTERN": './data_sample/news_original_pattern',
    "MODIFIED_PATTERN": './data_sample/news_modified_pattern'
}

PATH_MAIN = {
    "ROOT": "./data",
    "RAW": "./data/raw_news",
    "DATABASE": './data/news_database',
    "ORIGINAL_PATTERN": './data/news_original_pattern',
    "MODIFIED_PATTERN": './data/news_modified_pattern'
}

DATABASE_WORD_COUNT = 10_000
PATTERN_WORD_COUNT = 500
PERCENTAGE_DATABASE = 95

import os
def create_path(paths):
    for path in paths.values():
        if not os.path.exists(path):
            os.makedirs(path)

PATH = PATH_SAMPLE
