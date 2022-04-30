from word_preprocessing import TextPresprocessing
from constant import NUM_SHINGLES, PATH, NUM_TOP_JACCARD_SIMILARITY, DATABASE_WORD_COUNT
import os
import heapq

def get_shingles(text, k=2, sketch_size=None):
    hashed_shingles = set()
    heapq_shingles = []
    for i in range(len(text) - k + 1):
        if sketch_size == None:
            hashed_shingles.add(hash(tuple(text[i:i+k])))
        else:
            hashed_shingle = hash(tuple(text[i:i+k]))
            if not hashed_shingle in hashed_shingles:
                hashed_shingles.add(hashed_shingle)
                heapq.heappush(heapq_shingles, -hashed_shingle)
                if len(heapq_shingles) > sketch_size:
                    smallest_hashed_shingle = -heapq.heappop(heapq_shingles)
                    hashed_shingles.remove(smallest_hashed_shingle)
            
    return hashed_shingles
    
def jaccard_similarity(shingle1, shingle2):
    return len(shingle1 & shingle2) / len(shingle1 | shingle2)

class TopSimilarityCalculator:
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
    
    def get_top_k_similar(self, k=NUM_TOP_JACCARD_SIMILARITY):
        processed_pattern = TextPresprocessing(open(self.pattern_path, 'rb').read().decode('utf-8')).preprocess()
        shingle_pattern = get_shingles(processed_pattern, k=NUM_SHINGLES)
        jaccard_similarity_scores = []
        for database_file in os.listdir(PATH["DATABASE"]):
            database_file_path = os.path.join(PATH["DATABASE"], database_file)
            processed_database = TextPresprocessing(open(database_file_path, 'rb').read().decode('utf-8')).preprocess()
            shingle_database = get_shingles(processed_database, k=NUM_SHINGLES, sketch_size=DATABASE_WORD_COUNT / 4)
            jaccard_similarity_score = {"file": database_file, "score": jaccard_similarity(shingle_pattern, shingle_database)}
            jaccard_similarity_scores.append(jaccard_similarity_score)
            jaccard_similarity_scores.sort(key = lambda js_score: js_score["score"], reverse=True)
            if len(jaccard_similarity_scores) > k:
                jaccard_similarity_scores = jaccard_similarity_scores[:k]
        return jaccard_similarity_scores

if __name__=='__main__':
    cal = TopSimilarityCalculator("data_sample/news_modified_pattern/0.txt")
    print(cal.get_top_k_similar())