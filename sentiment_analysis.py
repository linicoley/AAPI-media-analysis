import nltk 
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

df = pd.read_csv(r"fox.csv")

def sentiment_scores_vader(texts):
    scores = []
    analyzer = SentimentIntensityAnalyzer()
    for text in texts :
        sentiment_dict = analyzer.polarity_scores(text)
        scores.append(sentiment_dict['compound'])
    return scores 

print(f"VADER:{sentiment_scores_vader("test folder/fox.RTF")}")