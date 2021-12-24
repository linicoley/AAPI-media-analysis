import collections
import pandas as pd
import numpy as np
import matplotlib.cm as cm
from matplotlib import rcParams
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

dataset = pd.read_csv(r'fox.csv', encoding='latin-1')
print(dataset.columns)

# REMOVE NaN and EMPTY VALUES:
dataset.dropna(inplace=True)

blanks = []  # start with an empty list

for t in dataset.itertuples():  
    if type(t) == str:
        if t.isspace():        
            blanks.append()     

dataset.drop(blanks, inplace=True)

all_text = "".join(dataset['text'].str.lower())

stopwords = STOPWORDS
stopwords_arr = ['the', 'know', 'going', 'want', 'say', 'will', 'one', 'well', 'way', 'need',
'see', 'thing', 'let', 'video', 'clip', 'actually', 'said', 'lot', 'even', 'take', 'make',
'come', 'got', 'end video']

for word in stopwords_arr :
    stopwords.add(word)

wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000).generate(all_text)

rcParams['figure.figsize'] = 10, 20 
plt.imshow(wordcloud)
plt.axis("off")
plt.show()