import string
import os
import contractions
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

os.environ["PYTHONHASHSEED"] = '0'

# https://analyticsindiamag.com/complete-tutorial-on-text-preprocessing-in-nlp/

class TextPresprocessing:
    def __init__(self, text):
        self.text = text

    def stopword_remove(self):
        clean = []
        for i in self.text:
            if i not in stopwords.words('english'):
                clean.append(i)
        self.text = clean

    def preprocess(self):
        # remove punctuation
        self.text = "".join([i if i not in string.punctuation else " " for i in self.text])
        # convert to lowercase
        self.text = self.text.lower()
        """expand shortened words, e.g. don't to do not"""
        self.text = contractions.fix(self.text)
        # tokenize, "abc def" to ["abc"]
        self.text = nltk.word_tokenize(self.text)
        self.stopword_remove()
        self.lemmatization()
        return self.text
    
    def lemmatization(self):
        lemma = WordNetLemmatizer()
        lemmas = []
        for i in self.text:
            lem = lemma.lemmatize(i, pos='v')
            lemmas.append(lem)
        self.text = lemmas  

if __name__=='__main__':
    y = TextPresprocessing("haha  hehe used using enjoying enjoyed enjoying enjoyed")
    print(y.preprocess())