from constant import *
import os
import random

random.seed(15)

def get_random_database_file():
    database_file = random.choice(os.listdir(PATH_TO_SAMPLE_DATABASE))
    return os.path.join(PATH_TO_SAMPLE_DATABASE, database_file)

# can mutate the sentence here
def get_random_text(database_file, num_sentence):
    f = open(database_file, 'r')
    content = f.read().split('.')
    index = random.randint(0, max(len(content) - num_sentence, 0))
    f.close()
    return content[index:index+num_sentence]

def mutate_origin_pattern(original_pattern_file):
    f = open(original_pattern_file, 'r')
    original_pattern = f.read().split('.')
    f.close()
    # insert from 5 different file in database
    for _ in range(NUM_DB_COPIED_TO_PATTERN):
        database_file = get_random_database_file()
        num_sentence = random.randint(1, MAX_NUM_SENTENCE)
        text_from_db = get_random_text(database_file, num_sentence)
        index_original_pattern = random.randint(0, len(original_pattern))
        # insert a random portion from db to the original pattern
        original_pattern[index_original_pattern:index_original_pattern] = text_from_db
    return original_pattern

if __name__=='__main__':
    for path in (PATH_TO_SAMPLE_DATABASE, PATH_TO_SAMPLE_ORIGINAL_PATTERN, PATH_TO_SAMPLE_MODIFIED_PATTERN):
        if not os.path.exists(path):
            os.makedirs(path)
    for original_pattern_file in os.listdir(PATH_TO_SAMPLE_ORIGINAL_PATTERN):
        original_pattern_file_path = os.path.join(PATH_TO_SAMPLE_ORIGINAL_PATTERN, original_pattern_file)
        muatated_pattern = mutate_origin_pattern(original_pattern_file_path)
        muatated_pattern_file_path = os.path.join(PATH_TO_SAMPLE_MODIFIED_PATTERN, original_pattern_file)
        f = open(muatated_pattern_file_path, 'w')
        f.write('.'.join(muatated_pattern))
        f.close()

        