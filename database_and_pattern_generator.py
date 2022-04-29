from constant import *
import os

def generate_database_file(word_count):
    pass

if __name__=='__main__':
    create_path(PATH_SAMPLE)
    for raw_news in os.listdir(PATH_SAMPLE["RAW"]):
        raw_news_path = os.path.join(PATH_SAMPLE["RAW"], raw_news)
