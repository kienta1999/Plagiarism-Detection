import json
import newspaper
import os

# Create directory to store data file
path = './raw_news'

isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)

f = open("News_Category_Dataset_v2.json", "r")
for i, line in enumerate(f.readlines()):
    try:
        headline = json.loads(line)
        article = newspaper.Article(url=headline['link'], language='en')
        article.download()
        article.parse()
        content = str(article.text).replace('\nAdvertisement\n', '')
        out_file = open(f"raw_news/{i}.txt", "w") 
        out_file.write(content)
        out_file.close() 
    except:
        print(f"An exception occurred on paper {i}")
f.close()