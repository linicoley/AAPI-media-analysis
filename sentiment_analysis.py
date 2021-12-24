import nltk 
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

df = pd.read_csv(r'fox.csv')
df = df['text']
print(df)


def sentiment_scores_vader(file):
    scores = []
    analyzer = SentimentIntensityAnalyzer()
    for line in file :
        sentiment_dict = analyzer.polarity_scores(line)
    #return sentiment_dict
    scores.append(sentiment_dict)
    return scores 

#df['scores'] = df['text'].apply(lambda review: sid.polarity_scores(review))

print(sentiment_scores_vader(df))
