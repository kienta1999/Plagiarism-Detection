from constant import *
import os

def generate_file(word_count, origins, target_folder):
    count = 0
    content = ""
    for raw_news in origins:
        raw_news_path = os.path.join(PATH_SAMPLE["RAW"], raw_news)
        curr_content = open(raw_news_path, 'r').read().decode('utf-8')
        if len(content.split()) < word_count:
            content += curr_content
        else:
            file = open(os.path.join(target_folder, f"{count}.txt"), "w")
            file.write(content)
            file.close()
            count += 1
            content = curr_content

        

if __name__=='__main__':
    create_path(PATH_SAMPLE)
    path_raw = os.listdir(PATH_SAMPLE["RAW"])
    count = 0
    database_count = int(len(path_raw) * PERCENTAGE_DATABASE / 100)
    path_for_database = path_raw[:database_count]
    path_for_pattern = path_raw[database_count:]
    generate_file(DATABASE_WORD_COUNT, path_for_database, PATH_SAMPLE["DATABASE"])
    generate_file(PATTERN_WORD_COUNT, path_for_pattern, PATH_SAMPLE["ORIGINAL_PATTERN"])
