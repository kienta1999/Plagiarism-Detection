from word_preprocessing import TextPresprocessing
from constant import NUM_SHINGLES

def get_shingles(text, k=2):
    hashed_shingles = set()
    for i in range(len(text) - k + 1):
        hashed_shingles.add(hash(tuple(text[i:i+k])))
    return hashed_shingles
    
def jaccard_similarity(shingle1, shingle2):
    return len(shingle1 & shingle2) / len(shingle1 | shingle2)

if __name__=='__main__':
    processed = TextPresprocessing("haha  hehe used using enjoying enjoyed enjoying enjoyed").preprocess()
    processed2 = TextPresprocessing("haha  hehe kaka keke ascasc used using enjoying enjoyed").preprocess()
    
    shingle1 = get_shingles(processed, k=NUM_SHINGLES)
    shingle2 = get_shingles(processed2, k=NUM_SHINGLES)
    print(jaccard_similarity(shingle1, shingle2))