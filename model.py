import pandas as pd
import numpy as np

import pymongo

from dotenv import load_dotenv
import os

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('./data/processed/data.csv', index_col=0)

# df.Title = df.Title.apply(lambda x: ''.join(x.split('"')))

cm = CountVectorizer().fit_transform(df.tags)

cs = cosine_similarity(cm)

def recommend(title):
    game_id = df[df.title == title].index[0]
    
    scores = list(enumerate(cs[game_id]))
    
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    top=10
    recommendation=[]
    for item in sorted_scores[:top+1]:
        game_id_title = df.loc[df.index == item[0], ['appid', 'title']].values[0]
        recommendation.append(game_id_title)
    
    return recommendation

def game_titles():
    return df.title.tolist()