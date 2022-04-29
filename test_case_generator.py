from constant import *
import os
import random
import json

random.seed(15)

def get_random_database_file():
    database_file = random.choice(os.listdir(PATH_SAMPLE["DATABASE"]))
    return database_file

# can mutate the sentence here
def get_random_text(database_file, num_sentence):
    f = open(database_file, 'r')
    content = f.read().split('.')
    index = random.randint(0, max(len(content) - num_sentence, 0))
    f.close()
    return content[index:index+num_sentence]

def word_count(text_from_db):
    return sum([len(text.split()) for text in text_from_db])

def mutate_origin_pattern(original_pattern_file):
    f = open(original_pattern_file, 'r')
    original_pattern = f.read().split('.')
    f.close()
    # insert from 5 different file in database
    chosen_files = []
    for _ in range(NUM_DB_COPIED_TO_PATTERN):
        database_file = get_random_database_file()
        database_file_path = os.path.join(PATH_SAMPLE["DATABASE"], database_file)
        num_sentence = random.randint(1, MAX_NUM_SENTENCE)
        text_from_db = get_random_text(database_file_path, num_sentence)
        chosen_files.append({"file": database_file, "num_sentence": len(text_from_db), "word_count": word_count(text_from_db)})
        index_original_pattern = random.randint(0, len(original_pattern))
        # insert a random portion from db to the original pattern
        original_pattern[index_original_pattern:index_original_pattern] = text_from_db
    chosen_files.sort(key=lambda file: file["word_count"], reverse=True)
    return original_pattern, chosen_files

if __name__=='__main__':
    for path in (PATH_SAMPLE["DATABASE"], PATH_SAMPLE["ORIGINAL_PATTERN"], PATH_SAMPLE["MODIFIED_PATTERN"]):
        if not os.path.exists(path):
            os.makedirs(path)
    json_file = open(os.path.join(PATH_SAMPLE["ROOT"], "data.json"), 'w')
    json_file.write("[")
    for original_pattern_file in os.listdir(PATH_SAMPLE["ORIGINAL_PATTERN"]):
        record = {"name": original_pattern_file}
        original_pattern_file_path = os.path.join(PATH_SAMPLE["ORIGINAL_PATTERN"], original_pattern_file)
        muatated_pattern, chosen_files = mutate_origin_pattern(original_pattern_file_path)
        muatated_pattern_file_path = os.path.join(PATH_SAMPLE["MODIFIED_PATTERN"], original_pattern_file)
        f = open(muatated_pattern_file_path, 'w')
        f.write('.'.join(muatated_pattern))
        f.close()
        record["copy_from"] = chosen_files
        json.dump(record, json_file)
        json_file.write(",")
    json_file.write("]")
    json_file.close()

        