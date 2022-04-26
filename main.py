from constant import *
from jaccard_similarity_shingling import TopSimilarityCalculator
from local_alignment_calculator import LocalAlignmentCalculator
from word_preprocessing import TextPresprocessing
import os
import json

def main():
    output_file = open(os.path.join(PATH_TO_SAMPLE_MODIFIED_PATTERN, "output.json"), 'w')
    output_file.write("[")
    for modified_pattern_file in os.listdir(PATH_TO_SAMPLE_MODIFIED_PATTERN):
        if not modified_pattern_file.endswith(".txt"):
            continue
        print('---------------------------------------------------------------')
        print(f"Considering pattern {modified_pattern_file}")
        modified_pattern_file_path = os.path.join(PATH_TO_SAMPLE_MODIFIED_PATTERN, modified_pattern_file)
        pattern_content = TextPresprocessing(open(modified_pattern_file_path, "r").read()).preprocess()
        # Top 10? most similar
        top_similarity_calculator = TopSimilarityCalculator(modified_pattern_file_path)
        top_k = top_similarity_calculator.get_top_k_similar(k=10)
        local_alignment_scores = []
        for db_infor in top_k:
            database_file = db_infor['file']
            database_file_path = os.path.join(PATH_TO_SAMPLE_DATABASE, database_file)
            database_content = TextPresprocessing(open(database_file_path, "r").read()).preprocess()
            local_alignment_cal = LocalAlignmentCalculator(pattern_content, database_content)
            print(f"score between pattern {modified_pattern_file} and db file {database_file} is {local_alignment_cal.calculate()}")
            local_alignment_scores.append({"file": database_file, "score": local_alignment_cal.calculate()})
            local_alignment_scores.sort(key = lambda la_score: la_score["score"], reverse=True)
            if len(local_alignment_scores) > NUM_DB_COPIED_TO_PATTERN:
                local_alignment_scores = local_alignment_scores[:NUM_DB_COPIED_TO_PATTERN]
        json.dump({"pattern": modified_pattern_file, "local_alignment_scores": local_alignment_scores}, output_file)
        output_file.write(",")
    output_file.write("]")
    output_file.close()
        
if __name__=='__main__':
    main()