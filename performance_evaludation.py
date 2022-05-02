import numpy as np
import json

prediction0 = json.loads('{"pattern": "0.txt", "local_alignment_scores": [{"file": "123.txt", "score": 137}, {"file": "254.txt", "score": 85}, {"file": "80.txt", "score": 83}, {"file": "114.txt", "score": 33}, {"file": "124.txt", "score": 4}]}')
actual0 = json.loads('{"name": "0.txt", "copy_from": [{"file": "123.txt", "num_sentence": 15, "word_count": 258}, {"file": "254.txt", "num_sentence": 8, "word_count": 132}, {"file": "80.txt", "num_sentence": 6, "word_count": 117}, {"file": "114.txt", "num_sentence": 3, "word_count": 49}, {"file": "194.txt", "num_sentence": 1, "word_count": 18}]}')


def preprocess(data, isPrediction=True):
    if isPrediction:
        field_db = "local_alignment_scores"
        field_score = "score"
    else:
        field_db = "copy_from"
        field_score = "word_count"
    scores = data[field_db]
    min_score = scores[-1][field_score]
    max_score = scores[0][field_score]
    return [{"file": score["file"], "score": score[field_score] / max_score} for score in scores]
        

def compare_similarity(prediction0, actual0):
    

    scores_prediction = preprocess(prediction0, isPrediction=True)
    scores_actual = preprocess(actual0, isPrediction=False)
    rse = 0
    for score_pred in scores_prediction:
        score_actual = filter(lambda s: s["file"] == score_pred["file"], scores_actual)
        if score_actual:
            print(score_pred["score"])
            rse += (list(score_actual)[0]["score"] - score_pred["score"]) ** 2
        else:
            rse += score_pred["score"] ** 2
    return rse

    # prediction0 = np.array([p['score'] for p in prediction0])    
    # actual0 = np.array([a['word_count'] for a in actual0])
    # score_prediction = (prediction0 - prediction0.min()) / (prediction0.max() - prediction0.min())
    # score_actual = (actual0 - actual0.min()) / (actual0.max() - actual0.min())
    # return 1 - sum((score_prediction - score_actual) ** 2)

print(compare_similarity(prediction0, actual0))