from constant import *
from jaccard_similarity_shingling import TopSimilarityCalculator
from local_alignment_calculator import LocalAlignmentCalculator
from word_preprocessing import TextPresprocessing
import os
import json
import time

def main():
    create_path(PATH_SAMPLE)
    start_time = time.perf_counter()
    output_file = open(os.path.join(PATH_SAMPLE["ROOT"], "local_alignment_output.json"), 'w')
    output_file.write("{")
    output_file.write('"result": [')
    modified_pattern_paths = os.listdir(PATH_SAMPLE["MODIFIED_PATTERN"])
    count_txt = 0
    for modified_pattern_file in modified_pattern_paths:
        if modified_pattern_file.endswith(".txt"):
            count_txt += 1
    js_output_file = open(os.path.join(PATH_SAMPLE["ROOT"], "js_output.json"), 'w')
    js_output_file.write("[")
    for modified_pattern_file in modified_pattern_paths:
        if not modified_pattern_file.endswith(".txt"):
            continue
        count_txt -= 1
        # print('---------------------------------------------------------------')
        # print(f"Considering pattern {modified_pattern_file}")
        modified_pattern_file_path = os.path.join(PATH_SAMPLE["MODIFIED_PATTERN"], modified_pattern_file)
        pattern_content = TextPresprocessing(open(modified_pattern_file_path, "r").read()).preprocess()
        # Top 10? most similar
        top_similarity_calculator = TopSimilarityCalculator(modified_pattern_file_path)
        top_k = top_similarity_calculator.get_top_k_similar(k=NUM_TOP_JACCARD_SIMILARITY)
        json.dump({"pattern": modified_pattern_file, "js_scores": top_k}, js_output_file)
        if count_txt != 0:
            js_output_file.write(",")
        # how about clustering --> choose NUM_DB_COPIED_TO_PATTERN?
        local_alignment_scores = []
        for db_infor in top_k:
            database_file = db_infor['file']
            database_file_path = os.path.join(PATH_SAMPLE["DATABASE"], database_file)
            database_content = TextPresprocessing(open(database_file_path, "r").read()).preprocess()
            local_alignment_cal = LocalAlignmentCalculator(pattern_content, database_content)
            # print(f"score between pattern {modified_pattern_file} and db file {database_file} is {local_alignment_cal.calculate()}")
            local_alignment_scores.append({"file": database_file, "score": local_alignment_cal.calculate()})
            local_alignment_scores.sort(key = lambda la_score: la_score["score"], reverse=True)
            if len(local_alignment_scores) > NUM_DB_COPIED_TO_PATTERN:
                local_alignment_scores = local_alignment_scores[:NUM_DB_COPIED_TO_PATTERN]
        json.dump({"pattern": modified_pattern_file, "local_alignment_scores": local_alignment_scores}, output_file)
        if count_txt != 0:
            output_file.write(",")
    output_file.write("],")
    duration = time.perf_counter() - start_time
    output_file.write(f'"time_in_second": {duration},')
    output_file.write(f'"time_in_minute": {duration / 60},')
    output_file.write(f'"time_in_hour": {duration / 3600}')
    output_file.write("}")
    output_file.close()

    js_output_file.write("]")
    js_output_file.close()
        
if __name__=='__main__':
    main()