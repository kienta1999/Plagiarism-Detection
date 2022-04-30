from word_preprocessing import TextPresprocessing
from constant import NUM_SHINGLES, PATH_SAMPLE, NUM_TOP_JACCARD_SIMILARITY
import os

def get_shingles(text, k=2):
    hashed_shingles = set()
    for i in range(len(text) - k + 1):
        hashed_shingles.add(hash(tuple(text[i:i+k])))
    return hashed_shingles
    
def jaccard_similarity(shingle1, shingle2):
    return len(shingle1 & shingle2) / len(shingle1 | shingle2)

class TopSimilarityCalculator:
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
    
    def get_top_k_similar(self, k=NUM_TOP_JACCARD_SIMILARITY):
        processed_pattern = TextPresprocessing(open(self.pattern_path, 'r').read()).preprocess()
        shingle_pattern = get_shingles(processed_pattern, k=NUM_SHINGLES)
        jaccard_similarity_scores = []
        for database_file in os.listdir(PATH_SAMPLE["DATABASE"]):
            database_file_path = os.path.join(PATH_SAMPLE["DATABASE"], database_file)
            processed_database = TextPresprocessing(open(database_file_path, 'r').read()).preprocess()
            shingle_database = get_shingles(processed_database, k=NUM_SHINGLES)
            jaccard_similarity_score = {"file": database_file, "score": jaccard_similarity(shingle_pattern, shingle_database)}
            jaccard_similarity_scores.append(jaccard_similarity_score)
            jaccard_similarity_scores.sort(key = lambda js_score: js_score["score"], reverse=True)
            if len(jaccard_similarity_scores) > k:
                jaccard_similarity_scores = jaccard_similarity_scores[:k]
        return jaccard_similarity_scores

if __name__=='__main__':
    cal = TopSimilarityCalculator("data_sample/raw_news_modified_pattern/15.txt")
    print(cal.get_top_k_similar())