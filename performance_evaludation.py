import numpy as np
def compare_similarity(prediction0, actual0):
    prediction0 = np.array([p['score'] for p in prediction0])    
    actual0 = np.array([a['word_count'] for a in actual0])

    score_prediction = (prediction0 - prediction0.min()) / (prediction0.max() - prediction0.min())
    score_actual = (actual0 - actual0.min()) / (actual0.max() - actual0.min())
    return 1 - sum((score_prediction - score_actual) ** 2)